import os
import uuid

import chromadb
from sentence_transformers import SentenceTransformer

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
DB_PATH = os.path.join(BASE_DIR, "app/db/chroma_db")

# model do embedingów
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

# lokalna baza
chroma_client = chromadb.PersistentClient(DB_PATH)
collection = chroma_client.get_or_create_collection(name="knowledge")

def add_documents(texts):
    embeddings = embedding_model.encode(texts).tolist()

    collection.add(
        documents=texts,
        embeddings=embeddings,
        ids=[str(uuid.uuid4()) for i in range(len(texts))]
    )


def search(query: str, k: int = 2):
    query_embedding = embedding_model.encode([query]).tolist()

    results = collection.query(
        query_embeddings=query_embedding,
        n_results=k
    )

    return results["documents"][0]
