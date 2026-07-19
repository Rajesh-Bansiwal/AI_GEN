from langchain_huggingface import HuggingFacePipeline, ChatHuggingFace

llm = HuggingFacePipeline.from_model_id(
    model_id="Qwen/Qwen2.5-7B-Instruct",
    task="text-generation",
    pipeline_kwargs=dict(
        temperature=0.5,
        max_new_tokens=100,
    )
)

model = ChatHuggingFace(llm=llm)

result = model.invoke("Who is the Prime Minister of India?")

print(result.content)
# isse llm hamare ram me hi load hoga 
# apni machine pe download then run 