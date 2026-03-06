from dotenv import load_dotenv
from openai import OpenAI
import requests

client = OpenAI()

def get_weather(city: str):
    url = f"https://wttr.in/{city}?format=%C+%t"
    response = requests.get(url)

    if response.status_code == 200:
        return f"The weather in {city} is: {response.text}"
    else:
        return "Sorry, I couldn't fetch the weather information."

def main():
    user_query = input("Enter your query: ")

    # simple logic
    if "weather" in user_query.lower():
        city = input("Enter city name: ")
        print(get_weather(city))
    else:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "user",
                    "content": user_query
                }
            ]
        )

        print(response.choices[0].message.content)

print(get_weather("New York"))