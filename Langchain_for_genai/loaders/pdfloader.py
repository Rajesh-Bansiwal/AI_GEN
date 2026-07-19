from langchain_community.document_loaders import PyPDFLoader #used only for text data in a pdf
loader=PyPDFLoader(r"langchain/loaders/Advanced RAG - Course Outline.pdf")
docs=loader.load()
print(len(docs))