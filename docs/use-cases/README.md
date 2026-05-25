# Use Cases

Runnable examples support three scenarios via `--scenario`:

| Scenario | Folder | Description |
|----------|--------|-------------|
| **helpdesk** | [`shared/examples/helpdesk/`](../shared/examples/helpdesk/) | Corp IT support |
| **ecommerce** | [`shared/examples/ecommerce/`](../shared/examples/ecommerce/) | Order tracking & returns |
| **demand-forecast** | [`shared/examples/demand_forecast/`](../shared/examples/demand_forecast/) | ML pipeline for demand forecasting (MLDLC) |

## Docs

- [IT Helpdesk](it-helpdesk.md)
- [E-commerce Order Support](ecommerce-order-support.md)
- [Demand Forecast ML Pipeline](demand-forecast.md)
- [Run all examples](run-all-examples.md)

## Layout

```
shared/examples/
├── helpdesk/
├── ecommerce/
├── demand_forecast/   # Python module (CLI: demand-forecast)
├── scenarios.py
└── cli.py

patterns/01-react/example/
├── main.py
├── helpdesk/main.py
├── ecommerce/main.py
└── demand-forecast/main.py
```
