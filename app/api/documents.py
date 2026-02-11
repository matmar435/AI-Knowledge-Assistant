from fastapi import APIRouter

from app.models.document import DocumentRequest
from app.services.vector_store import add_documents

router = APIRouter()


@router.post("/")
def add_document(request: DocumentRequest):
    add_documents([request.text])
    return {"status": "added"}
