# from langchain_core.runnables import RunnableSequence,RunnableParallel,RunnablePassthrough,RunnableLambda
def word_counter(text):
    return len(text.split())

# runnable_word_counter=RunnableLambda(word_counter)
# print(runnable_word_counter.invoke("hi i am rajesh"))
# ==========upeer hai how runnable lambda works
from dotenv import load_dotenv
load_dotenv()
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
# from langchain.schema.runnable import RunnableSequence
from langchain_core.runnables import RunnableSequence,RunnableParallel,RunnablePassthrough,RunnableLambda
llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct",
    # repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)
parser=StrOutputParser()
template1=PromptTemplate(template="write a joke about {topic}",
                          input_variables=["topic"])
joke_gen=RunnableSequence(template1,model,parser)
paralle_chian=RunnableParallel({
    "joke":RunnablePassthrough(),
    "word_count":RunnableLambda(word_counter)
    
})
final_chain=RunnableSequence(joke_gen,paralle_chian)
print(final_chain.invoke({"topic":"Ai"}))