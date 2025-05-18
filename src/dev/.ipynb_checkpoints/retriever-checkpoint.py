# import faiss
# import numpy as np

# # Set the embedding dimension
# dimension = 768  
# num_vectors = 10  

# # Create random embeddings
# np.random.seed(42)
# embeddings = np.random.random((num_vectors, dimension)).astype('float32')

# # Create a FAISS index
# index = faiss.IndexFlatL2(dimension)
# index.add(embeddings)

# # Create a random query vector
# query_vector = np.random.random((1, dimension)).astype('float32')

# # Search in the index
# distances, indices = index.search(query_vector, 5)

# # Print results
# print("Search successful!")
# print("Nearest Neighbors:", indices)
# print("Distances:", distances)

import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"  # Temporary fix
os.environ["FAISS_NO_OPENMP"] = "1"  # Prevent FAISS from using OpenMP

import faiss
from numpy.linalg import norm

index = faiss.read_index("../../volumes/indexes/law_corpus_index.bin")
print("Index loaded successfully!")
print("Number of vectors in the index:", index.ntotal)

# distances, indices = index.search(query_embeddings, 5)
 
def vector_db_retriever(query_embeddings, top_k=10):
    query_embeddings = query_embeddings/norm(query_embeddings[0])
    distances, indices = index.search(query_embeddings, top_k)
    return indices, distances

# from transformers import AutoModel
# from numpy.linalg import norm

# cos_sim = lambda a,b: (a @ b.T) / (norm(a)*norm(b))
# model = AutoModel.from_pretrained('../../volumes/models/jina-embeddings-v2-base-en/', trust_remote_code=True) # trust_remote_code is needed to use the encode method
# # embeddings = model.encode(['How is the weather today?', 'What is the current weather like today?'])
# # print(cos_sim(embeddings[0], embeddings[1]))
# print(model)

# query = "Application to Jammu and Kashmir"
# query_embeddings = model.encode([query])
# query_embeddings = query_embeddings/norm(query_embeddings[0])
# print("generating query embeddings")

# # Search in the index
# distances, indices = index.search(query_embeddings, 5)
# print("getting distance")
# # Print results
# print("Search successful!")
# print("Nearest Neighbors:", indices)
# print("Distances:", distances)