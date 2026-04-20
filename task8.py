# Multi AI Agents 

# 1. BAse setup

from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage

llm = ChatOllama(model="llama3")

# 2. Planner agent

# Job : planner agent job is to break the task

def planner(user_input):
    messages = [
        SystemMessage(content="You are a planner, Break the task into steps."),
        HumanMessage(content=user_input)
    ]
    return llm.invoke(messages).content

# Reseracher Agent

def researcher(plan):
    messages = [
        SystemMessage(content="You are a researcher . provide detailed info."),
        HumanMessage(content=plan)

    ]
    return llm.invoke(messages).content

# Writer Agent
def writer(research):
    messages = [
        SystemMessage(content="You are a writer. Create  final structured answer."),
        HumanMessage(content=research)
    ]
    return llm.invoke(messages).content


#Orchestration(flow of agents) most important

def multi_agent_system(user_input):
    plan = planner(user_input)
    research = researcher(plan)
    final_output = writer(research)
    return final_output   


# Run

query = input("Enter query: ")
print(multi_agent_system(query))