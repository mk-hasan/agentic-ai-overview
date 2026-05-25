"""ML playbook entries for RAG and search tools."""

PLAYBOOK_ENTRIES = {
    "metrics": {
        "title": "Forecast accuracy metrics",
        "text": (
            "Use MAPE for business reporting when demand > 0 consistently. "
            "Use RMSE when penalizing large errors matters. "
            "Target MAPE below 15% for A-class SKUs at weekly horizon."
        ),
        "tags": ["mape", "rmse", "metrics", "evaluation"],
    },
    "features": {
        "title": "Feature engineering guidelines",
        "text": (
            "Include lag-1, lag-7, lag-14 demand, 7-day rolling mean, day-of-week, "
            "month, promo_flag, and store fixed effects. Avoid leakage from future data."
        ),
        "tags": ["features", "lags", "rolling", "calendar", "promo"],
    },
    "deployment": {
        "title": "Model deployment checklist",
        "text": (
            "Require holdout MAPE improvement over naive baseline, peer review, "
            "and monitoring hooks before production. Staging shadow period: 1 week."
        ),
        "tags": ["deploy", "staging", "production", "registry", "monitoring"],
    },
    "monitoring": {
        "title": "Drift and retraining",
        "text": (
            "Monitor weekly MAPE and feature distribution drift. "
            "Retrain when drift score exceeds 0.25 or after major promotions."
        ),
        "tags": ["drift", "retrain", "monitoring", "promo"],
    },
}
