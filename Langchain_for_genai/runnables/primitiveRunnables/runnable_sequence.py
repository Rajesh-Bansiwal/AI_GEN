from dotenv import load_dotenv
load_dotenv()
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
# from langchain.schema.runnable import RunnableSequence
from langchain_core.runnables import RunnableSequence
llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct",
    # repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)
parser=StrOutputParser()
template1=PromptTemplate(template="write a joke about {topic}",
                          input_variables=["topic"])
template2=PromptTemplate(template="Explain the following - joke {text}",
                          input_variables=["text"])
chain=RunnableSequence(template1,model,parser,template2,model,parser)
print(chain.invoke({"topic":"AI"}))