from langchain_community.document_loaders import CSVLoader
loader=CSVLoader(file_path="")
docs=loader.load()
print(docs[0]) # print data in rows