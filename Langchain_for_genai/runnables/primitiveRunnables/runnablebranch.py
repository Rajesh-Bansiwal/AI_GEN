# used fro conditional execution like if else
from dotenv import load_dotenv
load_dotenv()
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
# from langchain.schema.runnable import RunnableSequence
from langchain_core.runnables import RunnableSequence,RunnableParallel,RunnablePassthrough,RunnableLambda,RunnableBranch
llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct",
    # repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)
parser=StrOutputParser()
template1=PromptTemplate(template="write a detailed report on {topic}",
                          input_variables=["topic"])
template2=PromptTemplate(template="Summarize the following text \n {text}",
                          input_variables=["topic"])

report_gen=RunnableSequence(template1,model,parser)
branch_chain=RunnableBranch((lambda x:len(x.split())>500,RunnableSequence(template2,model,parser)),
                            RunnablePassthrough()
                            )
final_chain=report_gen | branch_chain
print(final_chain.invoke({"topic":"Russia vs Ukrain"}))