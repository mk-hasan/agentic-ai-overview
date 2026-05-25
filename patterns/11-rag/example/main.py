"""RAG — grounded helpdesk answers from markdown KB."""

from shared.examples.cli import bootstrap_path, parse_example_args

bootstrap_path()

from graph import build_graph


def main() -> None:
    _, provider, scenario, question = parse_example_args("RAG IT helpdesk demo")
    graph = build_graph(provider=provider, scenario=scenario)
    result = graph.invoke({"messages": [], "user_request": question, "context": ""})
    print(f"\n--- Retrieved context ({provider}, {scenario}) ---\n")
    print(result["context"][:500], "...\n")
    print(f"--- Agent response ---\n{result['messages'][-1].content}")


if __name__ == "__main__":
    main()
