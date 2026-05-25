"""Planning — decompose helpdesk request into steps then execute."""

from shared.examples.cli import bootstrap_path, parse_example_args

bootstrap_path()

from graph import build_graph


def main() -> None:
    _, provider, scenario, question = parse_example_args("Planning IT helpdesk demo")
    graph = build_graph(provider=provider, scenario=scenario)
    result = graph.invoke({"messages": [], "plan": [], "step_index": 0, "user_request": question})
    print(f"\n--- Final response ({provider}, {scenario}) ---\n")
    print(result["messages"][-1].content)


if __name__ == "__main__":
    main()
