
from openai import OpenAI

client = OpenAI(
    api_key="API-KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

SYSTEM_PROMPT = """You should only and only answer the coding related questions.Your name is codemaster and if user asks you anything else you should reply with 'I am sorry I can only answer coding related questions'

Rule:
- Strictly follow the output in JSON format

output format:
{
    "code": "string" or null,
    "isCodingQuestion": boolean
}
Examples:
Q: Can you explain a+b whole square?
A: {"code": null, "isCodingQuestion": false}

Q: Write a simple 'Hello, World!' program in Python.
A: {"code": "print('Hello, World!')", "isCodingQuestion": true}

"""  

USER_PROMPT = "Write a simple 'Hello, World!' program in Python."

response = client.chat.completions.create(
    model="gemini-3-flash-preview",
    messages=[
      
        { "role": "system",
          "content": SYSTEM_PROMPT },
        {   "role": "user",
            "content": USER_PROMPT
        }
        
    ]
)

print(response.choices[0].message.content)
