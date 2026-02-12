import os
import uuid

from fastapi import APIRouter, UploadFile, File

from app.models.document import DocumentRequest
from app.services.file_parsers import read_pdf, read_docx, read_txt
from app.services.ingestion import chunk_text
from app.services.vector_store import add_documents, collection

router = APIRouter()
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.get("/")
def list_documents(limit: int = 20):
    data = collection.get(limit=limit)
    return {
        "count": len(data["ids"]),
        "documents": [
            {
                "id": data["ids"][i],
                "text": data["documents"][i][:200]
            }
            for i in range(len(data["ids"]))
        ]
    }


@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    file_id = str(uuid.uuid4())
    path = os.path.join(UPLOAD_DIR, f"{file_id}_{file.filename}")

    with open(path, "wb") as f:
        f.write(await file.read())

    # wybór parsera
    if file.filename.endswith(".pdf"):
        text = read_pdf(path)
    elif file.filename.endswith(".docx"):
        text = read_docx(path)
    elif file.filename.endswith(".txt"):
        text = read_txt(path)
    else:
        return {"error": "Unsupported file type"}

    chunks = chunk_text(text)

    add_documents(chunks)

    return {"status": "upload", "chunks": len(chunks)}


@router.delete("/{doc_id")
def delete_document(doc_id: str):
    collection.delete(ids=[doc_id])
    return {"status": "deleted", "id": doc_id}
