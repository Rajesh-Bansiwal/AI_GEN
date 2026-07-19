from dotenv import load_dotenv
from typing import TypedDict,Annotated,Optional,Literal
from pydantic import BaseModel,Field
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser,PydanticOutputParser
load_dotenv()

llm = HuggingFaceEndpoint(
    # repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",

    # task="text-generation"


    repo_id="Qwen/Qwen2.5-7B-Instruct",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)
class Person(BaseModel):
    name:str=Field(description='Nmae of the person')
    age:int=Field(gt=18,description='Age of the person')
    city:str=Field(description='NMAE OD THE CITY')
    
parser=PydanticOutputParser(pydantic_object=Person)
template=PromptTemplate(
    template='Generate the name  age and city of a functional {place} person \n {format_instruction}',
    input_variables=['place'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)
chain=template | model | parser
result=chain.invoke({"place":"srilanka"})
print(result)