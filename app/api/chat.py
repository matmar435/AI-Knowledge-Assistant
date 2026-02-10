from fastapi import APIRouter
from pydantic import BaseModel
from app.services.llm_service import generate_response

router = APIRouter()


class ChatRequest(BaseModel):
    question: str


class ChatResponse(BaseModel):
    answer: str


@router.post("/", response_model=ChatResponse)
def chat(request: ChatRequest):
    answer = generate_response(request.question)
    return ChatResponse(answer=answer)
