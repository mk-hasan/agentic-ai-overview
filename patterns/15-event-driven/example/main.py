"""Event-Driven — react to inbound support email."""

from shared.examples.cli import bootstrap_path, parse_example_args

bootstrap_path()

from graph import build_graph


def main() -> None:
    args, provider, scenario, _ = parse_example_args("Event-driven IT helpdesk demo")
    graph = build_graph(provider=provider, scenario=scenario)
    inputs = {"event": {}, "user_request": "", "messages": [], "response": ""}

    if getattr(args, "stream_events", False) or scenario == "demand-forecast":
        from shared.langgraph.streaming import stream_graph_events

        result = stream_graph_events(
            graph,
            inputs,
            header=f"Event pipeline ({provider}, {scenario})",
            interest_keys=["ingest", "handle", "prepare", "agent", "finalize"],
        )
    else:
        result = graph.invoke(inputs)

    print(f"\n--- Event processed ({provider}, {scenario}) ---")
    print("From:", result["event"]["from"])
    print("Subject:", result["event"]["subject"])
    print(f"\n--- Agent response ---\n{result['response']}")


if __name__ == "__main__":
    main()
