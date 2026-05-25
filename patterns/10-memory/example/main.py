"""Memory — multi-turn IT helpdesk conversation."""

from shared.examples.cli import bootstrap_path, parse_example_args
from shared.examples.scenarios import get_scenario

bootstrap_path()

from langchain_core.messages import HumanMessage, SystemMessage

from graph import build_graph, get_system_prompt


def main() -> None:
    _, provider, scenario, question = parse_example_args("Memory IT helpdesk demo")
    graph = build_graph(provider=provider, scenario=scenario)
    config = {"configurable": {"thread_id": "helpdesk-memory-1"}}
    system = SystemMessage(content=get_system_prompt(scenario))

    print(f"\n--- Turn 1 ({provider}, {scenario}) ---")
    r1 = graph.invoke({"messages": [system, HumanMessage(content=question)]}, config=config)
    print(r1["messages"][-1].content)

    follow_up = get_scenario(scenario).follow_up_question
    print(f"\n--- Turn 2 (follow-up, same thread) ---")
    r2 = graph.invoke({"messages": [HumanMessage(content=follow_up)]}, config=config)
    print(r2["messages"][-1].content)


if __name__ == "__main__":
    main()
