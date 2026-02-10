import chromadb
from sentence_transformers import SentenceTransformer

# model do embedingów
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

# lokalna baza
chroma_client = chromadb.Client()
collection = chroma_client.get_or_create_collection("knowledge")


def add_documents(texts):
    embeddings = embedding_model.encode(texts).tolist()

    collection.add(
        documents=texts,
        embeddings=embeddings,
        ids=[str(i) for i in range(len(texts))]
    )


def search(querry: str, k: int = 2):
    querry_embedding = embedding_model.encode([querry]).tolist()

    results = collection.query(
        querry_embeddings=querry_embedding,
        n_results=k
    )

    return results["documents"][0]
