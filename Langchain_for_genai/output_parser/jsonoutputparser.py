# json outyput from our llm 
from dotenv import load_dotenv
load_dotenv()
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct",
    # repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation"
)
parser=JsonOutputParser()
model = ChatHuggingFace(llm=llm)
tempate=PromptTemplate(template="give me 5 fatcs about {topic} \n {fromat_instruction}",
                       input_variables=['topic'],
                       partial_variables={'fromat_instruction':parser.get_format_instructions}
                       )

# prompt=tempate.format()
# print(prompt)
# result=model.invoke(prompt)
# final_result=parser.parse(result.content)
# print(final_result)
chain=tempate | model | parser
result=chain.invoke({'topic':"black hole"}) # empty bheja to error dega pasas empty dict 
print(result)
# is parse me hm schema enforce nahi kr skte 
# structre output me hm schema de skte hai