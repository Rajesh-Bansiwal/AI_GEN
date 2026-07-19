from dotenv import load_dotenv
from typing import TypedDict,Annotated,Optional
load_dotenv()

class Review(TypedDict): 
    key_themes:str
    summary:str
    # sentiment:str
    # pros:str
    # cons:str
    # key_themes:Annotated[list[str],"write dowm all the key themes discussed in the review in a list"]
    # summary:Annotated[str,'Berief summary of the review']
    # sentiment:Annotated[str,'Return sentiment of the review either nrgative,positive,neutral']
    # pros:Annotated[Optional[list[str]],"write down all the pros inside a list"]
    # cros:Annotated[Optional[list[str]],"write down all the cons inside a list"]
   
    
#its not true wo daya isi hi format me de

from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace

llm = HuggingFaceEndpoint(
    # repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    # task="text-generation"
    repo_id="Qwen/Qwen2.5-7B-Instruct",
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