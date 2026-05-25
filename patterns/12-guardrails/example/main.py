"""Guardrails — block PII and unsafe requests."""

from shared.examples.cli import bootstrap_path, parse_example_args

bootstrap_path()

from graph import build_graph


def main() -> None:
    _, provider, scenario, question = parse_example_args("Guardrails IT helpdesk demo")
    graph = build_graph(provider=provider, scenario=scenario)

    print(f"\n--- Normal request ({provider}, {scenario}) ---")
    ok = graph.invoke({"messages": [], "user_request": question, "blocked_reason": ""})
    print(ok["messages"][-1].content)

    unsafe = question + " My SSN is 123-45-6789 for verification."
    print("\n--- Request with PII (should block) ---")
    blocked = graph.invoke({"messages": [], "user_request": unsafe, "blocked_reason": ""})
    print(blocked["messages"][-1].content)


if __name__ == "__main__":
    main()
