# text plit in like 100 charatcer chunk
# drawbach like kuch meaningfull dena hai toh wo to chunks 
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader #used only for text data in a pdf
loader=PyPDFLoader(r"langchain/loaders/Advanced RAG - Course Outline.pdf")
docs=loader.load()
splitter=CharacterTextSplitter(chunk_size=100,chunk_overlap=0,separator='')
result=splitter.split_documents(docs)
# splitter.split_text()
print(result[0].page_content)
# chunk overlap y batat hai 2 chunks ke bich kitna chunk overlap hai 
# used for context retain 100 ka chunk to 10 - 20 % overlap ho
