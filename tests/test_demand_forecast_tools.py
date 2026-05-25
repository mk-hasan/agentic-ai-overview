"""Tests for demand forecast tools (mock MLflow backend)."""

import re

from shared.examples.demand_forecast.constants import DEFAULT_SKU, DEFAULT_STORE
from shared.examples.demand_forecast.tools import (
    evaluate_model,
    load_demand_data,
    train_forecast_model,
)
from shared.examples.demand_forecast.mlflow_tracking import set_mlflow_enabled


def test_load_demand_data_returns_rows():
    set_mlflow_enabled(False)
    result = load_demand_data.invoke({"sku_id": DEFAULT_SKU, "store_id": DEFAULT_STORE})
    assert DEFAULT_SKU in result
    assert "rows" in result.lower() or "Loaded" in result


def test_train_and_evaluate_mock_pipeline():
    set_mlflow_enabled(False)
    train_out = train_forecast_model.invoke(
        {"sku_id": DEFAULT_SKU, "store_id": DEFAULT_STORE, "horizon_days": 14}
    )
    assert "fcst-" in train_out
    model_id = re.search(r"fcst-\d+", train_out).group(0)
    eval_out = evaluate_model.invoke({"model_id": model_id, "holdout_days": 28})
    assert "MAPE" in eval_out or "mape" in eval_out.lower()
