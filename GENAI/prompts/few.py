#Few Shot prompting: Providing the model with a few examples of the desired output format or task before asking it to generate a response. This helps the model understand the context and produce more accurate results based on the provided examples.
from openai import OpenAI

client = OpenAI(
    api_key="API-KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)
# Few shot prompting: Directly giving the instructions to the model and few examples to the model
SYSTEM_PROMPT = """You should only and only answer the coding related questions.Your name is codemaster and if user asks you anything else you should reply with 'I am sorry I can only answer coding related questions'

Examples:
Q: Can you explain a+b whole square?
A: Sorry I can only answer coding related questions.

Q: Write a simple 'Hello, World!' program in Python.
A: Sure! Here is a simple 'Hello, World!' program in Python:

```python   
print("Hello, World!")
```
"""  

USER_PROMPT = "Can you explain a+b whole square?"

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
