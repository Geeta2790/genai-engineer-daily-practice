# day03 langgraph workflow

## Goal
Create a small StateGraph with typed state, two nodes and edges. Print the final state and explain node execution order.

## Your checklist
- [x] Understand the concept
- [x] Write the implementation yourself
- [x] Run the code locally
- [x] Test a success case and an error case
- [x] Commit your work with a meaningful message

## Learning notes
- A `StateGraph` has three pieces: a typed **state** (`TypedDict`), **nodes** (functions that receive state and return a partial update dict), and **edges** that define execution order.
- A node returns only the fields it wants to change — LangGraph merges the partial dict back into the full state. You don't rewrite the whole state object.
- `START` and `END` are built-in sentinels. Every graph needs an edge from `START` and at least one path to `END`.
- Call `.compile()` before `.invoke()` — compiling validates the graph (no dangling nodes, every node reachable).
- Execution order here: `START → process → generate → END`. The final state has both `question` (trimmed by node 1) and `answer` (filled by node 2).
- Conditional edges (see `conditional_graph.py`) let you branch based on state — a router function returns the name of the next node.
