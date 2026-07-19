import random
from abc import ABC,abstractmethod
class Runnable(ABC):
    @abstractmethod
    def invoke(input_data):
        pass

class Naklillm(Runnable):
    def predict(self, prompt):
        response_list = [
            "Delhi is the capital of India",
            "IPL is a cricket league",
            "AI stands for Artificial Intelligence"
        ]
        return {"response": random.choice(response_list)}
    def invoke(self,prompt):
        response_list = [
            "Delhi is the capital of India",
            "IPL is a cricket league",
            "AI stands for Artificial Intelligence"
        ]
        return {"response": random.choice(response_list)}
        

class NakliPrompt(Runnable):
    def __init__(self, template, input_variables):
        self.template = template
        self.input_variables = input_variables
    def invoke(self,input_dict):
        formatted_prompt = self.template.format(**input_dict)
        # print(formatted_prompt)
        return formatted_prompt
            

    def format(self, input_dict):
        # print(input_dict)
        formatted_prompt = self.template.format(**input_dict)
        # print(formatted_prompt)
        return formatted_prompt

class RunnableConnector(Runnable):
    def __init__(self,runnable_list):
        self.runnable_list=runnable_list
    
    def invoke(self,input_data):
        for runnable in self.runnable_list:
            input_data=runnable.invoke(input_data)
            
        return input_data    
        