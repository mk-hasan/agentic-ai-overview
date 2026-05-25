"""Tool Use — IT helpdesk with explicit function-calling tools."""

from shared.examples.cli import bootstrap_path, chat_stream_enabled, parse_example_args
from shared.examples.scenarios import get_scenario

bootstrap_path()

from langchain_core.messages import HumanMessage, SystemMessage

from graph import build_graph, get_tool_catalog


def main() -> None:
    args, provider, scenario, question = parse_example_args("Tool Use IT helpdesk demo")
    graph, tools = build_graph(provider=provider, scenario=scenario)
    sc = get_scenario(scenario)

    print(f"\n--- Tool catalog ({len(tools)} tools, {provider}, {scenario}) ---")
    for tool in tools:
        desc = get_tool_catalog(scenario).get(tool.name, tool.description)
        print(f"- {tool.name}: {desc}")

    system = sc.base_system_prompt + """

You must use tools for facts (FAQ, status, tickets). Call the smallest set of tools needed."""

    inputs = {
        "messages": [
            SystemMessage(content=system),
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
    print(f"\n--- Agent response ({provider}, {scenario}) ---\n")
    print(result["messages"][-1].content)


if __name__ == "__main__":
    main()
