from langchain_ollama import ChatOllama

# ✅ Load local LLM (Ollama)
llm = ChatOllama(model="llama3")

# ✅ Simple call
# response = llm.invoke("Explain AI in one sentence")
response = llm.invoke("Write python code to check number is Armstrong")

# ✅ Print output
print(response.content)