"""In-memory mock tracking when MLflow is disabled (--no-mlflow)."""

import statistics
from typing import Dict

from shared.examples.demand_forecast.constants import DEFAULT_HORIZON_DAYS

_REGISTRY: Dict[str, dict] = {}
_MODEL_COUNTER = 3000


def train_model(
    rows: list,
    *,
    sku_id: str,
    store_id: str,
    model_type: str,
    horizon_days: int,
) -> tuple[str, str]:
    global _MODEL_COUNTER
    _MODEL_COUNTER += 1
    model_id = f"fcst-{_MODEL_COUNTER}"
    _REGISTRY[model_id] = {
        "sku_id": sku_id,
        "store_id": store_id,
        "model_type": model_type,
        "horizon_days": horizon_days,
        "stage": "dev",
        "holdout_mape": 11.4 if model_type == "lightgbm" else 14.2,
    }
    msg = (
        f"Trained {model_type} model {model_id} for {sku_id}@{store_id} "
        f"(horizon={horizon_days}d). In-sample MAPE estimate: 10.8%. "
        f"[mock mode — use MLflow tracking without --no-mlflow]"
    )
    return model_id, msg


def evaluate_model(model_id: str, rows: list, holdout_days: int = 28) -> str:
    if model_id not in _REGISTRY:
        return f"Unknown model {model_id}."
    meta = _REGISTRY[model_id]
    mape = meta.get("holdout_mape", 11.4)
    baseline = 16.5
    return (
        f"Evaluation {model_id} on {holdout_days}-day holdout: MAPE {mape}% "
        f"(naive baseline {baseline}%). Bias: -0.3 units/day. "
        f"{'PASS' if mape < baseline else 'FAIL'} vs baseline. [mock mode]"
    )


def register_model(model_id: str, stage: str = "staging") -> str:
    if model_id not in _REGISTRY:
        return f"Cannot register unknown model {model_id}."
    _REGISTRY[model_id]["stage"] = stage
    return f"Registered {model_id} to stage '{stage}' in the mock registry. [mock mode]"


def generate_forecast(model_id: str, days: int = DEFAULT_HORIZON_DAYS) -> str:
    if model_id not in _REGISTRY:
        return f"Unknown model {model_id}."
    meta = _REGISTRY[model_id]
    return (
        f"{days}-day forecast from {model_id} for {meta['sku_id']}@{meta['store_id']}: "
        f"avg 24/26/25... units/day (mock series). Total: {days * 25} units. [mock mode]"
    )


def list_recent_runs(sku_id: str = "", store_id: str = "", limit: int = 5) -> str:
    items = list(_REGISTRY.items())
    if not items:
        return "No mock runs recorded. [mock mode]"
    lines = []
    for model_id, meta in items[-limit:]:
        if sku_id and meta.get("sku_id") != sku_id:
            continue
        if store_id and meta.get("store_id") != store_id:
            continue
        lines.append(
            f"{model_id} | {meta['sku_id']}@{meta['store_id']} | "
            f"MAPE {meta.get('holdout_mape')}% | type {meta['model_type']}"
        )
    return "Recent mock runs:\n" + "\n".join(lines) if lines else "No matching mock runs."


def get_best_run(sku_id: str, store_id: str, metric: str = "holdout_mape", maximize: bool = False) -> str:
    candidates = [
        (mid, meta)
        for mid, meta in _REGISTRY.items()
        if meta.get("sku_id") == sku_id and meta.get("store_id") == store_id
    ]
    if not candidates:
        return f"No mock runs for {sku_id}@{store_id}. [mock mode]"
    best_id, best_meta = min(candidates, key=lambda x: x[1].get("holdout_mape", 999))
    return (
        f"Best mock run for {sku_id}@{store_id}: {best_id} "
        f"with holdout_mape={best_meta.get('holdout_mape')}. [mock mode]"
    )
