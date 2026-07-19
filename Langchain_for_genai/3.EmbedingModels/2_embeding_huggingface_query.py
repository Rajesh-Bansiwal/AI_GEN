from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(
    model_name="BAAI/bge-small-en-v1.5"

)

result = embedding.embed_query("Delhi is the capital of India")
# print(len(result))
print(result)