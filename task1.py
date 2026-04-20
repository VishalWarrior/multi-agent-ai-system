from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage

llm = ChatOllama(model="llama3")



def generate_response(user_input: str) -> str:
    messages = [
        SystemMessage(content="You are a strict technical interviewer"), 
        HumanMessage(content=user_input)
    ]
    response = llm.invoke(messages)



    return response.content

user_input = input("Enter Your Query : ")
print(generate_response(user_input))