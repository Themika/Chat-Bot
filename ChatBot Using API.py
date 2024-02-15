import requests

input = input("Enter your question: ")  # Get input from user


url = "https://chatgpt-gpt4-ai-chatbot.p.rapidapi.com/ask"

payload = { "query": f"{input}" }
headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": "21c98ce353msh2e77624f518ce0bp1fb9f3jsn84b6d813ebd7",
	"X-RapidAPI-Host": "chatgpt-gpt4-ai-chatbot.p.rapidapi.com"
}

response = requests.post(url, json=payload, headers=headers)


print(response.json().get("response"))  # Print the response from the API 