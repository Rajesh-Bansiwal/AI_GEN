# maximum marginal relevance
# mmr is an information retrievel algo desinged to reduce redundaNCY IN THE RETRIEVED RESULTS WHILE MAINATAINING HIGH RELEVANCE TO THE QUERY
# PICK MOST RELEVEBNT DOVU FIRST THEN SECOND AT LEAT SIMILAR phir usse milte hue dega
from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_community.vectorstores import FAISS
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
vector_stor=FAISS.from_documents(
    documents=documents,
    embedding=HuggingFaceEmbeddings()
)
retrever=vector_stor.as_retriever(
    search_type="mmr",
    search_kwargs={"k":3,"lambda_mult":0.5} # 1 toh y normal similart search ki tarah work karega
    # iski value hame 0 se 1 kle bitch rakhni hogi
    # o set jayada diverce and dega
)
query="what i do using lamchain?"                   
result=retrever.invoke(query)
for i,doc in enumerate(result):
    print(f"\n--- Result{i+1} ---")
    print(f"Content:\n{doc.page_content}....")