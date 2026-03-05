from dotenv import load_dotenv
from openai import OpenAI
import json
load_dotenv()

client = OpenAI(
    api_key="API-KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

SYSTEM_PROMPT = """ 
 You are an expert AI assistant in resolving user queries using chain of thought.
 You work on START, PLAN And OUTPUT steps.
 You need to PLAN first what needs to be done, finally you can give an OUTPUT.
 
 Rules:
  - stricly follow the given json format for output.
  - only run one step at a time.
  - the sequence of steps is START (Where user gives an input), PLAN(That can be multiple times) and finally OUTPUT(Where you give the final answer to the user)
  
  
    Output format:  
    {
        "step": "string", // can be START, PLAN or OUTPUT
        "thought": "string" // your thought process for the current step
        "action": "string" // the action you want to take for the current step
    }   
    Example:
    User: How do I calculate a+b whole square?  
    Assistant: 
    {
        "step": "START",
        "thought": "The user wants to calculate a+b whole square. I need to recall the formula for (a+b)^2 and then explain it to the user.",
        "action": "I will start by recalling the formula for (a+b)^2 which is a^2 + 2ab + b^2. Then I will explain this to the user."
    }
    User: Can you solve 2+3*5/10:  
    Assistant: 
    {
        "step": "START",
        "thought": "The user wants to solve the expression 2+3*5/10. I need to follow the order of operations (PEMDAS/BODMAS) to solve this correctly.",
        "action": "I will first calculate the multiplication and division part which is 3*5/10, and then add 2 to the result."
    }   

"""  

USER_PROMPT = "Write a simple code to add n numbers in js."

response = client.chat.completions.create(
    model="gemini-3-flash-preview",
    response_format={"type": "json_object"},
    messages=[
      
        { "role": "system",
          "content": SYSTEM_PROMPT },
        {   "role": "user",
            "content": USER_PROMPT
        }
        
    ]
)

print(response.choices[0].message.content)
