from dotenv import load_dotenv
from openai import OpenAI
from langchain_openai import OpenAIEmbeddings
from langchain_qdrant import QdrantVectorStore
load_dotenv()



embedding_model = OpenAIEmbeddings(  
    model="text-embedding-3-large")

vector_db = QdrantVectorStore(
    embedding=embedding_model,
    collection_name="learning_rag", 
    host="localhost",
    port=6333
)

#take user input query
user_query = input("Enter your query: ")

#Returns revelent chunks from the vector db
search_results=vector_db.similarity_search(query=user_query)


#This loops through the retrieved chunks (search_results), extracts their text (page_content) and metadata (page number and file source), formats them into readable text, and joins them into one large string called context.
context = "\n\n\n".join([f"Page Content: {result.page_content}\nPage Numbers {result.metadata['page_label']}\file Location: {result.metadata['source']}" for result in search_results])

SYSTEM_PROMPT = """
You are an expert AI assistant for answering user queries based on the available context retrieved from a pdf file along with page_contents and page number.

you should only ans the user based on the following context and navigate the user to open the right page number to know more

Context:
{context}

"""
response = openai_client.chart.completions.create(
    model="gpt-5",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT.format(context=context)},
        {"role": "user", "content": user_query}
    ]
)

print(f"Answer: {response.choices[0].message.content}")