> [English](../use-cases/README.md) | **বাংলা**

# Use Cases

Runnable উদাহরণ `--scenario` দিয়ে তিনটি সিনারিও সমর্থন করে:

| সিনারিও | ফোল্ডার | বর্ণনা |
|---------|---------|--------|
| **helpdesk** | [`shared/examples/helpdesk/`](../../shared/examples/helpdesk/) | কর্প IT সাপোর্ট |
| **ecommerce** | [`shared/examples/ecommerce/`](../../shared/examples/ecommerce/) | অর্ডার ট্র্যাকিং ও রিটার্ন |
| **demand-forecast** | [`shared/examples/demand_forecast/`](../../shared/examples/demand_forecast/) | চাহিদা পূর্বাভাস ML পাইপলাইন (MLDLC) |

## ডক

- [IT Helpdesk](it-helpdesk.md)
- [E-commerce Order Support](ecommerce-order-support.md)
- [Demand Forecast ML Pipeline](demand-forecast.md)
- [সব উদাহরণ চালান](run-all-examples.md)

## কাঠামো

```
shared/examples/
├── helpdesk/
├── ecommerce/
├── demand_forecast/
├── scenarios.py
└── cli.py

patterns/01-react/example/
├── main.py
├── helpdesk/main.py
├── ecommerce/main.py
└── demand-forecast/main.py
```
