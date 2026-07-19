# multi query rereiver y user ki query se ambiquity ko khtm krne ki kosis krta hai
# ek query se 5 quuery genertqe kiya llm ne 
# how i stay healthy 
# query sahi se explain nahi hui toh khud uske regharding queries generate krta hai 
from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain.retrievers.multi_query import MultiQueryRetriever
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.documents import Document
llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct",
    task="text-generation"
)
documents = [
    # Health Documents
    Document(
        page_content="Regular exercise improves heart health boosts energy reduces stress strengthens immunity daily.",
        metadata={"source": "h1"}
    ),
    Document(
        page_content="Eating fresh fruits vegetables provides vitamins minerals fiber antioxidants supporting healthy living.",
        metadata={"source": "h2"}
    ),
    Document(
        page_content="Drinking enough water keeps body hydrated supports digestion improves concentration every day.",
        metadata={"source": "h3"}
    ),
    Document(
        page_content="Getting quality sleep improves memory mood recovery immune function overall wellness consistently.",
        metadata={"source": "h4"}
    ),
    Document(
        page_content="Routine medical checkups detect diseases early improving treatment success and long-term health.",
        metadata={"source": "h5"}
    ),

    # Random Documents
    Document(
        page_content="Artificial intelligence transforms industries automating tasks improving efficiency enabling innovative solutions worldwide.",
        metadata={"source": "r1"}
    ),
    Document(
        page_content="Mountains offer breathtaking landscapes attracting hikers photographers nature lovers throughout every season.",
        metadata={"source": "r2"}
    ),
    Document(
        page_content="Reading books expands knowledge enhances creativity improves vocabulary and critical thinking skills.",
        metadata={"source": "r3"}
    ),
]
vector_store=FAISS.from_documents(documents=documents,embedding=HuggingFaceEmbeddings())
similarity_retrever=vector_store.as_retriever(searh_type="similarity",search_kwargs={"k":5})
multiquery_retriever=MultiQueryRetriever.from_llm(
    retriever=vector_store.as_retriever(search_kwargs={"k":5}),llm=ChatHuggingFace(llm=llm)
)
query="How to improve book study level?"
similarity_results=similarity_retrever.invoke(query)
mutltiquery_result=multiquery_retriever.invoke(query)
print("============================== result frosimilarity ===================================")
for i,doc in enumerate(similarity_results):
    print(f"\n--- Result {i+1} ---")
    print(f"Content:\n{doc.page_content}....")
    
print("============================result from multi_similarity================================")    
for i,doc in enumerate(mutltiquery_result):
    print(f"\n--- Result{i+1} ---")
    print(f"Content:\n{doc.page_content}....")    