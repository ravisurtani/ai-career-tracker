import os
from google import genai
from google.genai import types


# - Setup (Same pattern as Day 13/14) --
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

# - Tool definitions (Carried over from Day 12) -----------

create_incident_ticket = {

    "name": "create_incident_ticket",
    "description": "Create an incident ticket in the ticketing system for a reported issue",
    "parameters": {  
        "type": "object",
        "properties": {
            "title" : {"type": "string", "description": "Short summary of the incident"},
            "severity": {"type": "string", "enum": ["P1", "P2", "P3", "P4"]},
            "reference_id": {"type": "string", "description": "RRN/UTR or transaction reference tied to the issue"},
        },
        "required": ["title", "severity"],
    },
}


check_service_status = {
    "name": "check_service_status",
    "description": "Checks current operational status of a payment rail (UPI, NEFT, RTGS).",
    "parameters": { 
        "type": "object",
        "properties": {
            "service_name": {"type": "string" , "enum": ["UPI", "NEFT", "RTGS"]},
        },
        "required": ["service_name"],
    },
}
                     
tools = types.Tool(function_declarations = [create_incident_ticket, check_service_status])

# - Fake backend implementation  (stubs, same as day 12) --------------

def run_create_incident_ticket(title, severity, reference_id=None):
    return {
        "ticket_id": "INC0045231",
        "status": "created",
        "title": title,
        "severity": severity,
        "reference_id": reference_id,
    }

def run_check_service_status(service_name):
    return {"service_name": service_name, "status": "degraded", "eta_resolution": "20 mins"}

available_functions = {
    "create_incident_ticket": run_create_incident_ticket,
    "check_service_status": run_check_service_status,
}

# --------------Persona (carried over from Day 14) -------------

persona = (
    "You are a terse, senior payment SME at a bank's Incident Management desk."
    "Answer concisely, no fluff, no 'As an AI....' preambles."
    "if a transaction reference ID is missing and it's relevant, ask for it before proceeding. "
    "when appropriate, use the available tools to check service status or raise incident tickets "
    "instead of just describing what should be done."
)

config = types.GenerateContentConfig(
    system_instruction=persona,
    tools=[tools],
)


# ---------Create the persistent chat session (day 13 features) ------------
chat =client.chats.create(model="gemini-2.5-flash", config=config)


def send_and_handle(user_message):
    response = chat.send_message(user_message)

    # Check if the model wants to call a tool
    candidate =  response.candidates[0]
    function_call_part = None

    for part in candidate.content.parts:
        if part.function_call:
            function_call_part = part.function_call
            break

    if function_call_part is None:
        # No tool call - just print the model's text reply
        print(f"Agent: {response.text}\n")
        return

    # ---------- Tool was requested - execute it locally ------------

    fn_name = function_call_part.name
    fn_args = dict(function_call_part.args)
    print(f"[Agent is calling the tool: {fn_name}({fn_args})]")


    if fn_name not in available_functions:
        result = {"error": f"Unknown function {fn_name}"}

    else :
        result = available_functions[fn_name](**fn_args)

# ------------ Feed the tool result back into the SAME chat session ------------
    function_response_part = types.Part.from_function_response(
    name=fn_name,
    response={"result": result},
    )

    follow_up = chat.send_message(function_response_part)
    print(f"Agent: {follow_up.text}\n")



# ------------- Run a multi-turn conversation ----------

if __name__ == "__main__":
    print("Day 15 - Conversational Agent (type 'quit' to exit)\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            break
        send_and_handle(user_input)

        



