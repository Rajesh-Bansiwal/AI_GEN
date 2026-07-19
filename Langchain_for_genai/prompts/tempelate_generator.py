
from langchain_core.prompts import PromptTemplate


# Prompt Template
prompt = PromptTemplate(
    input_variables=["topic"],
    validate_template=True,
    template="""
You are an AI tutor.

Explain the following topic in simple words.

Topic: {topic}

Answer:
"""

)
prompt.save('tempelate.json')
