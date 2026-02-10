from app.services.vector_store import  add_documents

with open("data/knowledge.txt", "r", encoding="utf-8") as f:
    texts = [line.strip() for line in f.readlines() if line.strip()]

add_documents(texts)

print("Wiedza załadowana")