from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser

load_dotenv()

# Model initialized
model = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
)

parser = JsonOutputParser()

# country name: area , religion, capital
template = PromptTemplate(
    template = "Give me the are, major religion and capital of the {country} \n {format_instructions}",
    input_variables=['country'],
    partial_variables= {'format_instructions': parser.get_format_instructions()}
)

chain = template | model | parser
result = chain.invoke({'country': 'Pakistan'})
print(result)

