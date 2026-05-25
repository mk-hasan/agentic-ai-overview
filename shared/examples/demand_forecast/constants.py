"""Demand forecasting ML pipeline scenario — constants."""

SCENARIO_NAME = "Demand Forecast ML Pipeline"

# MLDLC phases (Machine Learning Development Life Cycle)
MLDLC_STEPS = [
    "1. Business understanding — define forecast horizon, granularity, success metrics",
    "2. Data acquisition — load historical demand and catalog metadata",
    "3. Exploratory data analysis — seasonality, missing data, outliers",
    "4. Data preparation — features: lags, rolling stats, calendar, promotions",
    "5. Model development — train baseline + candidate forecast models",
    "6. Model evaluation — backtest MAPE/RMSE on holdout window",
    "7. Model deployment — register approved model to staging/production",
    "8. Monitoring — track drift and schedule retraining",
]

DEFAULT_QUESTION = (
    "Build a 14-day demand forecast for SKU-100 at STORE-NYC. "
    "Walk through the ML lifecycle, train a model, evaluate MAPE, and recommend deployment."
)

FOLLOW_UP_QUESTION = (
    "Drift was detected on SKU-100 after last week's promotion. "
    "Should we retrain and promote a new model to production?"
)

DEFAULT_SKU = "SKU-100"
DEFAULT_STORE = "STORE-NYC"
DEFAULT_HORIZON_DAYS = 14

PLAN_FALLBACK_STEPS = [
    "Frame problem: horizon, metric (MAPE), SKU-store scope",
    "Load demand history and run EDA",
    "Prepare features and train forecast model",
    "Evaluate on holdout and compare to baseline",
    "Recommend deployment or retrain",
]
