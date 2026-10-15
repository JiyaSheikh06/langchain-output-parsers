from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite",
    max_output_tokens=1000,
)

parser = JsonOutputParser()

template = PromptTemplate(
    template="""
    Analyze the sentiment of this text: {text}
    Return the sentiment (Positive, Negative, or Neutral)
    and a short explanation.
    {format_instructions}
    """,
    input_variables=["text"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)

chain = template | model | parser
result = chain.invoke({"text": "I really enjoyed learning LangChain today! It was a great experience and I feel more confident in my skills."})

print("Result:\n", result)