from dotenv import load_dotenv
load_dotenv()
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel
llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct",
    # repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation"
)
model =ChatHuggingFace(llm=llm)
parser=StrOutputParser()
prompt1=PromptTemplate(
    template='classify the sentiment of the following feedback text into positive or negative \n {feedback}',
    input_variables=['feedback']
)
classifier_chain=prompt1 | model | parser
result=classifier_chain.invoke({'feedback':"This is a wonderful smartphone"})
print(result)