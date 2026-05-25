> [English](../use-cases/demand-forecast.md) | **বাংলা**

# Demand Forecast ML Pipeline

রিটেইল SKU-store চাহিদা পূর্বাভাসের **Machine Learning Development Life Cycle (MLDLC)**-এর এজেন্টিক orchestration। Synthetic data ও **MLflow tracking** (ঐচ্ছিক) — train → evaluate → register → infer।

## কেন agentic AI-তে মানায়

| MLDLC ধাপ | Agentic প্যাটার্ন |
|-----------|-------------------|
| 1 Business understanding | Planning, prompt chaining |
| 2 Data acquisition | Tool use, ReAct |
| 3 EDA | Parallelization |
| 4 Feature prep | Tool use, specialist workers |
| 5 Model training | ReAct, orchestrator–workers |
| 6 Evaluation | Evaluator–optimizer |
| 7 Deployment | HITL (`register_model`) |
| 8 Monitoring | Event-driven retrain, handoff |

এজেন্ট **orchestrate** করে; টুল **MLflow** (বা mock) কল করে।

## MLflow tracking

| মোড | কীভাবে |
|-----|--------|
| **MLflow on** (ডিফল্ট) | params, MAPE, registry |
| **Mock** | `--no-mlflow` বা `USE_MLFLOW=0` |

```bash
pip install -r requirements-ml.txt
mlflow ui --backend-store-uri mlruns
```

### নতুন টুল

| টুল | উদ্দেশ্য |
|-----|---------|
| `list_recent_runs` | SKU-store-এর prior trainings |
| `get_best_run` | `holdout_mape` অনুযায়ী best run |
| `train_forecast_model` | baseline train + log |
| `evaluate_model` | metrics compare |
| `register_model` | Registry (HITL in 09) |
| `generate_forecast` | inference |

## MLDLC (আট ধাপ)

1. Business understanding — horizon, SKU, store, MAPE
2. Data acquisition — `demand_daily.csv`
3. EDA — seasonality, promos, gaps
4. Data preparation — lags, rolling, calendar
5. Model development — train + MLflow run
6. Evaluation — holdout MAPE vs baseline
7. Deployment — staging/production (HITL)
8. Monitoring — drift, retrain events

## Synthetic data

| ফাইল | বিষয়বস্তু |
|------|-----------|
| `data/demand_daily.csv` | 1,800 rows — 5 SKU × 3 store × 120 days |
| `data/sku_catalog.json` | product metadata |
| `data/pipeline_runs.json` | map–reduce |
| `data/retrain_event.json` | retrain event |
| `data/kb/*.md` | forecasting playbook (RAG) |

```bash
python shared/examples/demand_forecast/data/generate_data.py
```

## চালান

```bash
python patterns/01-react/example/main.py --scenario demand-forecast --provider openai
python patterns/01-react/example/main.py --scenario demand-forecast --no-mlflow
python patterns/09-human-in-the-loop/example/main.py --scenario demand-forecast --auto-approve
mlflow ui
```

## শেয়ার্ড কোড

- `shared/examples/demand_forecast/tools.py`
- `shared/examples/demand_forecast/mlflow_tracking.py`
- `shared/examples/demand_forecast/mock_tracking.py`
- [MCP architecture](../architecture/mcp.md)

তুলনা: [IT Helpdesk](it-helpdesk.md), [E-commerce](ecommerce-order-support.md)।
