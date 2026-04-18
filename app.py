print("Agent started...")

from langchain_openai import ChatOpenAI

# AI model
llm = ChatOpenAI()

# Calculator tool
def calculator_tool(query):
    try:
        return str(eval(query))
    except:
        return "Invalid math"

# Agent loop
while True:
    user_input = input("\nAsk something (type 'exit' to stop): ")

    if user_input.lower() == "exit":
        break

    # Check if math
    if any(char.isdigit() for char in user_input):
        print("Using calculator...")
        result = calculator_tool(user_input)
        print("Answer:", result)
    else:
        print("Using AI...")
        response = llm.invoke(user_input)
        print("Answer:", response.content)