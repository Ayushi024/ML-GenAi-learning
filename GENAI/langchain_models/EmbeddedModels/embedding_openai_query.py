from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbedding(model="text-embedding-3-small", dimensions=12)

result = embedding.embed_query("What is the capital of India?")



print(result.content) 