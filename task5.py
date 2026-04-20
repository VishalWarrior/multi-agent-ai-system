from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

llm = ChatOllama(model="llama3")
chat_history = []

roles = {
    "teacher": "Explain concepts simply under 50 words",
    "interviewer": "Act as a strict technical interviewer. Be precise and critical.",
    "friend": "Explain casually like a friendly conversation."
}

def generate_response(user_input: str, role: str) -> str:
    system_prompt = roles.get(role, roles["teacher"])

    messages = [
        SystemMessage(content=system_prompt),
        *chat_history,
        HumanMessage(content=user_input),
        
    ]

    response = llm.invoke(messages)

    chat_history.append(HumanMessage(content=user_input))
    chat_history.append(AIMessage(content=response.content))
    print(chat_history)
    return response.content

while True:
    user_query = input("Enter your query: ")
    if user_query.lower()=="exit":
        break
    reply = (generate_response(user_query, "teacher"))
    print("AI: ",reply)