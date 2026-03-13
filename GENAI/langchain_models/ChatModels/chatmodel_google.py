from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-pro",
    temperature=0.7,
    max_tokens=1024
)

result = model.invoke("What is the capital of india?")
print(result)
print(result.content)