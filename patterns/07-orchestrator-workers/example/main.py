"""Orchestrator–Workers — multi-specialist helpdesk team."""

from shared.examples.cli import bootstrap_path, parse_example_args

bootstrap_path()

from graph import build_graph


def main() -> None:
    args, provider, scenario, question = parse_example_args("Orchestrator–Workers IT helpdesk demo")
    graph = build_graph(provider=provider, scenario=scenario)
    inputs = {
        "messages": [],
        "user_request": question,
        "next_worker": "vpn",
        "done": False,
        "rounds": 0,
    }

    if getattr(args, "stream_events", False) or scenario == "demand-forecast":
        from shared.examples.scenarios import get_scenario
        from shared.langgraph.streaming import stream_graph_events

        workers = list(get_scenario(scenario).orchestrator_workers)
        result = stream_graph_events(
            graph,
            inputs,
            header=f"Pipeline events ({provider}, {scenario})",
            interest_keys=["supervisor"] + workers,
        )
    else:
        result = graph.invoke(inputs)

    print(f"\n--- Orchestrated response ({provider}, {scenario}) ---\n")
    print(result["messages"][-1].content if result.get("messages") else "Case closed.")


if __name__ == "__main__":
    main()
