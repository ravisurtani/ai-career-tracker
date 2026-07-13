from google import genai
from google.genai import types
import os
import json

API_KEY = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=API_KEY)


def ask_gemini(question, system_prompt=None, temperature=0.7, json_schema=None):
    config_params = {"temperature": temperature}
    if system_prompt:
        config_params["system_instruction"] = system_prompt
    if json_schema:
        config_params["response_mime_type"] = "application/json"
        config_params["response_schema"] = json_schema

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=question,
        config=types.GenerateContentConfig(**config_params)
    )
    return response.text

print(ask_gemini("Say hello in one sentence."))


print("\n ---  Support Agent Style --- ")
print(ask_gemini(
    question="Why did this payment failed",
    system_prompt="You are a Tier-1 Payment support agent. Never expose internal error codes. Keep it simple and end with next steps.",
    temperature=0.4
))

print("\n ---- Backend Engineer Style ---- ")
print(ask_gemini(
    question="Why this payment failed",
    system_prompt="You are a backend Payments Engineer debugging NPCI switch logs. Be technical and precise",
    temperature=0.4
))


print("\n -- Structured Incident Trige --- ")

incident_schema = {
    "type": "OBJECT",
    "properties": {
        "severity": {"type": "STRING", "enum": ["SEV1", "SEV2", "SEV3", "SEV4"]},
        "impact_summary": {"type": "STRING"},
        "affected_percentage": {"type": "NUMBER"},
        "recommended_next_steps": {"type": "STRING"},
    },
    "required": ["severity", "impact_summary", "affected_percentage", "recommended_next_steps"],
}

incidents = [
    "UPI transactions failing intermittently since 2:15 PM, affecting roughly 12% of traffic.",
    "Single customer complain about a delay NEFT credit, no other reports",
    "Core banking database showing high latency, response times up 400% in the last 10 minutes.",
]

for desc in incidents:
    result = ask_gemini(
        question=f"Analyize this incident: {desc}",
        temperature=0.2,
        json_schema=incident_schema
    )

    data = json.loads(result)
    print(f"\n [{data['severity']}] {desc}")
    print(f" Impact: {data['affected_percentage']}% affected")
    print(f" Next Step: {data[  'recommended_next_steps']}")

