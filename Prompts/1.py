# Imports 
from langchain_google_genai import ChatGoogleGenerativeAI


# laod API
from dotenv import load_dotenv
load_dotenv()

# Model initialized
model = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
)

# Ai powered Researcher
# paper Name
# Explanation Type : Beginner, Technical, Methematical 
# explanation Length
paper_name = input("Enter a paper Name ")
explanation_type = input("Enter a explanation Type i.e Beginner, Technical, Methematical")
explanation_length =  input ("Enter a explanation Length i.e Short, Medium, Long")



# A simple variable to store the prompts
prompt = """
Explain the research Paper titled {paper_name},
Explanation Type {explanation_type},
Explanation Length {explanation_length}
"""

# Invoke model
result = model.invoke(prompt)
print(result.content)
