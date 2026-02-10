from app.services.llm_service import generate_response
from app.services.vector_store import search


def ask_with_context(question: str) -> str:
    docs = search(question)

    context = "\n".join(docs)

    prompt = f"""
    Jesteś pomocnym asystentem AI. Odpowiadaj zawsze po polsku.
    Odpowiadaj jasno i profesjonalnie.
    Używaj prostego języka.
    Unikaj trudnych słów i neologizmów.
    Wykorzystaj KONTEKST poniżej do odpowiedzi na pytanie.
    Jeśli KONTEKST nie zawiera odpowiedzi, powiedz "Nie wiem"
    
    Kontekst:
    {context}
    
    Pytanie:
    {question}
    """

    return generate_response(prompt)
