> **English** | [বাংলা](../bn/use-cases/demand-forecast.md)

# Demand Forecast ML Pipeline

Agentic orchestration of the **Machine Learning Development Life Cycle (MLDLC)** for retail SKU-store demand forecasting. Synthetic data and **MLflow tracking** (optional) back train → evaluate → register → infer.

## Why this use case fits agentic AI

| MLDLC step | Agentic pattern |
|------------|-----------------|
| 1 Business understanding | Planning, prompt chaining |
| 2 Data acquisition | Tool use, ReAct |
| 3 EDA | Parallelization (data + EDA + drift) |
| 4 Feature prep | Tool use, specialist workers |
| 5 Model training | ReAct loop, orchestrator–workers |
| 6 Evaluation | Evaluator–optimizer |
| 7 Deployment | Human-in-the-loop (`register_model`) |
| 8 Monitoring | Event-driven retrain, handoff Tier-2 |

Agents **orchestrate** the pipeline; tools call **MLflow** (or an in-memory mock) for run history, metrics, registry, and inference.

## MLflow tracking

| Mode | How |
|------|-----|
| **MLflow on** (default) | Logs params, holdout MAPE, baseline; registry staging/production |
| **Mock** | `--no-mlflow` or `USE_MLFLOW=0` — same tools, in-memory fallback |

Install ML extras:

```bash
pip install -r requirements-ml.txt
```

View runs:

```bash
mlflow ui --backend-store-uri mlruns
```

### New tools

| Tool | Purpose |
|------|---------|
| `list_recent_runs` | Browse prior trainings for a SKU-store |
| `get_best_run` | Pick best run by `holdout_mape` before retrain/deploy |
| `train_forecast_model` | Train moving-average baseline + log run |
| `evaluate_model` | Read/compare logged metrics |
| `register_model` | MLflow Model Registry (HITL in pattern 09) |
| `generate_forecast` | Inference from logged pyfunc model |

## MLDLC steps (all eight)

1. **Business understanding** — horizon, SKU, store, metric (MAPE)
2. **Data acquisition** — load `demand_daily.csv`
3. **EDA** — seasonality, promos, gaps
4. **Data preparation** — lags, rolling stats, calendar features
5. **Model development** — train + **MLflow run**
6. **Model evaluation** — holdout MAPE vs baseline (logged)
7. **Model deployment** — register to staging/production (HITL)
8. **Monitoring** — drift score, scheduled retrain events

## Synthetic data

| File | Contents |
|------|----------|
| `data/demand_daily.csv` | 1,800 rows — 5 SKUs × 3 stores × 120 days |
| `data/sku_catalog.json` | Product metadata |
| `data/pipeline_runs.json` | Batch run log (map–reduce) |
| `data/retrain_event.json` | Scheduled retrain event |
| `data/kb/*.md` | Forecasting playbook (RAG) |

Regenerate data:

```bash
python shared/examples/demand_forecast/data/generate_data.py
```

## Run

```bash
# MLflow tracking (default)
python patterns/01-react/example/main.py --scenario demand-forecast --provider openai

# In-memory mock (no MLflow)
python patterns/01-react/example/main.py --scenario demand-forecast --no-mlflow

# Tools via MCP (optional; Python 3.10+, pip install -r requirements-mcp.txt)
python patterns/01-react/example/main.py --scenario demand-forecast --use-mcp --no-mlflow

python patterns/09-human-in-the-loop/example/main.py --scenario demand-forecast --auto-approve
mlflow ui
```

## Shared code

- `shared/examples/demand_forecast/tools.py` — agent tools
- `shared/examples/demand_forecast/mlflow_tracking.py` — MLflow backend
- `shared/examples/demand_forecast/mock_tracking.py` — `--no-mlflow` backend
- `shared/examples/tool_provider.py` — local vs MCP tool loading
- [MCP architecture](../architecture/mcp.md) — `--use-mcp` for all scenarios

Compare with [IT Helpdesk](it-helpdesk.md) and [E-commerce](ecommerce-order-support.md).
