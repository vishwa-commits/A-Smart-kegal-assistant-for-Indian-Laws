from .llm import nemotron_llama
from .embeddings import get_embeddings
from .retriever import vector_db_retriever
import pickle

with open(r"C:\vishwa\LLM_law_bot2\volumes\metadata\new_pdfs_corpus_data.pkl", "rb") as p:
    metadata = pickle.load(p)

# ids = list(metadata.keys())


# def RAG(query, chat_history):
#     query_embeddings = get_embeddings([query])
#     result = vector_db_retriever(query_embeddings, 10)
#     indexes = result[0][0]
#     context = ""
#     for idx in indexes:
#         hash_id = ids[idx]
#         retrieved_results = metadata[hash_id]
#         context+="Title:"+retrieved_results['title']+"\n"+"Date:"+retrieved_results['date']+"\n"+"Page Number:"+str(retrieved_results['page_no'])+"\n"+"Corpus:"+retrieved_results['text']+"\n\n"
#     completion = nemotron_llama(query, context, chat_history)
#     # for chunk in completion:
#     #     if chunk.choices[0].delta.content is not None:
#     #         print(chunk.choices[0].delta.content, end = '')
#     return completion
# RAG("explain the seventh amentment act", chat_history=[])


def RAG(query, chat_history):
    query_embeddings = get_embeddings([query])
    result = vector_db_retriever(query_embeddings, 10)
    indexes = result[0][0]
    context = ""
    for idx in indexes:
        # hash_id = ids[idx]
        retrieved_results = metadata[idx]
        context+="Title:"+retrieved_results['title']+"\n"+"Page Number:"+str(retrieved_results['page'])+"\n"+"Corpus:"+retrieved_results['paragraphs']+"\n\n"
    completion = nemotron_llama(query, context, chat_history)
    # for chunk in completion:
    #     if chunk.choices[0].delta.content is not None:
    #         print(chunk.choices[0].delta.content, end = '')
    return completion

print("imported sucessfully")