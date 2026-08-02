import os
from google import genai
from google.genai import types

client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))


# The persistent persona -set once, applies to every turn
system_instructions =""" You are a senior payments infrastructure SME assistinng with incident triage for a bank's UPI/NEFT/RTGS systems.
Always respond concisely, use technical banking terminology correctly, and if a transaction reference ID (like a UTR or RRN) is missing from the user's message, ask for it before proceeding."""

chat = client.chats.create(
    model = "gemini-2.5-flash",
    config=types.GenerateContentConfig(
        system_instruction=system_instructions
    )
)
print("Day 14:  Chat with persistent persona. Type 'quit' to exit. \n")


while True:
    user_input = input("You ")
    if user_input.lower() == "quit":
        print("Session ended.")
        break

    response = chat.send_message(user_input)
    print(f"Gemini: {response.text}\n")


# Inspect history - note the system_instruction does not show up here
# because it's not a "turn," it's a standing config pn the session itself
print("=== Full conversation history logged in this session ===")

for message in chat.get_history():
    role = message.role
    text = message.parts[0].text
    print(f"[{role.upper()}]:   {text}\n")

    