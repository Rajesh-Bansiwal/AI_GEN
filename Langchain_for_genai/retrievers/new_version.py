from dotenv import load_dotenv
load_dotenv()
from langchain_huggingface import HuggingFaceEmbeddings, HuggingFaceEndpoint, ChatHuggingFace
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# ------------------------
# LLM
# ------------------------

llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct",
    task="text-generation"
)

chat_model = ChatHuggingFace(llm=llm)

# ------------------------
# Documents
# ------------------------

documents = [
    Document(
        page_content="""
Regular exercise improves heart health, increases stamina, and reduces stress.
Python is widely used for web development, automation, data analysis,
and machine learning applications.
""",
        metadata={"source": "doc1"},
    ),
    Document(
        page_content="""
Drinking enough water keeps the body hydrated, improves digestion,
and supports healthy organs.
FAISS enables efficient similarity search over embedding vectors.
""",
        metadata={"source": "doc2"},
    ),
]

# ------------------------
# Vector Store
# ------------------------

vectorstore = FAISS.from_documents(
    documents,
    HuggingFaceEmbeddings()
)

retriever = vectorstore.as_retriever(
    search_kwargs={"k": 2}
)

# ------------------------
# Retrieve documents
# ------------------------

query = "What should I do to stay fit?"

docs = retriever.invoke(query)

# ------------------------
# Compress Context
# ------------------------

prompt = ChatPromptTemplate.from_template(
"""
You are a context compressor.

Question:
{question}

Document:
{document}

Extract ONLY the text relevant to answering the question.

If nothing is relevant, return "NONE".
"""
)

chain = prompt | chat_model | StrOutputParser()

compressed_docs = []

for doc in docs:
    result = chain.invoke({
        "question": query,
        "document": doc.page_content
    })

    if result.strip() != "NONE":
        compressed_docs.append(result)

print(compressed_docs)