from langchain_core.tools import tool

@tool
def multiply(a: int, b: int) -> int: # its a runnable
    """Multiply two numbers."""
    return a * b


def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b

result=multiply.invoke({"a":3,"b":4})
print(result)
print(multiply.args,multiply.description,multiply.name)
print(multiply.args_schema.model_json_schema()) #llm ko y dikhta hai tool ka schema