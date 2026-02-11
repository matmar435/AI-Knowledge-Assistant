from fastapi import FastAPI
from app.api import healt, chat, documents

app = FastAPI(title="Ai Knowledge Assistant")

# rejestracja routerów
app.include_router(healt.router, prefix="/health")
app.include_router(chat.router, prefix="/chat")
app.include_router(documents.router, prefix="/documents", tags=["documents"])
