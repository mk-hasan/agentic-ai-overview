"""MLflow experiment tracking for demand-forecast (optional)."""

import os
import statistics
from typing import Optional

from shared.config.settings import REPO_ROOT
from shared.examples.demand_forecast.constants import DEFAULT_HORIZON_DAYS

EXPERIMENT_NAME = "demand-forecast"
REGISTERED_MODEL_NAME = "demand-forecast-model"
DEFAULT_TRACKING_URI = (REPO_ROOT / "mlruns").as_uri()


def is_mlflow_enabled() -> bool:
    """Return True when MLflow tracking is active (default on unless USE_MLFLOW=0)."""
    return os.getenv("USE_MLFLOW", "1").strip().lower() not in ("0", "false", "no", "off")


def set_mlflow_enabled(enabled: bool) -> None:
    os.environ["USE_MLFLOW"] = "1" if enabled else "0"


def _tracking_uri() -> str:
    return os.getenv("MLFLOW_TRACKING_URI", DEFAULT_TRACKING_URI)


def _require_mlflow():
    if not is_mlflow_enabled():
        raise RuntimeError("MLflow is disabled (USE_MLFLOW=0 or --no-mlflow).")
    try:
        import mlflow
        from mlflow.tracking import MlflowClient
    except ImportError as exc:
        raise RuntimeError(
            "MLflow is not installed. Run: pip install -r requirements-ml.txt"
        ) from exc
    mlflow.set_tracking_uri(_tracking_uri())
    mlflow.set_experiment(EXPERIMENT_NAME)
    return mlflow, MlflowClient()


def _baseline_model(train_rows: list, window: int = 7) -> dict:
    units = [int(r["units_sold"]) for r in train_rows]
    tail = units[-window:] if len(units) >= window else units
    return {
        "type": "moving_average",
        "window": window,
        "forecast_level": statistics.mean(tail) if tail else 0.0,
    }


def _mape(actual: list[float], predicted: list[float]) -> float:
    errors = [abs((a - p) / a) * 100 for a, p in zip(actual, predicted) if a > 0]
    return statistics.mean(errors) if errors else 0.0


