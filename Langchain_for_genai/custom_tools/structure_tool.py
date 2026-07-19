from langchain_core.tools import tool,StructuredTool
from pydantic import BaseModel,Field
class MultiplyInput(BaseModel):
    a:int=Field(required=True,description="THE FIRST NUMBER TO ADD")
    b:int=Field(required=True,description="The second number to add")
    
def multiply_fun(a: int, b: int) -> int: # its a runnable
    """Multiply two numbers."""
    return a * b

 
mutiply_tool=StructuredTool.from_function(
     
 )