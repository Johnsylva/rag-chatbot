from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
llm = OpenAI()

#Load the entire documentation into memory
with open("cocktails.md", "r", encoding="utf-8") as file:
    documentation = file.read()

assistant_message = "How can I help you today?"
print(f"Assistant: {assistant_message}\n")
user_input = input("User: ")

history = [
    {"role": "developer", "content": f"""You ara an AI user guide support who is knowlegdeable about classic cocktail. You will provide information on how to make various cocktails; ingredients, instructions, tips and history of the cocktail. You are to answer user queries below solely on the following documentation: {documentation} """},
    {"role": "assistant", "content": assistant_message}, 
    {"role": "user", "content": user_input},
]

while user_input != "exit":
    response = llm.responses.create(
        model= "gpt-4.1",
        temperature =0,
        input = history
    )
    print(f"\nAssistant: {response.output_text}")

    user_input = input("\nUser: ")

    history += [
        {"role": "assistant", "content": response.output_text},
        {"role":"user", "content": user_input}
    ]

print(history)