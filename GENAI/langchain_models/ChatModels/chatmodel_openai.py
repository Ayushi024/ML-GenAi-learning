from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()


model = ChatOpenAI(model="gpt-4" temperature=0.7, max_completion_token=10) #here temperature is a parameter that controls the randomness of the output. A higher temperature will result in more random output, while a lower temperature will result in more deterministic output. You can adjust this parameter based on your needs.

#max_completion_token is a parameter that limits the maximum number of tokens in the response. This can be useful to control the length of the output and prevent excessively long responses so that you can manage the cost and response time of the API calls.

result = model.invoke("What is the capital of India?")
print(result)  # this will print the entire response object, which may include metadata and other information
print(result.content) # this will print just the content of the response, which is the answer to the question about the capital of India