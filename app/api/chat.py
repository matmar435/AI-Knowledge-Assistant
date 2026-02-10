from fastapi import APIRouter
from pydantic import BaseModel

from app.pipelines.rag_pipeline import ask_with_context

router = APIRouter()


class ChatRequest(BaseModel):
    question: str


class ChatResponse(BaseModel):
    answer: str


@router.post("/", response_model=ChatResponse)
def chat(request: ChatRequest):
    answer = ask_with_context(request.question)
    return ChatResponse(answer=answer)
