from openai import OpenAI

client = OpenAI(
    api_key="API-KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
    model="gemini-3-flash-preview",
    messages=[
        #prompt to restrict or set a background for the model to answer the question
        { "role": "system",
          "content": "You are an expert in maths and you should only answer questions related to maths."},
        {   "role": "user",
            "content": "Hey can you help me solve a+b whole square?"
        }
        
    ]
)

print(response.choices[0].message.content)