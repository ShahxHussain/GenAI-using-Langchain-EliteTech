from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from dotenv import load_dotenv

load_dotenv()

# import os
# os.environ['HF_HOME'] = "E:/huggingface_cache"

llm = HuggingFacePipeline.from_model_id(
    model_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task = "text-generation",
    
)

model = ChatHuggingFace(llm=llm)

result = model.invoke("Who is the founder of Paksitan")
print(result.content)