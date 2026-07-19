from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
load_dotenv()
embedding = HuggingFaceEmbeddings(
    model_name="BAAI/bge-small-en-v1.5"

)
documents=["Delhi is the capital of India","Kolkata is the capital of West Bengal","Paris is the capital of France"]

# result = embedding.embed_query("Delhi is the capital of India")
query="tell me capital of india"
doc_embeding=embedding.embed_documents(documents)
query_embeding=embedding.embed_query(query)
scores=cosine_similarity([query_embeding],doc_embeding)[0] #[[0.80354201 0.70554831 0.64038346]]
# print("scores pehle : ",scores)
index,scores=sorted(list(enumerate(scores)),key=lambda x:x[1])[-1]
print(query)
print(documents[index])
print("similaarity scores is : ",scores)
# print(list(enumerate(scores)))