from dotenv import load_dotenv
load_dotenv()

from langchain_community.document_loaders import WebBaseLoader
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda

llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

def load_page(inputs):
    loader = WebBaseLoader("https://app.invosresearch.com")
    docs = loader.load()

    return {
        "content": docs[0].page_content,
        "question": inputs["question"]
    }

prompt = PromptTemplate(
    template="""
You are given a webpage.

Webpage:
{content}

User Question:
{question}

Instructions:
1. First summarize the webpage in 5-6 lines.
2. Then answer the user's question using only the webpage content.
""",
    input_variables=["content", "question"]
)

chain = (
    RunnableLambda(load_page)
    | prompt
    | model
    | StrOutputParser()
)

result = chain.invoke({
    "question": "this app give momentum"
})

print(result)