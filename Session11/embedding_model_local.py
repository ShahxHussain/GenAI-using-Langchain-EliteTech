# from langchain_huggingface import HuggingFaceEmbeddings
# # import os
# # os.environ['HF_HOME'] = "E:/huggingface_cache"
# # embeddings = HuggingFaceEmbeddings(
# #     model_name = "sentence-transformers/all-MiniLM-L6-v2",
# # )


from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
load_dotenv()

embedding_model = GoogleGenerativeAIEmbeddings(
    model= "models/gemini-embedding-001"
)
text = "Pakistan is a country in Asia."
vector = embedding_model.embed_query(text)
print(str(vector))


# documents = [
#     "Pakistan is in asia",
#     "Islamabad is the capital of Pakistan",
#     "Pakistan is a democratic country",
#     "Pakistan is a nuclear power",
#     "Paris is the capital of France",
#     "Delhi is the capital of india"
# ]

# embedding = embeddings.embed_documents(documents)
# print(embedding)