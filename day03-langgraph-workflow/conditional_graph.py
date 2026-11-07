
from typing import TypedDict
from langgraph.graph import StateGraph, START, END

class HRState(TypedDict):
    question: str
    answer: str

def route_question(state: HRState):
    question = state["question"].lower()
    if "leave" in question:
        return "leave"
    return "salary"

def leave_node(state: HRState):
    return {"answer": "You have 20 annual leaves."}

def salary_node(state: HRState):
    return {"answer": "Contact payroll for salary details."}

graph = StateGraph(HRState)

graph.add_node("leave", leave_node)
graph.add_node("salary", salary_node)

graph.add_conditional_edges(
    START,
    route_question,
    {
        "leave": "leave",
        "salary": "salary"
    }
)

graph.add_edge("leave", END)
graph.add_edge("salary", END)

app = graph.compile()

result = app.invoke({
    "question": "What is my leave balance?",
    "answer": ""
})

print(result["answer"])
