from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser, StrOutputParser
from typing import Literal
from pydantic import BaseModel, Field
from langchain_core.runnables import RunnableBranch, RunnableLambda

load_dotenv()

model = ChatGoogleGenerativeAI(
    model = "gemini-2.0-flash"
)

class Feedback(BaseModel):
    sentiment: Literal['Positive', 'Negative'] = Field(description="Give the sentiment of the feedback")

parser = StrOutputParser()
parser2 = PydanticOutputParser(pydantic_object=Feedback)

prompt = PromptTemplate(
    template= "Classify the sentiment of the following feedback into Negative or Positive.\n{format_instructions}\nFeedback: {feedback}",
    input_variables=["feedback"],
    partial_variables={"format_instructions": parser2.get_format_instructions()},
)

feedback_text = """
i really enjoyed this meal
"""

classifier_chain = prompt | model | parser2


prompt2 =PromptTemplate(
    template="Write a single appropirate response to this positive feedback in a professional tone \n {feedback}",
    input_variables=['feedback']
)
prompt3 =PromptTemplate(
    template="Write a single appropirate response to this negative feedback in a professional tone \n {feedback}",
    input_variables=['feedback']
)

negative_chain = prompt3 | model | parser


# sentiment = x


branch_chain = RunnableBranch(
    (lambda x:x.sentiment == 'Positive', prompt2 | model | parser),
    (lambda x:x.sentiment == 'Negative', negative_chain),
    RunnableLambda(lambda x:x.sentiment == "Could not find a sentiment")
)

chain = classifier_chain | branch_chain
print(chain.invoke({'feedback': feedback_text}))