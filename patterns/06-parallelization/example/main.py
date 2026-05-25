"""Parallelization — concurrent FAQ + status checks."""

from shared.examples.cli import bootstrap_path, parse_example_args

bootstrap_path()

from graph import build_graph


def main() -> None:
    _, provider, scenario, question = parse_example_args("Parallelization IT helpdesk demo")
    graph = build_graph(provider=provider, scenario=scenario)
    result = graph.invoke({"user_request": question})
    parallel = result["parallel_results"]
    print(f"\n--- Parallel findings ({provider}, {scenario}) ---")
    for key, value in parallel.items():
        preview = value if len(value) <= 120 else value[:120] + "..."
        print(f"{key}: {preview}")
    print(f"\n--- Merged reply ---\n{result['final_response']}")


if __name__ == "__main__":
    main()
