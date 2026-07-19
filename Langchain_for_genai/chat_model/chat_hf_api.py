# from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
# import os
# from dotenv import load_dotenv
# load_dotenv()
# print(os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN"))
# llm=HuggingFaceEndpoint(repo_id='TinyLlama/TinyLlama-1.1B-Chat-v1.0',task="text-generation")
# model=ChatHuggingFace(llm=llm)
# result=model.invoke("what is the capital of india")
# print(result.content)

from dotenv import load_dotenv
import os

load_dotenv()

print(os.getenv("HUGGINGFACEHUB_API_TOKEN"))

from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace

llm = HuggingFaceEndpoint(
    # repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    # task="text-generation"
    repo_id="Qwen/Qwen2.5-7B-Instruct",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

result = model.invoke("What is nsc?")
# print(result)
print(result.content)