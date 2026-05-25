"""Evaluator–Optimizer — improve helpdesk draft quality."""

from shared.examples.cli import bootstrap_path, parse_example_args

bootstrap_path()

from graph import build_graph


def main() -> None:
    _, provider, scenario, question = parse_example_args("Evaluator–Optimizer IT helpdesk demo")
    graph = build_graph(provider=provider, scenario=scenario)
    result = graph.invoke({"user_request": question, "round": 0, "score": 0, "feedback": ""})
    print(f"\n--- Optimized reply ({provider}, {scenario}) ---")
    print(f"Rounds: {result['round']} | Score: {result['score']}")
    print(f"\n{result['final_response']}")


if __name__ == "__main__":
    main()
