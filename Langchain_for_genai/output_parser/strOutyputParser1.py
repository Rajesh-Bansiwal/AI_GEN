# output parsers use chains method
from dotenv import load_dotenv
load_dotenv()
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct",
    # repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)
template1=PromptTemplate(template="write a detail report on {topic}",
                          input_variables=["topic"])
template2 = PromptTemplate(
    template="Write a 5-line summary on the following text.\n{text}",
    input_variables=["text"]
)
parser=StrOutputParser()
# parserne result me se string output nikala or dusre me daal diya 
chain =template1 | model | parser | template2 | model | parser
result =chain.invoke({'topic':'black hole'})
print(result)