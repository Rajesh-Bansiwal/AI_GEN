from dotenv import load_dotenv
from typing import TypedDict,Annotated,Optional,Literal
from pydantic import BaseModel,Field
load_dotenv()

mob_json={
  "title": "Samsung Galaxy S24 Review",
  "description": "Structured schema for analyzing a Samsung Galaxy S24 review",
  "type": "object",
  "properties": {
    "summary": {
      "type": "string",
      "description": "A brief summary of the review"
    },
    "sentiment": {
      "type": "string",
      "enum": ["positive", "negative", "neutral"],
      "description": "Overall sentiment of the review"
    },
    "key_themes": {
      "type": "array",
      "description": "Main topics discussed in the review",
      "items": {
        "type": "string"
      }
    },
    "pros": {
      "type": "array",
      "description": "Advantages mentioned in the review",
      "items": {
        "type": "string"
      }
    },
    "cons": {
      "type": "array",
      "description": "Disadvantages mentioned in the review",
      "items": {
        "type": "string"
      }
    },
    "rating": {
      "type": "number",
      "description": "Overall rating out of 5"
    }
  },
  "required": [
    "summary",
    "sentiment",
    "key_themes",
    "pros",
    "cons",
    "rating"
  ]
}
#its not true wo daya isi hi format me de

from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace

llm = HuggingFaceEndpoint(
    # repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    # task="text-generation"
    repo_id="Qwen/Qwen2.5-7B-Instruct",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)
structured_model=model.with_structured_output(mob_json)
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
print(result)
# print(result['summary'])
# print(result['sentiment'])