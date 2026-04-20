from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

llm = ChatOllama(model="llama3")

# ✅ Memory
chat_history = []

# ✅ Debug logger
def log(step, message=""):
    print(f"\n🔍 [{step}] {message}")


# ---------------- AGENTS ---------------- #

def planner(user_input):
    log("PLANNER", "Creating plan...")
    messages = [
        SystemMessage(content="Break the task into steps."),
        *chat_history,
        HumanMessage(content=user_input)
    ]
    result = llm.invoke(messages).content
    log("PLANNER OUTPUT", result)
    return result


def researcher(plan):
    log("RESEARCHER", "Processing plan...")
    messages = [
        SystemMessage(content="Provide detailed information."),
        HumanMessage(content=plan)
    ]
    result = llm.invoke(messages).content
    log("RESEARCHER OUTPUT", result)
    return result


def writer(research):
    log("WRITER", "Generating final answer...")
    messages = [
        SystemMessage(content="Write a structured final answer."),
        HumanMessage(content=research)
    ]
    result = llm.invoke(messages).content
    log("WRITER OUTPUT", result)
    return result


def validator(answer):
    log("VALIDATOR", "Checking quality...")
    messages = [
        SystemMessage(content="Reply only GOOD or BAD."),
        HumanMessage(content=answer)
    ]
    result = llm.invoke(messages).content
    log("VALIDATOR OUTPUT", result)
    return result


# ---------------- MAIN SYSTEM ---------------- #

def system(user_input):
    global chat_history

    log("USER INPUT", user_input)

    # Multi-agent pipeline
    plan = planner(user_input)
    research = researcher(plan)

    attempt = 0
    max_attempts = 2

    while attempt < max_attempts:
        draft = writer(research)
        validation = validator(draft)

        if "GOOD" in validation.upper():
            log("VALIDATION", "Accepted ✅")
            break

        log("VALIDATION", "Retrying ❌")
        attempt += 1

    # ✅ Memory update
    chat_history.append(HumanMessage(content=user_input))
    chat_history.append(AIMessage(content=draft))

    # ✅ Limit memory
    chat_history = chat_history[-4:]

    return draft


# ---------------- RUN LOOP ---------------- #

while True:
    query = input("\nYou: ")

    if query.lower() == "exit":
        break

    if query.lower() == "clear":
        chat_history.clear()
        print("Memory cleared ✅")
        continue

    print("\nAI:", system(query))