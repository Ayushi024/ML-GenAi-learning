from openai import OpenAI

client = OpenAI(
    api_key="API-KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)
#Zero shot prompting: Directly asking the model to perform a task without providing any examples. The model relies solely on its pre-trained knowledge to generate a response based on the given prompt.
SYSTEM_PROMPT = "You are a helpful assistant that translates English to Python code."
USER_PROMPT = "Write a simple 'Hello, World!' program in Python."

response = client.chat.completions.create(
    model="gemini-3-flash-preview",
    messages=[
        #prompt to restrict or set a background for the model to answer the question
        { "role": "system",
          "content": SYSTEM_PROMPT },
        {   "role": "user",
            "content": USER_PROMPT
        }
        
    ]
)

print(response.choices[0].message.content)
#1. Zero- shot prompting: The model is given a direct ques or task without prior examples.