from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite",
    max_output_tokens=1000,
)

class Person(BaseModel):
    name: str = Field(..., description="Name of the Person")
    age: int = Field(..., gt=18, description="Age of the Person")
    city: str = Field(..., description="City of the Person")

parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template = ' Generate the name, age, and city of a fictional {place} person.\n {format_instructions}',
    input_variables=["place"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)

chain = template | model | parser
result = chain.invoke({"place": "Pakistani"})

print("Result:\n", result)