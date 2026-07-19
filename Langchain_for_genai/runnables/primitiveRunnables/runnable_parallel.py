from dotenv import load_dotenv
load_dotenv()
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
# from langchain.schema.runnable import RunnableSequence
from langchain_core.runnables import RunnableSequence,RunnableParallel
llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct",
    # repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation"
)
prompt1=PromptTemplate(template="Generate a tweet about {topic}",
                       input_variables=["topic"])
prompt2=PromptTemplate(template="Generate a linkedin post  about {topic}",
                       input_variables=["topic"])
model = ChatHuggingFace(llm=llm)
parser=StrOutputParser()
parallel_chain=RunnableParallel({
    "tweet":RunnableSequence(prompt1,model,parser),
    "linkedin":RunnableSequence(prompt2,model,parser)
})
result=parallel_chain.invoke("AI")
print(result)