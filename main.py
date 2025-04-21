from langgraph.graph import StateGraph, END
from agents.researcher import search_web
from agents.writer import draft_answer

# Research Node
def research_node(state):
    print("🔍 Researching with Tavily...")
    # Calling the search function and store the result in state
    research = search_web(state["query"])
    # Ensuring research results are added to the state
    state["research"] = research
    return state  # Returning the updated state

# Answer Node
def answer_node(state):
    print("DEBUG: State contents:", state)
    print("🧠 Drafting answer with Gemini...")
    # Ensuring both query and research are available in the state
    answer = draft_answer(state["query"], state["research"])
    state["answer"] = answer  # Adding the answer to the state
    return state  # Returning the updated state with the answer

# Building the graph
builder = StateGraph(dict)  

builder.add_node("research", research_node)
builder.add_node("draft", answer_node)

builder.set_entry_point("research")
builder.add_edge("research", "draft")
builder.add_edge("draft", END)

graph = builder.compile()


if __name__ == "__main__":
    print("🤖 Deep Research AI Agent\n")
    query = input("📝 Enter your research question: ")

    # Initializing the state with the user's query
    initial_state = {"query": query}

    # Runing the graph with the initial state
    result = graph.invoke(initial_state)

    print("\n FINAL ANSWER:\n")
    print(result["answer"])

    # Save to file
    with open("answer.txt", "w", encoding="utf-8") as f:
        f.write(result["answer"])
