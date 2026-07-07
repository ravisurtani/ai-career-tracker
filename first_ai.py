# Dy 10 - My First AI API Cll!
# Ravi talks to Gemini AI through Python

from google import genai
import os

# My API Key 

API_KEY = os.environ.get("GEMINI_API_KEY")

# Connect to Gemini
client = genai.Client(api_key=API_KEY)

# Ask AI a question

print("Connecting to Gemini AI.....")
print("=" * 50)

question = "What is AI Engineering in simple terms?"

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=question
)


print(F"Question: {question}")
print(f"\nGemini AI Answer:")
print(response.text)
print("=" * 50)

print("Your Python code just talked to real AI!")