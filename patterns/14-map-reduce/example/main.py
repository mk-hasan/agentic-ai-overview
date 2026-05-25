"""Map–Reduce — batch incident log report."""

from shared.examples.cli import bootstrap_path, parse_example_args

bootstrap_path()

from graph import build_graph


def main() -> None:
    _, provider, scenario, _ = parse_example_args("Map–Reduce incident report demo")
    graph = build_graph(provider=provider, scenario=scenario)
    result = graph.invoke({"incidents": [], "partial_summaries": [], "final_report": ""})
    print(f"\n--- Partial summaries ({provider}, {scenario}) ---")
    for line in result["partial_summaries"]:
        print("-", line[:100], "...")
    print(f"\n--- Executive report ---\n{result['final_report']}")


if __name__ == "__main__":
    main()
