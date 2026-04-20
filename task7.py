# LLM + Memory + Tool

from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
import  re

# Load model
llm = ChatOllama(model="llama3")

# memory
chat_history = []

roles = {
    "teacher": "Explain concepts simply under 50 words.",
    "interviewer": "Act as a strict technical interviewer. Be precise and critical.",
    "friend": "Explain casually like a friendly conversation."
}

# Tool : calculator
def calculate(user_input: str):
    numbers = re.findall(r'\d+', user_input)

    if len(numbers) < 2:
        return None
    a, b = map(int, numbers)

    if "+" in user_input:
        return a+b
    elif "-" in user_input:
        return a-b
    elif "*" in user_input:
        return a*b
    elif "/" in user_input:
        return a/b
    return None

# Main function

def generate_response(user_input: str, role:str) -> str:
    global chat_history
    # step1: check tool
    result = calculate(user_input)
    if result is not None:
        return f"The answer is {result}"
    # step2: LLM flow
    system_prompt = roles.get(role, roles["teacher"])
    messages =[
    SystemMessage(content=system_prompt),
    *chat_history,
    HumanMessage(content=user_input)
    ]

    response = llm.invoke(messages)

    # mwmory updated
    chat_history.append(HumanMessage(content=user_input))
    chat_history.append(AIMessage(content=response.content))

    # Limit memory(last 4 messages)
    chat_history = chat_history[-4:]
    return response.content

while True:
    user_query = input("You: ")
    if user_query.lower()=="exit":
        break
    if user_query.lower() == "clear":
        chat_history.clear()
        print("Memory cleared")
        continue
    reply = generate_response(user_query, "teacher")
    print("AI: ",reply)