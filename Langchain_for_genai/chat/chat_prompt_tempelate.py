from dotenv import load_dotenv
load_dotenv()
from langchain_core.prompts import ChatPromptTemplate
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.messages import AIMessage,HumanMessage,SystemMessage
llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct",
    task="text-generation"
)
chat_tempelate=ChatPromptTemplate([
    ('system',"You are a helpful {domain} expert"),
    ('human','Explain in simple terms, what is {topic}')
    # SystemMessage(content="You are a helpful {domain} expert"),
    # HumanMessage(content="Explain in simple terms, what is {topic}")
])
# model = ChatHuggingFace(llm=llm)
prompt=chat_tempelate.invoke({'domain':'cricket','topic':'Dusra'})
print(prompt)
