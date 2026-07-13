from  google import genai
from google.genai import types
import os

client = genai.Client(api_key=os.environ["Gemini_API_KEY"])


# Step 1: Define your "runbooks" as fucntion declartions
create_ticket_func = {
    "name": "create_incident_ticket",
    "description": "Creates an incident in th tracking system when a service disruption is reported.",
    "parameters": {
        "type" : "object",
        "properties": {

            "severity": {
                "type": "string",
                "enum": ["P1", "P2", "P3", "P4"],
                "description": "Incident severity level, P1 is most critical"
            },
            "affected_service": {
                "type": "string",
                "description": " Nme of the service or system or system affected"
            },
            "summary": {
                "type" : "string",
                "description": "One-line summary of the incident"
            }
        },
        "required": ["severity", "affected_service", "summary"]
    }
}

check_status_func = {
    "name": "check_service_status",
    "description" : " Check the current health/status of a given service.",
    "parameters" : {
        "type" : "object",
        "properties": {
            "service_name": {"type": "string"}
        },
        "required": ["service_name"]
    }
}
                     

tools = types.Tool(function_declarations=[create_ticket_func, check_status_func])
config = types.GenerateContentConfig(tools=[tools])

def ask_with_tools(prompt: str):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
        config=config
    )

    #Check if Gemini wants to call a function
    part = response.candidates[0].content.parts[0]
    if part.function_call:
        fc = part.function_call
        print(f" Gemini wamts to call: {fc.name}")
        print(f" Arguments: {dict(fc.args)}")
    else:
        print(" Gemini responded with text (no function call):")
        print(response.text)


# text cases
print(" ------ Test 1: Clear incident ---- ")
ask_with_tools (
    "UPI payment gateway is down for all customers, transactions failing since 10 minutes. Please log this."
)

print(" ---- Test 2: Status check --- ")
ask_with_tools(
    "is the core banking service currently healthy?"
)

print("\n ---- Test 3: Plain question, no action needed ---")
ask_with_tools(
    "What does P1 severity mean?"
)

def create_incident_ticket(severity, affected_service, summary):
    ticket_id = "INC" + str(hash(summary) % 100000)
    return {"ticket_id": ticket_id, "status": "created", "severity": severity}

def check_service_status(service_name):
    #Simulated - in reality this would call a monitoring API
    return {"service_name": service_name, "status": "healthy", "uptime_pst": 99.95}

available_functions = {
    "create_incident_ticket": create_incident_ticket,
    "check_service_status": check_service_status
}

def ask_with_tools_full_loop(prompt: str):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
        config=config
    )

    part = response.candidates[0].content.parts[0]

    if part.function_call:
        fc = part.function_call
        print(f" Gemini called: {fc.name} with {dict(fc.args)}")

        # Step 3 : Actually execute it
        function_to_call = available_functions[fc.name]
        result = function_to_call(**dict(fc.args))
        print(f" Function result: {result}")

        #Step 4: Send the result BACK to Gemini so it can respond naturally
        follow_up = client.models. generate_content(
            model = "gemini-2.5-flash",
            contents=[
                prompt,
                response.candidates[0].content, # Gemini's function call turn
                types.Content(
                    role="user",
                    parts=[types.Part.from_function_response(
                        name=fc.name,
                        response=result
                    )]
                )
            ],
            config=config
        )
        print(f" Gemini's final response: {follow_up.text}")
    else:
        print(f" Gemini responded with test: {response.text}")

print(" ----- Full Loop test ----")
ask_with_tools_full_loop(
    "UPI payment gateway is down for all customers, transactions failing since 10 minutes. Please log this."
)

