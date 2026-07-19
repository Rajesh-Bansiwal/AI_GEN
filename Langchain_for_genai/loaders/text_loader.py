# from langchain_community.document_loaders import TextLoader
from dotenv import load_dotenv
load_dotenv()
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import TextLoader
llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct",
    # repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)
parser=StrOutputParser()
loader =TextLoader(r'C:\Invos_Projects\GEN_AI\AI_GEN\langchain\loaders\poem.txt',encoding='utf-8')
docs=loader.load()
template = PromptTemplate(
    template="Write a summary for the following poem - \n{text}",
    input_variables=["text"]
)
# print(docs)
# iska type list hai 
print(docs[0].page_content) #is ka type wo ek documnet 
chain=template | model | parser
print(chain.invoke({"text":docs[0].page_content}))
