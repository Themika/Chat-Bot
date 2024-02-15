import requests
import os
from dotenv import load_dotenv

load_dotenv()

ApiKey = os.getenv("API_KEY")
input = input("Enter your question: ")  # Get input from user


url = "https://chatgpt-gpt4-ai-chatbot.p.rapidapi.com/ask"

payload = { "query": f"{input}" }
headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": f"{ApiKey}", #Replace with yoru own api key :)
	"X-RapidAPI-Host": "chatgpt-gpt4-ai-chatbot.p.rapidapi.com"
}

response = requests.post(url, json=payload, headers=headers)


print(response.json().get("response"))  # Print the response from the API 