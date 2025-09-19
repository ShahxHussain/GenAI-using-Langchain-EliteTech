from langchain_google_genai import ChatGoogleGenerativeAI

from dotenv import load_dotenv
load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
)

query = input("Enter your query")

result = model.invoke(query)

print(result.content)
