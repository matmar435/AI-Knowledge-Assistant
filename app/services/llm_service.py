import requests

OLLAMA_URL = ""

def generate_response(prompt: str) -> str:
    payload = {
        "model" : "llama3",
        "prompt" : prompt,
        "stream" : False
    }

    response = requests.post(OLLAMA_URL, json=payload)
    data = response.json()
    return data["response"]