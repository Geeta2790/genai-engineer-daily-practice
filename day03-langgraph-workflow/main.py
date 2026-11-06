
from typing import TypedDict
from langgraph.graph import StateGraph, START, END

# Step 1: Define shared state
class AgentState(TypedDict):
    question: str
    answer: str


# Step 2: Create first node
def process_question(state: AgentState):
    print("Node 1: Processing question")

    return {
        "question": state["question"].strip()
    }


# Step 3: Create second node
def generate_answer(state: AgentState):
    print("Node 2: Generating answer")

    return {
        "answer": f"You asked: {state['question']}"
    }


# Step 4: Build graph
workflow = StateGraph(AgentState)

workflow.add_node("process", process_question)
workflow.add_node("generate", generate_answer)

workflow.add_edge(START, "process")
workflow.add_edge("process", "generate")
workflow.add_edge("generate", END)

# Step 5: Compile graph
app = workflow.compile()

# Step 6: Run graph
result = app.invoke({
    "question": "What is RAG?",
    "answer": ""
})

print(result)
