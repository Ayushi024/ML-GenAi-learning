from dotenv import load_dotenv
from openai import OpenAI
import os
import requests
import json

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))  # Make sure your .env has OPENAI_API_KEY

def get_weather(city: str):
    url = f"https://wttr.in/{city}?format=%C+%t"
    response = requests.get(url)
    if response.status_code == 200:
        return f"The weather in {city} is: {response.text}"
    else:
        return "Sorry, I couldn't fetch the weather information."

# Available tools
available_tools = {
    "get_weather": get_weather
}

SYSTEM_PROMPT = """
You are an expert AI assistant for weather queries.
You use a step-by-step chain-of-thought approach.

Steps:
- START: Understand the user query and what needs to be done.
- PLAN: Decide which tools to call and for which cities.
- TOOL: Call get_weather(city) for each city separately. Wait for observation after each tool call.
- OUTPUT: Summarize the results of all cities into one final answer.

Rules:
- Show each step clearly :
   START
   PLAN
   TOOL
- For multiple cities, call the tool separately for each city.
- Always respond in JSON format:
{
 "step": "START | PLAN | TOOL | OUTPUT",
 "content": "string",
 "tool": "tool_name_if_needed",
 "input": "tool_input_if_needed"
}

Available tools:
get_weather(city:str)
"""

while True:
    user_query = input("Enter your query: ")

    message_history = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_query}
    ]

    while True:
        response = client.chat.completions.create(
            model="gemini-3-flash-preview",
            response_format={"type": "json_object"},
            messages=message_history
        )

        raw_result = response.choices[0].message.content
        parsed_result = json.loads(raw_result)

        step = parsed_result.get("step")
        content = parsed_result.get("content")

        if step == "START":
            print( content)
            message_history.append({"role": "assistant", "content": raw_result})
            continue

        if step == "PLAN":
            print(content)
            message_history.append({"role": "assistant", "content": raw_result})
            continue

        if step == "TOOL":
            tool_call = parsed_result.get("tool")
            tool_input = parsed_result.get("input")

            if tool_call not in available_tools:
                print(f" Tool {tool_call} not found")
                break

            # Support multiple cities separated by comma
            cities = [city.strip() for city in tool_input.split(",")]
            for city in cities:
                print(f" Running tool: {tool_call}({city})")
                tool_response = available_tools[tool_call](city)

                # Send observation back to LLM
                observation_msg = json.dumps({"observation": tool_response})
                message_history.append({"role": "user", "content": observation_msg})

            continue

        if step == "OUTPUT":
            print("\n Final Answer:")
            print(content)
            break