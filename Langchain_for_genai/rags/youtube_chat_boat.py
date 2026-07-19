from dotenv import load_dotenv
load_dotenv()
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace,HuggingFaceEmbeddings
from langchain_core.prompts import PromptTemplate
from youtube_transcript_api import YouTubeTranscriptApi,TranscriptsDisabled
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter, Language
from langchain_core.runnables import RunnableSequence,RunnableParallel,RunnablePassthrough,RunnableLambda
from langchain_core.output_parsers import StrOutputParser
video_id = "_6R7Ym6Vy_I"
llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct",
    # repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
)
model =ChatHuggingFace(llm=llm)
try:
    transcript_list=YouTubeTranscriptApi().fetch(
    "_6R7Ym6Vy_I",
    languages=["en"]
)
    # transcript=" ".join({"text":chunk.text,"duration":chunk.duration,"start":chunk.start for chunk in transcript_list})
    transcript =  " ".join(chunk.text for chunk in transcript_list)
#     [
#     {
#         "text": chunk.text,
#         "duration": chunk.duration,
#         "start": chunk.start
#     }
#     for chunk in transcript_list
# ]
    # print(transcript)
except TranscriptsDisabled:
    print("No caption available for this video.")    
    
splitter = RecursiveCharacterTextSplitter(
    # language=Language.PYTHON,
    chunk_size=1000,
    chunk_overlap=200,
)
chunks=splitter.create_documents([transcript])
prompt = PromptTemplate.from_template("""
Context:
{context}

Question:
{question}

Answer:
""",
)
# print(len(chunks))
# embeddings=H
vector_store=FAISS.from_documents(chunks,HuggingFaceEmbeddings())
retriever=vector_store.as_retriever(search_type="similarity",search_kwargs={"k":4}) # "k":4c4 similart vector nikal kr dega
# print(vector_store.index_to_docstore_id)
# print(retriever.invoke("what is gen ai and how its used inb real world?"))
question="is the question of gen ai discussed in this video? if yes then what was discussed"
# ==================using chain =================
def format_text(retrieved_docs):
    context="\n\n".join(doc.page_content for doc in retrieved_docs)
    return context

paralle_chain=RunnableParallel({
    "context":retriever | RunnableLambda(format_text),
    "question":RunnablePassthrough()
})
    
# chain=paralle_chain.invoke(question)
main_chain=paralle_chain | prompt | model | StrOutputParser()

print(main_chain.invoke("Can you summarize the video."))

# ================using manually not chain================
# docs=retriever.invoke(question)
# # print(docs)
# prompt=PromptTemplate()

# context="\n\n".join(doc.page_content for doc in docs)
# final_prompt=prompt.invoke({"content":context,"question":question})
# answer=model.invoke(final_prompt)
# print(answer)
# # chain = prompt | model 

# # compressed_docs = []

# # for doc in docs:
# #     result = chain.invoke({
# #         "question": query,
# #         "document": doc.page_content
# #     })

# #     if result.strip() != "NONE":
# #         compressed_docs.append(result)

# # print(compressed_docs)