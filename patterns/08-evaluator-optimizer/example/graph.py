"""Evaluator–Optimizer — draft, evaluate, revise until quality passes."""

from typing import TypedDict

from langchain_core.messages import HumanMessage, SystemMessage
from langgraph.graph import END, START, StateGraph

from shared.examples.scenarios import get_scenario
from shared.examples.tool_provider import get_core_tools, get_extended_tools, get_tool_catalog, get_tools_by_name, get_tool_by_name
from shared.utils.llm import get_chat_model

MAX_ROUNDS = 3


class EvalState(TypedDict):
    user_request: str
    draft: str
    feedback: str
    score: int
    round: int
    final_response: str


def build_graph(*, provider: str = "openai", scenario: str = "helpdesk"):
    s = get_scenario(scenario)
    model = get_chat_model(provider=provider)

    def generate(state: EvalState):
        round_no = state.get("round", 0) + 1
        prompt = [
            SystemMessage(content=s.base_system_prompt + "\nDraft a helpdesk reply."),
            HumanMessage(content=state["user_request"]),
        ]
        if state.get("feedback"):
            prompt.append(HumanMessage(content=f"Revise using feedback:\n{state['feedback']}"))
        r = model.invoke(prompt)
        return {"draft": r.content.strip(), "round": round_no}

    def evaluate(state: EvalState):
        r = model.invoke(
            [
                SystemMessage(
                    content=(
                        "Score the draft 1-10 for clarity, actionable steps, and professionalism. "
                        "Reply as JSON: {\"score\": N, \"feedback\": \"...\"}"
                    )
                ),
                HumanMessage(content=state["draft"]),
            ]
        )
        text = r.content
        score = 7
        feedback = text
        if "\"score\"" in text:
            try:
                import json

                data = json.loads(text[text.find("{") : text.rfind("}") + 1])
                score = int(data.get("score", 7))
                feedback = data.get("feedback", text)
            except (ValueError, json.JSONDecodeError):
                pass
        return {"score": score, "feedback": feedback}

    def finalize(state: EvalState):
        return {"final_response": state["draft"]}

    def route_after_eval(state: EvalState):
        if state["score"] >= 8 or state["round"] >= MAX_ROUNDS:
            return "finalize"
        return "generate"

    graph = StateGraph(EvalState)
    graph.add_node("generate", generate)
    graph.add_node("evaluate", evaluate)
    graph.add_node("finalize", finalize)
    graph.add_edge(START, "generate")
    graph.add_edge("generate", "evaluate")
    graph.add_conditional_edges("evaluate", route_after_eval, {"generate": "generate", "finalize": "finalize"})
    graph.add_edge("finalize", END)
    return graph.compile()
