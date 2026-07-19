from dotenv import load_dotenv
load_dotenv()
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
# system message jaise you are a doctor phir start krte hai 
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace

llm = HuggingFaceEndpoint(
    # repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    # task="text-generation"
    repo_id="Qwen/Qwen2.5-7B-Instruct",
    # task="text-generation"
)
model=ChatHuggingFace(llm=llm)
messages=[SystemMessage(content="You are a helpful assistent"),
          HumanMessage(content="Tell me about langchain")]
result=model.invoke(messages)
messages.append(AIMessage(content=result.content))
# print(result.content)
print(messages)