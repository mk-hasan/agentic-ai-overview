"""Generate synthetic demand history for the demand-forecast scenario."""

import csv
import json
import random
from datetime import date, timedelta
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent
RANDOM_SEED = 42


def generate_daily_demand(days: int = 120) -> list[dict]:
    random.seed(RANDOM_SEED)
    start = date(2025, 12, 1)
    skus = ["SKU-100", "SKU-200", "SKU-300", "SKU-400", "SKU-500"]
    stores = ["STORE-NYC", "STORE-LA", "STORE-CHI"]
    rows = []
    for offset in range(days):
        day = start + timedelta(days=offset)
        dow = day.weekday()
        for sku in skus:
            for store in stores:
                base = 18 + (hash(f"{sku}-{store}") % 17)
                weekend_lift = 6 if dow >= 5 else 0
                trend = offset // 25
                promo = random.random() < 0.07
                noise = random.gauss(0, 2.5)
                units = max(0, int(base + weekend_lift + trend + (12 if promo else 0) + noise))
                rows.append(
                    {
                        "date": day.isoformat(),
                        "sku_id": sku,
                        "store_id": store,
                        "units_sold": units,
                        "promo_flag": int(promo),
                        "avg_price": round(19.99 + (hash(sku) % 30), 2),
                    }
                )
    return rows


def write_outputs() -> None:
    rows = generate_daily_demand()
    csv_path = DATA_DIR / "demand_daily.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f, fieldnames=["date", "sku_id", "store_id", "units_sold", "promo_flag", "avg_price"]
        )
        writer.writeheader()
        writer.writerows(rows)

    catalog = {
        "SKU-100": {"name": "Organic granola 500g", "category": "grocery", "lead_time_days": 3},
        "SKU-200": {"name": "Sparkling water 12-pack", "category": "beverage", "lead_time_days": 2},
        "SKU-300": {"name": "Protein bars box", "category": "snacks", "lead_time_days": 4},
        "SKU-400": {"name": "House blend coffee 1kg", "category": "grocery", "lead_time_days": 5},
        "SKU-500": {"name": "Frozen berries 1kg", "category": "frozen", "lead_time_days": 3},
    }
    (DATA_DIR / "sku_catalog.json").write_text(json.dumps(catalog, indent=2), encoding="utf-8")

    run_log = [
        {
            "run_id": "RUN-101",
            "sku_id": "SKU-100",
            "store_id": "STORE-NYC",
            "step": "evaluation",
            "note": "MAPE 11.2% on 4-week holdout",
        },
        {
            "run_id": "RUN-102",
            "sku_id": "SKU-200",
            "store_id": "STORE-LA",
            "step": "training",
            "note": "LightGBM beat naive baseline by 18%",
        },
        {
            "run_id": "RUN-103",
            "sku_id": "SKU-300",
            "store_id": "STORE-CHI",
            "step": "monitoring",
            "note": "Drift score 0.31 after promo week",
        },
        {
            "run_id": "RUN-104",
            "sku_id": "SKU-400",
            "store_id": "STORE-NYC",
            "step": "deployment",
            "note": "Promoted model v3 to staging",
        },
    ]
    (DATA_DIR / "pipeline_runs.json").write_text(json.dumps(run_log, indent=2), encoding="utf-8")

    event = {
        "type": "scheduled_retrain",
        "trigger": "weekly_schedule",
        "scope": {"sku_ids": ["SKU-100", "SKU-200"], "stores": ["STORE-NYC", "STORE-LA"]},
        "reason": "Scheduled refresh plus drift alert on SKU-100",
        "requested_at": "2026-05-25T06:00:00Z",
    }
    (DATA_DIR / "retrain_event.json").write_text(json.dumps(event, indent=2), encoding="utf-8")

    summary = {
        "rows": len(rows),
        "date_range": [rows[0]["date"], rows[-1]["date"]],
        "skus": len(catalog),
        "stores": 3,
    }
    (DATA_DIR / "dataset_summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(f"Wrote {len(rows)} rows to {csv_path}")


if __name__ == "__main__":
    write_outputs()
