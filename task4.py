from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage

llm = ChatOllama(model="llama3")

roles = {
    "teacher": "Explain concepts simply and clearly with examples.",
    "interviewer": "Act as a strict technical interviewer. Be precise and critical.",
    "friend": "Explain casually like a friendly conversation."
}

def generate_response(user_input: str, role: str) -> str:
    system_prompt = roles.get(role, roles["teacher"])

    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=user_input)
    ]

    response = llm.invoke(messages)
    return response.content


user_query = input("Enter your query: ")

print(generate_response(user_query, "teacher"))
print(generate_response(user_query, "interviewer"))
print(generate_response(user_query, "friend"))