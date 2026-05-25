"""Routing — dispatch helpdesk requests by intent."""

from shared.examples.cli import bootstrap_path, parse_example_args

bootstrap_path()

from graph import build_graph


def main() -> None:
    _, provider, scenario, question = parse_example_args("Routing IT helpdesk demo")
    graph = build_graph(provider=provider, scenario=scenario)
    result = graph.invoke({"user_request": question})
    print(f"\n--- Routed to: {result['route']} ({provider}, {scenario}) ---\n")
    print(result["response"])


if __name__ == "__main__":
    main()
