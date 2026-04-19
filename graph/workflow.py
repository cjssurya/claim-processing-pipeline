from langgraph.graph import StateGraph
from typing import TypedDict

from agents.segregator import segregate_pages
from agents.id_agent import extract_id_data
from agents.discharge_agent import extract_discharge_data
from agents.bill_agent import extract_bill_data


# ✅ Proper State Definition (VERY IMPORTANT)
class State(TypedDict):
    claim_id: str
    pages: list
    classification: dict
    id_data: dict
    discharge_data: dict
    bill_data: dict
    final_output: dict


# Nodes
def segregator_node(state):
    pages = state.get("pages", [])  # ✅ safe access
    classification = segregate_pages(pages)
    state["classification"] = classification
    return state


def id_node(state):
    state["id_data"] = extract_id_data(
        state.get("pages", []),
        state.get("classification", {})
    )
    return state


def discharge_node(state):
    state["discharge_data"] = extract_discharge_data(
        state.get("pages", []),
        state.get("classification", {})
    )
    return state


def bill_node(state):
    state["bill_data"] = extract_bill_data(
        state.get("pages", []),
        state.get("classification", {})
    )
    return state


def aggregator_node(state):
    state["final_output"] = {
        "claim_id": state.get("claim_id"),
        "patient": state.get("id_data"),
        "discharge_summary": state.get("discharge_data"),
        "billing": state.get("bill_data")
    }
    return state


# Build graph
def build_graph():
    graph = StateGraph(State)

    graph.add_node("segregator", segregator_node)
    graph.add_node("id_agent", id_node)
    graph.add_node("discharge_agent", discharge_node)
    graph.add_node("bill_agent", bill_node)
    graph.add_node("aggregator", aggregator_node)

    graph.set_entry_point("segregator")

    graph.add_edge("segregator", "id_agent")
    graph.add_edge("id_agent", "discharge_agent")
    graph.add_edge("discharge_agent", "bill_agent")
    graph.add_edge("bill_agent", "aggregator")

    graph.set_finish_point("aggregator")

    return graph.compile()