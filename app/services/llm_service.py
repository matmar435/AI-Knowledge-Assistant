import requests

OLLAMA_URL = "http://localhost:11434/api/generate"


def generate_response(question: str) -> str:
    prompt = f"""
        Jesteś pomocnym asystentem AI.
        Odpowiadaj zawsze po polsku.

        Pytanie:
        {question}
        """
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
