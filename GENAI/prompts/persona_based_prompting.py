from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()

client = OpenAI(
    api_key="API-KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

SYSTEM_PROMPT = """
You are an AI Persona Assistant named Piyush Garg.
You are acting on behalf of Piyush Garg who is a 25 years old tech enthusiastic and a principal engineer.
His main tech stack is JavaScript and Python and he is currently learning Generative AI.

Your job is to reply to the user exactly how Piyush Garg would reply.
"""

response = client.chat.completions.create(
    model="gemini-3-flash-preview",
    messages=[
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": "What is your name?"
        }
    ]
)

print(response.choices[0].message.content)