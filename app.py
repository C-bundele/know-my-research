from src.data_loader import load_all_documents
from src.embedding import EmbeddingPipeline
from src.vectorstore import FaissVectorStore
from src.search import RAGSearch



# Example usage
if __name__ == "__main__":
    
    docs = load_all_documents("data")
    store = FaissVectorStore("faiss_store")
    store.build_from_documents(docs)
    store.load()
    print(store.query("What is clustering and KNN?", top_k=3))
    rag_search = RAGSearch()
    query = "What is clustering and KNN?"
    summary = rag_search.search_and_summarize(query, top_k=3)
    print("Summary:", summary)
    print(docs)
# if __name__ == "__main__":
    
#     docs = load_all_documents("data")
#     emb_pipe = EmbeddingPipeline()
#     chunks = emb_pipe.chunk_documents(docs)
#     embeddings = emb_pipe.embed_chunks(chunks)
#     print("[INFO] Example embedding:", embeddings[0] if len(embeddings) > 0 else None)

# if __name__ == "__main__":
    
#     docs = load_all_documents("data")
#     store = FaissVectorStore("faiss_store")
#     store.build_from_documents(docs)
#     store.load()
#     print(store.query("What is clustering?", top_k=3))

# Example usage
# if __name__ == "__main__":
#     rag_search = RAGSearch()
#     query = "What is clustering and  KNN?"
#     summary = rag_search.search_and_summarize(query, top_k=3)
#     print("Summary:", summary)