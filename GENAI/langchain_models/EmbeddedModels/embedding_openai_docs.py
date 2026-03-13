from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbedding(model="text-embedding-3-small", dimensions=12)


documents = [
    "The capital of India is New Delhi.",
    "The capital of France is Paris.",
    "The capital of Japan is Tokyo."
]
result = embedding.embed_documents(documents)


print(str(result)) 