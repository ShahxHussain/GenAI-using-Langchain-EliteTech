from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

# Model initialized
model = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
)
# 1st prompt: Learning Content
template1 = PromptTemplate(
    template="Provide a detailed learning note on {topic} in simple language for students.",
    input_variables=['topic']
)

template2 = PromptTemplate(
    template = "Based on the above content, create 5 multiple-choice questions with 4 options each. \
Only 1 option should be correct. Highlight the correct answer.\n\n{text}",
    input_variables=['text']
)

parser = StrOutputParser()

content_chain = template1 | model | parser
content = content_chain.invoke({'topic': 'Pakistan'})

quiz_chain = template2 | model | parser
quiz = quiz_chain.invoke({'text': content})

print(content)
print(quiz)