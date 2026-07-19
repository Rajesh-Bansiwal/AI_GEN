from langchain_community.document_loaders import PyPDFLoader,DirectoryLoader #used only for text data in a pdf
loader=DirectoryLoader(path="",
                       glob="*.pdf",
                       loader_cls=PyPDFLoader)
docs=loader.load()
# docs=loader.lazy_load() load kiya phit remove kiya
print(len(docs))
# lazy loading if load 1000s of document 1 bar me ek hio document load hota haiu uske sath jo kaam kiya phir agla on demand load return generator of document objects
# list na milke generator object milta hai uske upeer loop chla ke perocessing krte hai 
for document in docs:
    print(document.metadat)