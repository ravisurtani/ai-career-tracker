## """ Day 13 - Multi -turn Chat and Conversation History
   # Phase 3, Day 1

    #Goal: Insted of one-off generate_content() calls (Day 10-12 style),
   # use a 'chat' session object that remembers earlier turns automticlly.


import os
from google import genai


# Step 1: Load the API key from my windws environment variables
# (Same as Day 10-12 - no change here)
api_key = os.environ.get("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found. Set it in your environment varibles first.")
            
# Step 2 : Create the client (same as before)
client = genai.Client(api_key=api_key)

# Step 3: THE NEW PART - Create a chat session instead of calling generate_content directly
# Think of this as "Opening the incident bridge call" - one persistent thread.
chat = client.chats.create(model="gemini-2.5-flash")

print("==== Day 13 : Multi-turn Cht Demo ====")
print("Type 'quit' to end the session.\n")

# Step 4: Loop - keep sending messages into the same chat object
while True:
    user_input = input("You: ")

    if user_input.lower() in ("quit", "exit"):
        print(" Session ended.")
        break


    # This is the key line: chat.send_message() instead of client.models.generate_content()
    response = chat.send_message(user_input)

    print(f"Gemini: {response.text}\n")


## Step 5: After the loop ends, print the full history to PROVE it remembered everything
print("\n=== Full conversation history loggedin this session ===")
for message in chat.get_history():
    role = message.role
    text = message.parts[0].text
    print(f"[{role.upper()}]: {text}")




