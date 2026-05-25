"""Prompt chaining — linear pipeline for helpdesk replies."""

from shared.examples.cli import bootstrap_path, parse_example_args

bootstrap_path()

from graph import build_graph


def main() -> None:
    _, provider, scenario, question = parse_example_args("Prompt chaining IT helpdesk demo")
    graph = build_graph(provider=provider, scenario=scenario)
    result = graph.invoke({"user_request": question})
    print(f"\n--- Pipeline stages ({provider}, {scenario}) ---")
    print(f"Extracted: {result['extracted_issue']}")
    print(f"Category:  {result['category']}")
    print(f"\n--- Final reply ---\n{result['final_response']}")


if __name__ == "__main__":
    main()
