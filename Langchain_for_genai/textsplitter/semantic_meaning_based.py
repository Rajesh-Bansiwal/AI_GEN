# use sliding window approach for check sementic meaning are same or not based on vector 
from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv
from langchain_experimental.text_splitter import SemanticChunker
text_splitter=SemanticChunker(
    HuggingFaceEmbeddings(),breakpoint_threshold_type="standard_deviation",
    breakpoint_threshold_amount=1
)
text="""
Farmers are the backbone of a nation because they grow crops and produce food that sustains people every day. 
They work tirelessly in fields through different seasons, facing challenges like unpredictable weather, pests, and water shortages. 
Cricket, on the other hand, is one of the most popular sports, bringing people together through teamwork, skill, and sportsmanship. 
Just as farmers contribute to the country's food security, cricketers inspire millions with their dedication, discipline, and perseverance.
Both farming and cricket require patience, hard work, and determination to achieve success, making them equally valuable to society.

"""
docs=text_splitter.create_documents([text])
print(docs)