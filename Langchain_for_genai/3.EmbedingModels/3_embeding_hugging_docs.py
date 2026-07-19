from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(
    model_name="BAAI/bge-small-en-v1.5"

)
documents=["Delhi is the capital of India","Kolkata is the capital of West Bengal","Paris is the capital of France"]

# result = embedding.embed_query("Delhi is the capital of India")
result=embedding.embed_documents(documents)
# print(len(result))s
print(str(result))