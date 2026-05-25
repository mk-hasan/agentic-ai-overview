"""Run the ReAct IT helpdesk starter (LangGraph)."""

from shared.examples.cli import bootstrap_path, chat_stream_enabled, parse_example_args

bootstrap_path()

from langchain_core.messages import HumanMessage, SystemMessage

from graph import build_graph, get_system_prompt


def main() -> None:
    args, provider, scenario, question = parse_example_args("ReAct IT helpdesk demo (LangGraph)")
    graph = build_graph(provider=provider, scenario=scenario)
    inputs = {
        "messages": [
            SystemMessage(content=get_system_prompt(scenario)),
            HumanMessage(content=question),
        ]
    }

    if chat_stream_enabled(args, scenario):
        from shared.langgraph.streaming import stream_chat_response

        stream_chat_response(
            graph,
            inputs,
            header=f"Agent response ({provider}, {scenario}, streaming)",
        )
        return

    result = graph.invoke(inputs)
    final_message = result["messages"][-1]
    print(f"\n--- Agent response ({provider}, {scenario}) ---\n")
    print(final_message.content)


if __name__ == "__main__":
    main()
