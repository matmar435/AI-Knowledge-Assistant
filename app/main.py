from fastapi import FastAPI
from app.api import healt

app = FastAPI(title="Ai Knowledge Assistant")

#rejestracja routerów
app.include_router(healt.router, prefix="/health")