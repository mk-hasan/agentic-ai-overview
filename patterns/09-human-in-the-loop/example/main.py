"""Human-in-the-Loop — approve tickets before creation."""

from shared.examples.cli import bootstrap_path, build_example_parser, resolve_scenario
from shared.examples.scenarios import get_scenario
from shared.utils.cli import resolve_provider

bootstrap_path()

from langchain_core.messages import HumanMessage, SystemMessage
from langgraph.types import Command

from graph import build_graph


def main() -> None:
    parser = build_example_parser("HITL IT helpdesk demo")
    parser.add_argument("--auto-approve", action="store_true", help="Skip interactive prompt")
    parser.add_argument(
        "--time-travel",
        action="store_true",
        help="After interrupt, rewind checkpoint and patch ticket before approval",
    )
    parser.add_argument(
        "--memory-checkpointer",
        action="store_true",
        help="Use in-memory checkpointer instead of SQLite (for tests)",
    )
    args = parser.parse_args()
    from shared.examples.cli import apply_mlflow_cli, apply_mcp_cli

    apply_mlflow_cli(args)
    apply_mcp_cli(args)

    provider = resolve_provider(args.provider)
    scenario = resolve_scenario(args.scenario)
    sc = get_scenario(scenario)
    question = " ".join(args.question) if args.question else sc.default_question

    graph = build_graph(
        provider=provider,
        scenario=scenario,
        sqlite=not args.memory_checkpointer,
    )
    config = {"configurable": {"thread_id": "hitl-demo-1"}}
    initial = {
        "messages": [
            SystemMessage(content=sc.tier1_prompt),
            HumanMessage(content=question),
        ],
        "pending_ticket": {},
    }

    graph.invoke(initial, config=config)

    while graph.get_state(config).next:
        snap = graph.get_state(config)
        payload = {}
        if snap.tasks and snap.tasks[0].interrupts:
            payload = snap.tasks[0].interrupts[0].value
        print("\n--- Human approval required ---")
        print(payload)

        if args.time_travel:
            from shared.langgraph.time_travel import print_checkpoint_history, replay_hitl_with_ticket_patch

            print_checkpoint_history(graph, config)
            patch = {"priority": "low"} if scenario == "helpdesk" else {}
            if patch:
                config = replay_hitl_with_ticket_patch(graph, config, patch)
                print(f"Time travel: patched pending ticket with {patch}")

        if args.auto_approve:
            decision = "approved"
            print("(auto-approve enabled)")
        else:
            choice = input("Approve ticket? [y/N]: ").strip().lower()
            decision = "approved" if choice in ("y", "yes") else "rejected"
        graph.invoke(Command(resume=decision), config=config)

    final = graph.get_state(config).values
    print(f"\n--- Final outcome ({provider}, {scenario}) ---\n")
    print(final["messages"][-1].content)


if __name__ == "__main__":
    main()
