"""Parallel MLDLC checks for demand forecast scenario."""

from shared.examples.demand_forecast.constants import DEFAULT_SKU, DEFAULT_STORE
from shared.examples.demand_forecast.tools import check_data_drift, load_demand_data, run_eda


def run_parallel_checks(user_request: str) -> dict:
    return {
        "demand_data": load_demand_data.invoke({"sku_id": DEFAULT_SKU, "store_id": DEFAULT_STORE}),
        "eda": run_eda.invoke({"sku_id": DEFAULT_SKU, "store_id": DEFAULT_STORE}),
        "drift": check_data_drift.invoke({"sku_id": DEFAULT_SKU, "store_id": DEFAULT_STORE}),
    }
