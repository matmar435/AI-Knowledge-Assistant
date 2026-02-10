from app.services.llm_service import generate_response
from app.services.vector_store import search


def ask_with_context(question: str) -> str:
    docs = search(question)

    context = "\n".join(docs)

    prompt = f"""
    Odpowiadaj po polsku.
    
    Kontekst:
    {context}
    
    Pytanie:
    {question}
    """

    return generate_response(prompt)
