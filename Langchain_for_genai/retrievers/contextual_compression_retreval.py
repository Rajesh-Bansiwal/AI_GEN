from dotenv import load_dotenv
load_dotenv()

from langchain_core.documents import Document
from langchain_huggingface import (
    HuggingFaceEmbeddings,
    HuggingFaceEndpoint,
    ChatHuggingFace,
)
from langchain_community.vectorstores import FAISS

from langchain.retrievers import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import LLMChainExtractor


# ----------------------------
# LLM
# ----------------------------

llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct",
    task="text-generation",
)

chat_model = ChatHuggingFace(llm=llm)


# ----------------------------
# Documents
# ----------------------------

documents = [
    Document(
        page_content="""
Regular exercise improves heart health, increases stamina, and reduces stress.
Python is widely used for web development, automation,
data analysis, and machine learning applications.
""",
        metadata={"source": "doc1"},
    ),

    Document(
        page_content="""
A balanced diet rich in fruits and vegetables strengthens immunity.
React builds fast user interfaces using reusable components,
hooks, and the virtual DOM.
""",
        metadata={"source": "doc2"},
    ),

    Document(
        page_content="""
Drinking enough water keeps the body hydrated and supports healthy organs.
FAISS enables efficient similarity search over embedding vectors.
""",
        metadata={"source": "doc3"},
    ),

    Document(
        page_content="""
Getting quality sleep improves memory and concentration.
LangChain helps developers build LLM applications
using prompts, retrievers, vector stores, and tools.
""",
        metadata={"source": "doc4"},
    ),

    Document(
        page_content="""
Walking daily improves cardiovascular fitness and reduces anxiety.
Docker packages applications into portable containers.
""",
        metadata={"source": "doc5"},
    ),
]


# ----------------------------
# Embeddings
# ----------------------------

embeddings = HuggingFaceEmbeddings()


# ----------------------------
# Vector Store
# ----------------------------

vector_store = FAISS.from_documents(
    documents,
    embeddings
)


# ----------------------------
# Base Retriever
# ----------------------------

base_retriever = vector_store.as_retriever(
    search_kwargs={"k": 5}
)


# ----------------------------
# Context Compressor
# ----------------------------

compressor = LLMChainExtractor.from_llm(chat_model)

compression_retriever = ContextualCompressionRetriever(
    base_retriever=base_retriever,
    base_compressor=compressor,
)


# ----------------------------
# Query
# ----------------------------

query = "What is photosynthesis?"

compressed_docs = compression_retriever.invoke(query)


# ----------------------------
# Output
# ----------------------------

print("=" * 60)

for i, doc in enumerate(compressed_docs, 1):
    print(f"\nDocument {i}")
    print(doc.page_content)
    print(doc.metadata)