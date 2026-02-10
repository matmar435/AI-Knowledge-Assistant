import requests

OLLAMA_URL = "http://localhost:11434/api/generate"


def generate_response(prompt: str) -> str:
    payload = {
        "model": "llama3",
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post(OLLAMA_URL, json=payload)
        response.raise_for_status()
        data = response.json()
        return data["response"]
    except Exception as e:
        return f"LLM error: {e}"
