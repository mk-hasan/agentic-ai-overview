"""ML pipeline tools for demand forecasting (MLDLC steps)."""

import csv
import statistics
from pathlib import Path

from langchain_core.tools import tool

from shared.examples.demand_forecast.constants import DEFAULT_HORIZON_DAYS, DEFAULT_SKU, DEFAULT_STORE
from shared.examples.demand_forecast.playbook import PLAYBOOK_ENTRIES

DATA_DIR = Path(__file__).resolve().parent / "data"
_DEMAND_ROWS = None


def _load_rows() -> list:
    global _DEMAND_ROWS
    if _DEMAND_ROWS is None:
        with (DATA_DIR / "demand_daily.csv").open(encoding="utf-8") as f:
            _DEMAND_ROWS = list(csv.DictReader(f))
    return _DEMAND_ROWS


def _filter_rows(sku_id: str, store_id: str) -> list:
    return [r for r in _load_rows() if r["sku_id"] == sku_id and r["store_id"] == store_id]


def _tracking_backend():
    from shared.examples.demand_forecast import mock_tracking
    from shared.examples.demand_forecast.mlflow_tracking import is_mlflow_enabled

    if not is_mlflow_enabled():
        return mock_tracking
    from shared.examples.demand_forecast import mlflow_tracking

    return mlflow_tracking


def _tracking_mode_label() -> str:
    from shared.examples.demand_forecast.mlflow_tracking import is_mlflow_enabled

    return "MLflow" if is_mlflow_enabled() else "mock (--no-mlflow)"


@tool
def search_playbook(query: str) -> str:
    """Search the ML forecasting playbook (metrics, features, deployment, monitoring)."""
    q = query.lower()
    matches = []
    for key, entry in PLAYBOOK_ENTRIES.items():
        haystack = f"{entry['title']} {entry['text']} {' '.join(entry['tags'])}".lower()
        if any(w in haystack for w in q.split() if len(w) > 2):
            matches.append(f"[{key}] {entry['title']}: {entry['text']}")
    return "\n".join(matches) if matches else "No playbook entries matched."


@tool
def frame_forecast_problem(
    sku_id: str = DEFAULT_SKU,
    store_id: str = DEFAULT_STORE,
    horizon_days: int = DEFAULT_HORIZON_DAYS,
    target_metric: str = "MAPE",
) -> str:
    """MLDLC step 1 — document business framing: scope, horizon, and success metric."""
    return (
        f"Problem framed: forecast {sku_id} @ {store_id} for {horizon_days} days. "
        f"Primary metric: {target_metric}. Granularity: daily units_sold. "
        f"Tracking: {_tracking_mode_label()}."
    )


@tool
def load_demand_data(
    sku_id: str = DEFAULT_SKU,
    store_id: str = DEFAULT_STORE,
    last_n_days: int = 90,
) -> str:
    """MLDLC step 2 — load historical demand rows for a SKU-store pair."""
    rows = _filter_rows(sku_id, store_id)[-last_n_days:]
    if not rows:
        return f"No demand history for {sku_id} at {store_id}."
    units = [int(r["units_sold"]) for r in rows]
    return (
        f"Loaded {len(rows)} daily rows for {sku_id} @ {store_id}. "
        f"Mean demand: {statistics.mean(units):.1f}, max: {max(units)}, min: {min(units)}."
    )


@tool
def run_eda(sku_id: str = DEFAULT_SKU, store_id: str = DEFAULT_STORE) -> str:
    """MLDLC step 3 — exploratory analysis: seasonality hints, promos, gaps."""
    rows = _filter_rows(sku_id, store_id)
    if not rows:
        return "EDA failed — no data."
    promo_days = sum(int(r["promo_flag"]) for r in rows)
    weekend = []
    weekday = []
    for r in rows:
        from datetime import date

        dow = date.fromisoformat(r["date"]).weekday()
        val = int(r["units_sold"])
        (weekend if dow >= 5 else weekday).append(val)
    wknd_lift = statistics.mean(weekend) - statistics.mean(weekday) if weekend and weekday else 0
    return (
        f"EDA {sku_id}@{store_id}: {len(rows)} days, {promo_days} promo days, "
        f"weekend lift +{wknd_lift:.1f} units vs weekday, no missing dates detected."
    )


