from dotenv import load_dotenv
load_dotenv()
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct",
    # repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)
template1=PromptTemplate(template="Generate 5 interestings fatcs about  {topic}",
                          input_variables=["topic"])
parser=StrOutputParser()
chain=template1 | model | parser
result=chain.invoke({"topic":"Gen AI"})
print(result)
chain.get_graph().print_ascii()