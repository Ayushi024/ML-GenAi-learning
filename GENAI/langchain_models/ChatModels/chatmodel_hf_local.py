from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFacePipeline(
    repo_id="TinyLlama/TinyLlama-1.1B-GGUF",    task="text-generation", 
    pipeline_kwargs={"temperature": 0.7, "max_new_tokens": 100}
)

model = ChatHuggingFace(llm=llm)

result = model.invoke("What is the capital of India?") 
print(result.content) 