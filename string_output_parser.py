from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite",
    max_output_tokens=1000,
)

# 1st Prompt -> Detailed Report
template1 = PromptTemplate(
    input_variables=["topic"],
    template='Write a detailed report on {topic}. Include the following sections: Introduction, Background, Methodology, Results, Discussion, Conclusion. Use clear and concise language, and provide relevant examples and references where appropriate.'
)


# 2nd Prompt -> Summary of the report
template2 = PromptTemplate(
    input_variables=["text"],
    template='Write the 5 line summary on the following text: {text}'
)

parser = StrOutputParser()

chain = template1 | model | parser | template2 | model | parser

result = chain.invoke({"topic": "The impact of climate change on global agriculture"})
print("\nSummary:\n", result)