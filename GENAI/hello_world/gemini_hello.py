from google import genai
client = genai.Client(
    api_key="API-KEY"
)
response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="Write a simple 'Hello, World!' program in Python."
)
print(response.text)    
