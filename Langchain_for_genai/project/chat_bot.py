    from dotenv import load_dotenv
    # import os/

    load_dotenv()

    # print(os.getenv("HUGGINGFACEHUB_API_TOKEN"))

    from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
    from langchain_core.messages import AIMessage,HumanMessage,SystemMessage
    llm = HuggingFaceEndpoint(
        # repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
        # task="text-generation"
        repo_id="Qwen/Qwen2.5-7B-Instruct",
        task="text-generation"
    )

    model = ChatHuggingFace(llm=llm)
    chat_history=[]
    while True:
        user_input=input("You : ")
        chat_history.append(user_input)
        if user_input == 'exit':
            break
        result=model.invoke(chat_history)
        chat_history.append(result.content)
        print("AI : ",result.content)


    # result = model.invoke("What is nsc?")
    # print(result)
    # print(result.content)
    print(chat_history)
    # no need to know konsa message kisne likhe hai langchain automatically knows