# a vector store retrever in langchain is the mpost common tye of retiver rhat lets you search and fetch documents 
# from a vector store based on semantic similarity using vector embeddings
# how to use 
# 1 store docs on vector store like chroma 
# each docs convert into dense vector using embeding models 
# phit wo query se match krte hai or us query ka bhi vectgor bnate hai 
from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_core.documents import Document

documents = [
    Document(
        page_content="""
LangChain builds intelligent AI applications.
Chains connect multiple language models.
Prompts guide model behavior effectively.
Retrievers fetch relevant information quickly.
Agents automate complex reasoning tasks.
""",
        metadata={"topic": "Introduction"}
    ),

    Document(
        page_content="""
Document loaders import external data.
PDF loaders extract document content.
Web loaders collect website information.
Text splitters create smaller chunks.
Chunks improve retrieval performance significantly.
""",
        metadata={"topic": "Document Loaders"}
    ),

    Document(
        page_content="""
Embeddings represent text numerically.
Chroma stores embedding vectors efficiently.
FAISS enables similarity searching.
Semantic search finds related documents.
Vector databases improve retrieval accuracy.
""",
        metadata={"topic": "Embeddings"}
    ),

    Document(
        page_content="""
Prompt templates create dynamic prompts.
LCEL simplifies workflow creation.
Output parsers structure responses.
Runnables execute processing pipelines.
Chains improve application readability.
""",
        metadata={"topic": "LCEL"}
    ),

    Document(
        page_content="""
Agents select appropriate tools.
Memory preserves conversation history.
Wikipedia provides external knowledge.
RAG combines retrieval generation.
LangChain powers modern chatbots.
""",
        metadata={"topic": "Agents"}
    )
]

vector_store=Chroma.from_documents(
    documents=documents,
    embedding=HuggingFaceEmbeddings(),
    collection_name="my_collection"
)
retrever=vector_store.as_retriever(search_kwarg={"k":2})
query="what is chroma used for?"
result=retrever.invoke(query)
for i,doc in enumerate(result):
    print(f"\n--- Result{i+1} ---")
    print(f"Content:\n{doc.page_content}....")
    
# is kaam ko toh hm vector store se bhi kr skte hai toh y kyu
    