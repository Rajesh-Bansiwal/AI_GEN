# wikipedia retriever wikipedia ke api pe hit krke puchta hai query matching ke according to match krti hai usko lake deat hai 
from langchain_community.retrievers import WikipediaRetriever
retrever=WikipediaRetriever(top_k_results=2,lang="en")
query="what about ukrain and russia war?"
docs=retrever.invoke(query)
# print(docs)  
for i,doc in enumerate(docs):
    print(f"\n--- Result{i+1} ---")
    print(f"Content:\n{doc.page_content}....")
    
# retrievr ek search engine ki tarah kaam kr raha hai relevent document konse hai based on query
# retrieveris a runnable function
