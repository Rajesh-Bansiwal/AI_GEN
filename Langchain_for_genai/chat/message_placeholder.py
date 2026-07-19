from dotenv import load_dotenv
load_dotenv()
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.messages import AIMessage,HumanMessage,SystemMessage
llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct",
    task="text-generation"
)
chat_template=ChatPromptTemplate([('system','You are a helpful customer support agent'),
                                  MessagesPlaceholder(variable_name='chat_history'), 
                                  # messageholder craete a placeholder purani chat ke behave per aage talk kr saker 
                                  ('human','{query}')])

chat_history=[]
with open(r'C:\Invos_Projects\GEN_AI\AI_GEN\langchain\chat\chat_history.txt') as f:
    chat_history.extend(f.readlines())
    
print(chat_history)

prompt=chat_template.invoke({'chat_history':chat_history,'query':'where is my refund'})
model = ChatHuggingFace(llm=llm)
result=model.invoke(prompt)
print(result.content)