from dotenv import load_dotenv
from openai import OpenAI
import json

load_dotenv()

client = OpenAI(
    api_key="API-KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

SYSTEM_PROMPT = """
You are an expert AI assistant in resolving user queries using chain of thought.

You work in 3 steps:
START → PLAN → OUTPUT

Rules:
- Strictly follow JSON format
- Only one step at a time
- PLAN can repeat multiple times

Output format:

{
 "step": "START | PLAN | OUTPUT",
 "content": "text"
}
"""

message_history = [
    {"role": "system", "content": SYSTEM_PROMPT}
]

user_query = input("User: ")

message_history.append({
    "role": "user",
    "content": user_query
})

while True:

    response = client.chat.completions.create(
        model="gemini-3-flash-preview",
        response_format={"type": "json_object"},
        messages=message_history
    )

    raw_result = response.choices[0].message.content

    message_history.append({
        "role": "assistant",
        "content": raw_result
    })

    parsed_result = json.loads(raw_result)

    if parsed_result.get("step") == "START":
        print("START:", parsed_result.get("content"))
        continue

    if parsed_result.get("step") == "PLAN":
        print("PLAN:", parsed_result.get("content"))
        continue

    if parsed_result.get("step") == "OUTPUT":
        print("\nFINAL OUTPUT:")
        print(parsed_result.get("content"))
        break