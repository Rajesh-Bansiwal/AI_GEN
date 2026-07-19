from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate,load_prompt
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace

load_dotenv()

# LLM
llm = HuggingFaceEndpoint(
    # repo_id="BAAI/bge-small-en-v1.5",
    # task="text-generation",
    # max_new_tokens=100,
    # temperature=0.7
     repo_id="Qwen/Qwen2.5-7B-Instruct",
     temperature=0
    # task="text-generation",
)

model = ChatHuggingFace(llm=llm)
# 
# template load kiy ausinh template .json
template=load_prompt(r"C:\Invos_Projects\GEN_AI\AI_GEN\tempelate.json") # puri file ka path

# Prompt Template
# prompt = PromptTemplate(
#     input_variables=["topic"],
#     validate_template=True,
#     template="""
# You are an AI tutor.

# Explain the following topic in simple words.

# Topic: {topic}

# Answer:
# """

# )

# Fill the template
# formatted_prompt = prompt.format(topic="Vector Embeddings")
# formatted_prompt=prompt.invoke({
#     'topic':"what is god."
# })
# ======using template =====================
# formatted_prompt=template.invoke({
#     'topic':"what is god."
# })
#  chaining 
chain =template | model
result=chain.invoke(
    {
    'topic':"what is god."
}
)
print(result.content)
# Invoke model
# response = model.invoke(formatted_prompt)

# print(response.content)