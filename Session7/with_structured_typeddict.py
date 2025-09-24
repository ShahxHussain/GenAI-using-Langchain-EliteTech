from typing import TypedDict, Annotated, Literal, Optional
from langchain_google_genai import ChatGoogleGenerativeAI

from dotenv import load_dotenv
load_dotenv()

# Model initialized
model = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
)

class Review(TypedDict):
    summary: Annotated[str, "Provide a summary of this review"]
    sentiment : Annotated[Literal["P+", "N-", "Neutral"], "Return Sentiment fo the review"]
    name : Annotated[Optional[str], "Return name of the reviewer"]

structured_model = model.with_structured_output(Review)

result = structured_model.invoke("""NUST is truly one of the leading universities in Pakistan, offering a world-class learning environment with a blend of academic excellence, innovation, and personal growth. The institution stands out for its strong focus on quality education, research, and producing graduates who are not just skilled professionals but also responsible global citizens.
One of the most impressive aspects of NUST is its diverse range of programs in engineering, computer science, management, natural sciences, social sciences, and architecture. The curriculum is designed to keep pace with international standards, ensuring that students are prepared to meet the evolving demands of industry and academia.
The faculty at NUST is highly qualified, supportive, and deeply committed to student success. Many professors bring global exposure and practical expertise into their teaching, which bridges the gap between theory and real-world applications.
The campus life is vibrant and enriching. With state-of-the-art facilities, modern labs, libraries, and collaborative spaces, NUST provides an environment that nurtures creativity and innovation. Beyond academics, the university encourages students to take part in societies, competitions, and extracurricular activities that help in building leadership, teamwork, and communication skills.
Reviewed by ChatGPT
""")

print(result)

