from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage

llm = ChatOllama(model="llama3")



def generate_response(user_input: str, role: str) -> str:
    if role=="teacher":
        messages = [
        SystemMessage(content="You are a very good professional teacher who explain any topics or problems solution in simple way"),
        HumanMessage(content=user_input)
        ]
    elif role=="interviewer":
        messages = [
        SystemMessage(content="You are a strict technical interviewer"), 
        HumanMessage(content=user_input)
    ]
    elif role =="friend":
        messages = [
        SystemMessage(content="You are a good friend who explain topic or user query in casual friendly tone"),
        HumanMessage(content=user_input)
    ]
    else:
        pass
    response = llm.invoke(messages)

    return response.content


user_query = input("Enter your query :")

print(generate_response("What is AI?", "teacher"))
print("teacher end"*5)

print(generate_response("What is AI?", "interviewer"))
print("innterview end"*5)
print(generate_response("What is AI?", "friend"))

     