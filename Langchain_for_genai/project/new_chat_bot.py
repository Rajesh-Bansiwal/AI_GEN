from dotenv import load_dotenv
load_dotenv()

from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.messages import AIMessage,HumanMessage,SystemMessage
llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)
chat_history=[SystemMessage(content="You are a helpful AI assistent")]
while True:
    user_input=input("You : ")
    chat_history.append(user_input)
    if user_input == 'exit':
        break
    result=model.invoke(chat_history)
    chat_history.append(AIMessage(result.content))
    print("AI : ",result.content)


# result = model.invoke("What is nsc?")
# print(result)
# print(result.content)
print(chat_history)
# no need to know konsa message kisne likhe hai langchain automatically knows