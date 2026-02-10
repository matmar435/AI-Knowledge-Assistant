from fastapi import FastAPI
from app.api import healt, chat

app = FastAPI(title="Ai Knowledge Assistant")

#rejestracja routerów
app.include_router(healt.router, prefix="/health")
app.include_router(chat.router, prefix="/chat")