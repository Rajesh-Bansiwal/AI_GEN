from dotenv import load_dotenv
from typing import TypedDict,Annotated,Optional,Literal
from pydantic import BaseModel,Field
load_dotenv()

class Review(BaseModel):
    theme_keys:list[str]=Field(description="write down all the key themes discussed in the review in a list")
    summary:str=Field(description="A brief summary of the review.")
    sentiment:Literal["pos","cons"]=Field(description="Return a sentiment of the review either positive ,negative or neutral.")
    pos:Optional[list[str]]=Field(default=None,description="write down all the pros inside a list")
    
    
#its not true wo daya isi hi format me de

from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace

llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    # task="text-generation"
    # repo_id="Qwen/Qwen2.5-7B-Instruct",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)
structured_model=model.with_structured_output(Review)
result = structured_model.invoke("""
                    The Samsung Galaxy S24 is an impressive flagship smartphone that delivers a premium experience
                    in a compact design. Its vibrant AMOLED display is sharp, bright, 
                    and smooth, making it ideal for streaming, gaming, and everyday use. 
                    The powerful processor ensures fast performance, 
                    while the cameras capture detailed photos and excellent videos in various lighting conditions. 
                    Battery life comfortably lasts a full day, and fast charging adds convenience. 
                    Samsung's One UI is feature-rich, and the promise of long-term software updates makes 
                    the device a smart investment. Overall, the Galaxy S24 offers excellent performance, 
                    camera quality, and value for flagship buyers.

                      """)
# print(result)
print(result['summary'])
print(result['sentiment'])