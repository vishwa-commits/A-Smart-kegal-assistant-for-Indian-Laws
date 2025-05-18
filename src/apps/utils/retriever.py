import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"  # Temporary fix
os.environ["FAISS_NO_OPENMP"] = "1"  # Prevent FAISS from using OpenMP

import faiss
from numpy.linalg import norm

index = faiss.read_index(r"C:\vishwa\LLM_law_bot2\volumes\indexes\law_corpus_index2.bin")
print("Index loaded successfully!")
print("Number of vectors in the index:", index.ntotal)

def vector_db_retriever(query_embeddings, top_k=10):
    query_embeddings = query_embeddings / norm(query_embeddings[0])
    distances, indices = index.search(query_embeddings, top_k)
    return indices, distances
