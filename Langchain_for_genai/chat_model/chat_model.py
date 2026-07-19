from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()
model=ChatOpenAI(model='gpt-5.4',temperature=1.5) #0 for like code or 1.5 some craetiveness
result=model.invoke("what is the capitla of india")
print(result.content)