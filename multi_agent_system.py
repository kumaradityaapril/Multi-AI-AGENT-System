from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
from langgraph.graph import StateGraph
from typing import TypedDict
import os
from dotenv import load_dotenv

load_dotenv()

class AgentState(TypedDict):
    user_input: str
    plan: str
    topics: str
    schedule: str
    review: str

def planner_agent(state: AgentState):
    llm = ChatGroq(model="llama-3.1-8b-instant", api_key=os.environ.get("GROQ_API_KEY"))
    
    response = llm.invoke([
        HumanMessage(content=f"Understand this goal and summarize: {state['user_input']}")
    ])
    
    return {"plan": response.content}

def research_agent(state: AgentState):
    llm = ChatGroq(model="llama-3.1-8b-instant", api_key=os.environ.get("GROQ_API_KEY"))
    
    response = llm.invoke([
        HumanMessage(content=f"Break this into study topics: {state['plan']}")
    ])
    
    return {"topics": response.content}

def scheduler_agent(state: AgentState):
    llm = ChatGroq(model="llama-3.1-8b-instant", api_key=os.environ.get("GROQ_API_KEY"))
    
    response = llm.invoke([
        HumanMessage(content=f"Create a 10-day study plan using: {state['topics']}")
    ])
    
    return {"schedule": response.content}

def reviewer_agent(state: AgentState):
    llm = ChatGroq(model="llama-3.1-8b-instant", api_key=os.environ.get("GROQ_API_KEY"))
    
    response = llm.invoke([
        HumanMessage(content=f"Improve this schedule: {state['schedule']}")
    ])
    
    return {"review": response.content}

def build_graph():
    graph = StateGraph(AgentState)

    graph.add_node("planner", planner_agent)
    graph.add_node("research", research_agent)
    graph.add_node("scheduler", scheduler_agent)
    graph.add_node("reviewer", reviewer_agent)

    graph.set_entry_point("planner")

    graph.add_edge("planner", "research")
    graph.add_edge("research", "scheduler")
    graph.add_edge("scheduler", "reviewer")

    graph.set_finish_point("reviewer")

    return graph.compile()


def main():
    app = build_graph()

    user_input = input("Enter your goal: ")

    result = app.invoke({
        "user_input": user_input
    })

    print("\nFinal Output:\n")
    print(result["review"])


if __name__ == "__main__":
    main()