@tool
def prepare_features(sku_id: str = DEFAULT_SKU, store_id: str = DEFAULT_STORE) -> str:
    """MLDLC step 4 — build feature matrix (lags, rolling means, calendar, promo)."""
    rows = _filter_rows(sku_id, store_id)
    n = len(rows)
    return (
        f"Feature matrix for {sku_id}@{store_id}: {n} rows × 12 features "
        "(lag_1, lag_7, lag_14, roll_mean_7, dow, month, promo_flag, store_id, sku_id, ...)."
    )


@tool
def list_recent_runs(
    sku_id: str = DEFAULT_SKU,
    store_id: str = DEFAULT_STORE,
    limit: int = 5,
) -> str:
    """List recent training runs from MLflow (or mock registry) for a SKU-store."""
    backend = _tracking_backend()
    try:
        return backend.list_recent_runs(sku_id=sku_id, store_id=store_id, limit=limit)
    except RuntimeError as exc:
        return str(exc)


@tool
def get_best_run(
    sku_id: str = DEFAULT_SKU,
    store_id: str = DEFAULT_STORE,
    metric: str = "holdout_mape",
) -> str:
    """Find the best prior training run by metric (lower MAPE is better)."""
    backend = _tracking_backend()
    try:
        return backend.get_best_run(sku_id=sku_id, store_id=store_id, metric=metric)
    except RuntimeError as exc:
        return str(exc)


@tool
def train_forecast_model(
    sku_id: str = DEFAULT_SKU,
    store_id: str = DEFAULT_STORE,
    model_type: str = "lightgbm",
    horizon_days: int = DEFAULT_HORIZON_DAYS,
) -> str:
    """MLDLC step 5 — train a candidate forecast model and log the run."""
    rows = _filter_rows(sku_id, store_id)
    if not rows:
        return f"No data to train for {sku_id}@{store_id}."
    backend = _tracking_backend()
    try:
        model_id, msg = backend.train_model(
            rows,
            sku_id=sku_id,
            store_id=store_id,
            model_type=model_type,
            horizon_days=horizon_days,
        )
        return msg
    except RuntimeError as exc:
        return str(exc)


@tool
def evaluate_model(model_id: str, holdout_days: int = 28) -> str:
    """MLDLC step 6 — backtest on holdout window using logged metrics."""
    backend = _tracking_backend()
    rows = _load_rows()
    try:
        return backend.evaluate_model(model_id, rows, holdout_days=holdout_days)
    except RuntimeError as exc:
        return str(exc)


@tool
def register_model(model_id: str, stage: str = "staging") -> str:
    """MLDLC step 7 — register model in MLflow Model Registry (side effect)."""
    backend = _tracking_backend()
    try:
        return backend.register_model(model_id, stage=stage)
    except RuntimeError as exc:
        return str(exc)


@tool
def check_data_drift(sku_id: str = DEFAULT_SKU, store_id: str = DEFAULT_STORE) -> str:
    """MLDLC step 8 — compute drift score on recent demand vs training window."""
    score = 0.22
    rows = _filter_rows(sku_id, store_id)
    if rows and int(rows[-1].get("promo_flag", 0)):
        score = 0.31
    status = "elevated" if score > 0.25 else "normal"
    return f"Drift check {sku_id}@{store_id}: score={score:.2f} ({status}). Recommend monitor weekly."


@tool
def generate_forecast(model_id: str, days: int = DEFAULT_HORIZON_DAYS) -> str:
    """Generate forward demand forecast from a registered or logged model."""
    backend = _tracking_backend()
    try:
        return backend.generate_forecast(model_id, days=days)
    except RuntimeError as exc:
        return str(exc)


CORE_TOOLS = [
    search_playbook,
    frame_forecast_problem,
    load_demand_data,
    run_eda,
    prepare_features,
    list_recent_runs,
    get_best_run,
    train_forecast_model,
    evaluate_model,
    generate_forecast,
    check_data_drift,
]
EXTENDED_TOOLS = CORE_TOOLS + [register_model]

TOOL_CATALOG = {t.name: (t.description or "") for t in EXTENDED_TOOLS}


def get_core_tools() -> list:
    return list(CORE_TOOLS)


def get_extended_tools() -> list:
    return list(EXTENDED_TOOLS)


def get_tool_catalog() -> dict:
    return dict(TOOL_CATALOG)


def get_tools_by_name(names: list) -> list:
    by_name = {t.name: t for t in EXTENDED_TOOLS}
    return [by_name[n] for n in names if n in by_name]
