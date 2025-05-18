from transformers import AutoModel
from numpy.linalg import norm

cos_sim = lambda a,b: (a @ b.T) / (norm(a)*norm(b))
print("Loading the model weights...")
model = AutoModel.from_pretrained(r'C:\vishwa\LLM_law_bot2\volumes\models\jina-embeddings-v2-base-en', trust_remote_code=True) # trust_remote_code is needed to use the encode method
embeddings = model.encode(['How is the weather today?', 'What is the current weather like today?'])
# print(cos_sim(embeddings[0], embeddings[1]))
# print(model)

def get_embeddings(text:list):
    embeddings = model.encode(text)
    normalized_embeddings = embeddings/norm(embeddings[0])
    return normalized_embeddings

