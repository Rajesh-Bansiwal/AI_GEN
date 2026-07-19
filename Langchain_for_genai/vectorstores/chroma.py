# light weight open source vector database that is especially friendly for local developement and small to med production needs
from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_core.documents import Document

documents = [
    Document(
        page_content="""
        Virat Kohli is one of the greatest batsmen in modern cricket.
        He has scored more than 80 international centuries and has captained
        the Indian cricket team across all formats. He is known for his
        aggressive batting style and exceptional fitness.
        """,
        metadata={"player": "Virat Kohli", "country": "India"}
    ),

    Document(
        page_content="""
        Rohit Sharma is the captain of the Indian ODI and Test cricket team.
        He is famous for his elegant batting style and holds the record for
        the highest individual score in One Day Internationals (264 runs).
        """,
        metadata={"player": "Rohit Sharma", "country": "India"}
    ),

    Document(
        page_content="""
        MS Dhoni is regarded as one of the best wicketkeeper-batsmen and
        captains in cricket history. He led India to victory in the 2007
        T20 World Cup, the 2011 Cricket World Cup, and the 2013 Champions Trophy.
        """,
        metadata={"player": "MS Dhoni", "country": "India"}
    ),

    Document(
        page_content="""
        Sachin Tendulkar is known as the 'God of Cricket'.
        He is the highest run scorer in international cricket and was the
        first player to score 100 international centuries.
        """,
        metadata={"player": "Sachin Tendulkar", "country": "India"}
    ),

    Document(
        page_content="""
        Jasprit Bumrah is one of the world's best fast bowlers.
        He is known for his unique bowling action, yorkers, and ability to
        perform under pressure in all formats of the game.
        """,
        metadata={"player": "Jasprit Bumrah", "country": "India"}
    )
]

vector_store=Chroma(
    embedding_function=HuggingFaceEmbeddings(),
    persist_directory="chroma_db",
    collection_name="sample"
)
ids=vector_store.add_documents(documents)
# vector_store.save_local("faiss_index") isse y disk me folder me store ho jayega
# print(ids)
# print(vector_store.get(include=['embeddings"','documents','metadatas']))
print(vector_store.similarity_search_with_score(query="Who among these are bowler?",k=1))
# k means kitne similar document ko dikhana chahte hai 
vector_store.similarity_search_with_score(query="",filter={"team":"chennai super kings"}) 
# y filter metadat ke base per lage hote hai 
update_doc1=Document(
    page_content="""
    Virat Kohli is a legendary Indian cricketer and one of the greatest batsmen
    in the history of cricket. He is a right-handed top-order batsman known for
    his consistency, aggressive batting, chase-master ability, and exceptional
    fitness. He has scored more than 80 international centuries and has won
    numerous ICC awards. Virat Kohli is not a bowler; his primary role in the
    team is batting.
    """,
    metadata={
        "player": "Virat Kohli",
        "country": "India",
        "role": "Batsman"
    }
)
vector_store.update_document(document_id="a6effe11-c063-4c6e-b175-0fb223374248",document=update_doc1)
print(vector_store.get(include=['documents']))
# vector_store.delete(ids=[""]) isme kitni bhi ids de skte hai 