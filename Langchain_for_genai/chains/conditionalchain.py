from dotenv import load_dotenv
load_dotenv()
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser,PydanticOutputParser
from pydantic import BaseModel,Field
from langchain_core.runnables import RunnableParallel,RunnableBranch,RunnableLambda
# runnable brach is usewd for write if else condition in this
from typing import Literal
class FeedBack(BaseModel):
    sentiment:Literal['positive','negative']=Field(description='Give the sentiment of the feedback')

llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct",
    # repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
)
model =ChatHuggingFace(llm=llm)
parser=StrOutputParser()
parser1=PydanticOutputParser(pydantic_object=FeedBack)

prompt1=PromptTemplate(
    template='classify the sentiment of the following feedback text into positive or negative {feedback} \n {format_instruction}',
    input_variables=['feedback'],
    partial_variables={'format_instruction':parser1.get_format_instructions()}
)
prompt2=PromptTemplate(
    template='write appropriate resposne to this positive feedback \n {feedback}',
    input_variables=['feedback'],
    # partial_variables={'format_instruction':parser1.get_format_instructions()}
)
prompt3=PromptTemplate(
    template='write appropriate resposne to this negative feedback \n {feedback}',
    input_variables=['feedback'],
    # partial_variables={'format_instruction':parser1.get_format_instructions()}
)
classifier_chain=prompt1 | model | parser1
brach_main=RunnableBranch((lambda x:x.sentiment == "positive",prompt2 | model | parser),
                          (lambda x:x.sentiment == "negative",prompt3 | model | parser),
                         RunnableLambda( lambda x :"could not find sentiment") # its not a chain
                          )
# result=classifier_chain.invoke({'feedback':"This is a bad smartphone"})
chain=classifier_chain | brach_main
print(chain.invoke({'feedback':"This is a bad smartphone"}))
# Rule to remember
# After the | operator → every component must be a Runnable (PromptTemplate, LLM, RunnableLambda, OutputParser, etc.).
# Inside RunnableBranch as a condition → a simple Python function or lambda is sufficient because RunnableBranch evaluates it directly.