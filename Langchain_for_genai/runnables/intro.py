import random

class Naklillm:
    def predict(self, prompt):
        response_list = [
            "Delhi is the capital of India",
            "IPL is a cricket league",
            "AI stands for Artificial Intelligence"
        ]
        return {"response": random.choice(response_list)}


class NakliPrompt:
    def __init__(self, template, input_variables):
        self.template = template
        self.input_variables = input_variables

    def format(self, input_dict):
        # print(input_dict)
        formatted_prompt = self.template.format(**input_dict)
        # print(formatted_prompt)
        return formatted_prompt


class Naklichain:
    def __int__(self,llm,prompt):
        self.llm=llm
        self.prompt=prompt
    def run(self,input_dict):
       final_prompt= self.prompt.format(input_dict)
       result=self.llm.predict(final_prompt)
       return result['response']
llm = Naklillm()
print(llm.predict("What is the capital of India"))

template = NakliPrompt(
    template="Write a {length} poem about {topic}",
    # template="Write a {length} poem about {topic}",
    input_variables=["length","topic"]
)
chain=Naklichain(llm,template)
chain.run({'length':'short','topic':'india'})
print(template.format({'length':"short","topic": "India"}))