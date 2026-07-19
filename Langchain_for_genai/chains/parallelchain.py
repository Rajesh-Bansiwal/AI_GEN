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
llm1 = HuggingFaceEndpoint(
#    model="gemini-2.5-pro",
#     temper
   repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation"
)
model1=ChatHuggingFace(llm=llm1)
model2 = ChatHuggingFace(llm=llm)
prompt1=PromptTemplate(template='Generate short and simple notes from the following text \n {text}',
                       input_variables=['text'])
prompt2=PromptTemplate(template="Genearte 5 short questions answers from the following text \n {text}",
                       input_variables=['text'])
prompt3=PromptTemplate(template="Merge the provided notes and quiz into a single document \n notes -> {notes} and {quiz}",
                       input_variables=['notes','quiz'])
parser=StrOutputParser()
paralle_chain=RunnableParallel({
    'notes':prompt1 | model1 | parser,
    'quiz':prompt2 | model2 |  parser
    
    })
merge_chain=prompt3 | model1 | parser
chain = paralle_chain | merge_chain
text="""
**Linear Regression** is a supervised machine learning algorithm used to predict continuous numerical values, such as house prices, 
salaries, or sales. It establishes a linear relationship between one or more 
independent variables (features) and a dependent variable (target). 
The objective of linear regression is to find the best-fit line that minimizes the difference between the predicted and actual values, 
usually by minimizing the Mean Squared Error (MSE). In simple linear regression, the relationship is represented by the equation **y = mx + c**, where **m** is 
the slope and **c** is the intercept. For multiple input features, multiple linear regression is used. The model is easy to understand, 
computationally efficient, and highly interpretable. Its performance is commonly evaluated using metrics such as 
**R² Score, MAE, MSE, and RMSE**. Linear regression works well when the relationship between variables is linear,
but it may not perform effectively for complex non-linear data.

"""
result=chain.invoke({"text":text})

print(result)