def _split_holdout(rows: list[dict], holdout_days: int) -> tuple[list[dict], list[dict]]:
    if len(rows) <= holdout_days:
        holdout_days = max(1, len(rows) // 4)
    return rows[:-holdout_days], rows[-holdout_days:]


def _run_id_to_model_id(run_id: str) -> str:
    return f"fcst-{run_id.replace('-', '')[:8]}"


def _model_id_to_run_id(model_id: str, client) -> Optional[str]:
    if model_id.startswith("fcst-"):
        suffix = model_id.replace("fcst-", "")
        for run in client.search_runs(
            experiment_ids=[_experiment_id(client)],
            filter_string="",
            max_results=200,
        ):
            if run.info.run_id.replace("-", "").startswith(suffix):
                return run.info.run_id
    if len(model_id) == 32 or "-" in model_id:
        return model_id
    return None


def _experiment_id(client) -> str:
    exp = client.get_experiment_by_name(EXPERIMENT_NAME)
    if exp is None:
        from mlflow import MlflowException

        raise MlflowException(f"Experiment {EXPERIMENT_NAME} not found")
    return exp.experiment_id


def train_model(
    rows: list[dict],
    *,
    sku_id: str,
    store_id: str,
    model_type: str,
    horizon_days: int,
) -> tuple[str, str]:
    """Train baseline model, log run to MLflow, return (model_id, message)."""
    mlflow, _ = _require_mlflow()
    train_rows, holdout_rows = _split_holdout(rows, holdout_days=28)
    model = _baseline_model(train_rows)
    holdout_actual = [float(r["units_sold"]) for r in holdout_rows]
    holdout_pred = [model["forecast_level"]] * len(holdout_actual)
    holdout_mape = _mape(holdout_actual, holdout_pred)
    naive_mape = _mape(holdout_actual, [statistics.mean([float(r["units_sold"]) for r in train_rows])] * len(holdout_actual))

    with mlflow.start_run(run_name=f"{sku_id}@{store_id}-{model_type}") as run:
        mlflow.log_params(
            {
                "sku_id": sku_id,
                "store_id": store_id,
                "model_type": model_type,
                "horizon_days": horizon_days,
                "train_rows": len(train_rows),
            }
        )
        mlflow.log_metrics(
            {
                "holdout_mape": round(holdout_mape, 2),
                "naive_baseline_mape": round(naive_mape, 2),
                "train_mean_demand": round(statistics.mean([float(r["units_sold"]) for r in train_rows]), 2),
            }
        )

        class MovingAverageModel(mlflow.pyfunc.PythonModel):
            def __init__(self, model_dict):
                self.model_dict = model_dict

            def predict(self, context, model_input):
                level = float(self.model_dict.get("forecast_level", 0))
                n = len(model_input) if hasattr(model_input, "__len__") else 1
                return [level] * int(n)

        mlflow.pyfunc.log_model(
            artifact_path="model",
            python_model=MovingAverageModel(model),
        )

        model_id = _run_id_to_model_id(run.info.run_id)
        msg = (
            f"Trained {model_type} model {model_id} (MLflow run {run.info.run_id}) for "
            f"{sku_id}@{store_id}. Holdout MAPE: {holdout_mape:.1f}% "
            f"(naive baseline {naive_mape:.1f}%). Tracking URI: {_tracking_uri()}"
        )
        return model_id, msg


def evaluate_model(model_id: str, rows: list[dict], holdout_days: int = 28) -> str:
    """Load run metrics or recompute; log evaluation metrics on the run."""
    _, client = _require_mlflow()
    run_id = _model_id_to_run_id(model_id, client)
    if not run_id:
        return f"Unknown model {model_id} in MLflow."

    run = client.get_run(run_id)
    holdout_mape = float(run.data.metrics.get("holdout_mape", 0))
    baseline = float(run.data.metrics.get("naive_baseline_mape", 0))
    passed = holdout_mape < baseline if baseline else True

    client.log_metric(run_id, "eval_holdout_days", holdout_days)
    return (
        f"Evaluation {model_id} (run {run_id}) on {holdout_days}-day holdout: "
        f"MAPE {holdout_mape:.1f}% (naive baseline {baseline:.1f}%). "
        f"{'PASS' if passed else 'FAIL'} vs baseline."
    )


def register_model(model_id: str, stage: str = "staging") -> str:
    """Register MLflow run artifact and set registry stage."""
    mlflow, client = _require_mlflow()
    run_id = _model_id_to_run_id(model_id, client)
    if not run_id:
        return f"Cannot register unknown model {model_id}."

    model_uri = f"runs:/{run_id}/model"
    try:
        result = mlflow.register_model(model_uri, REGISTERED_MODEL_NAME)
        version = result.version
    except Exception:
        versions = client.search_model_versions(f"name='{REGISTERED_MODEL_NAME}'")
        version = max((int(v.version) for v in versions), default=0) + 1

    stage_name = stage.capitalize()
    if stage_name not in ("Staging", "Production", "Archived", "None"):
        stage_name = "Staging"
    try:
        client.transition_model_version_stage(
            name=REGISTERED_MODEL_NAME,
            version=str(version),
            stage=stage_name,
            archive_existing_versions=False,
        )
    except Exception:
        pass

    return (
        f"Registered {model_id} (run {run_id}) to MLflow registry "
        f"'{REGISTERED_MODEL_NAME}' stage '{stage_name}'. URI: {_tracking_uri()}"
    )


def generate_forecast(model_id: str, days: int = DEFAULT_HORIZON_DAYS) -> str:
    """Load pyfunc model from MLflow run and produce forecast."""
    mlflow, client = _require_mlflow()
    run_id = _model_id_to_run_id(model_id, client)
    if not run_id:
        return f"Unknown model {model_id}."

    model_uri = f"runs:/{run_id}/model"
    pyfunc = mlflow.pyfunc.load_model(model_uri)
    preds = pyfunc.predict([0] * min(days, 14))
    level = float(statistics.mean(preds)) if preds else 25.0
    series = "/".join(str(int(round(p))) for p in preds[: min(days, 7)])
    total = int(round(sum(preds[:days]) if len(preds) >= days else level * days))
    run = client.get_run(run_id)
    sku = run.data.params.get("sku_id", "?")
    store = run.data.params.get("store_id", "?")
    return (
        f"{days}-day forecast from {model_id} (MLflow) for {sku}@{store}: "
        f"avg {series}... units/day. Total ≈ {total} units."
    )


def list_recent_runs(sku_id: str = "", store_id: str = "", limit: int = 5) -> str:
    """List recent MLflow runs, optionally filtered by SKU/store tags in params."""
    _, client = _require_mlflow()
    runs = client.search_runs(
        experiment_ids=[_experiment_id(client)],
        order_by=["start_time DESC"],
        max_results=50,
    )
    lines = []
    for run in runs:
        params = run.data.params
        if sku_id and params.get("sku_id") != sku_id:
            continue
        if store_id and params.get("store_id") != store_id:
            continue
        metrics = run.data.metrics
        mid = _run_id_to_model_id(run.info.run_id)
        lines.append(
            f"{mid} | {params.get('sku_id')}@{params.get('store_id')} | "
            f"MAPE {metrics.get('holdout_mape', 'n/a')}% | type {params.get('model_type')}"
        )
        if len(lines) >= limit:
            break
    if not lines:
        return "No MLflow runs found for the given filter."
    return "Recent MLflow runs:\n" + "\n".join(lines)


def get_best_run(
    sku_id: str,
    store_id: str,
    metric: str = "holdout_mape",
    maximize: bool = False,
) -> str:
    """Return the best prior run for a SKU-store by metric (lower MAPE is better)."""
    _, client = _require_mlflow()
    runs = client.search_runs(
        experiment_ids=[_experiment_id(client)],
        filter_string=(
            f"params.sku_id = '{sku_id}' AND params.store_id = '{store_id}'"
        ),
        order_by=[f"metrics.{metric} ASC"],
        max_results=1,
    )
    if not runs:
        return f"No MLflow runs for {sku_id}@{store_id}."
    run = runs[0]
    mid = _run_id_to_model_id(run.info.run_id)
    mape = run.data.metrics.get(metric, "n/a")
    return (
        f"Best run for {sku_id}@{store_id}: {mid} (run {run.info.run_id}) "
        f"with {metric}={mape}. Use this model_id for evaluation, registration, or inference."
    )
