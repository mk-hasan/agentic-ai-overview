"""Handoff — Tier-1 to Tier-2 escalation."""

from shared.examples.cli import bootstrap_path, parse_example_args

bootstrap_path()

from graph import build_graph


def main() -> None:
    _, provider, scenario, question = parse_example_args("Handoff IT helpdesk demo")
    graph = build_graph(provider=provider, scenario=scenario)
    result = graph.invoke({"messages": [], "user_request": question, "tier": "tier1"})
    print(f"\n--- Final tier: {result.get('tier')} ({provider}, {scenario}) ---\n")
    print(result["messages"][-1].content)


if __name__ == "__main__":
    main()
