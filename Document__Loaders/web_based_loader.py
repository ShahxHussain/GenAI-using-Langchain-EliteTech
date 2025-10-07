from langchain_community.document_loaders import WebBaseLoader


url = "https://www.cuiatd.edu.pk/"
loader = WebBaseLoader(url)
docs = loader.load()
print(docs[0].page_content)




# ---------------------------------------------------------
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


from dotenv import load_dotenv
load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
)

template = PromptTemplate(
    template="Answer the following question: {question}, from the the following text: {text}",
    input_variables=["question", "text"]
)

parser  = StrOutputParser()
chain = template | model | parser

print(chain.invoke({'question': 'Who is the director of COMSATS Abbottabad?', 'text': docs[0].page_content}))