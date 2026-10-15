# LangChain Output Parsers

This repository contains hands-on examples of LangChain output parsers using Google Gemini. It demonstrates how to transform LLM responses into different formats that applications can process.

## What I Learned

- **JsonOutputParser** — Parses LLM responses into JSON objects.
- **PydanticOutputParser** — Validates structured data using Pydantic models and field constraints.
- **StrOutputParser** — Converts model outputs into plain text and supports chaining multiple LLM operations.
- **StructuredOutputParser** — Defines a response schema using `ResponseSchema` and parses the output into structured data.
- **LCEL (LangChain Expression Language)** — Connects prompts, models, and output parsers using the pipe (`|`) operator.

## Project Structure

```text
langchain-output-parsers/
├── json_output_parser.py
├── pydantic_output_parser.py
├── string_output_parser.py
├── structured_output_parser.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Technologies Used

- Python
- LangChain
- Google Gemini
- Pydantic
- Python-dotenv

## Setup and Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/langchain-output-parsers.git
cd langchain-output-parsers
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
```

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure your API key

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=your_google_api_key
```

**Important:** Never commit your `.env` file or expose your API key.


## 5. ▶️ Run the Examples

Run any of the four implementations:

```bash
python json_output_parser.py
python pydantic_output_parser.py
python string_output_parser.py
python structured_output_parser.py
```

## 🎯 Key Takeaway

Each output parser serves a different purpose:

| **Parser** | **Best suited for** |
|---|---|
| JsonOutputParser | Parsing LLM responses into JSON |
| PydanticOutputParser | Structured data with validation |
| StrOutputParser | Converting model responses into plain text |
| StructuredOutputParser | Parsing responses based on a defined schema |

The right parser depends on the application's output format, validation requirements, and use case.

## 📚 Learning Focus

This project is part of my learning journey in **Generative AI and AI Engineering**, focusing on LangChain output parsers, structured data, and chaining prompts, models, and parsers using LCEL.

## 👩‍💻 Author

**Javairiya Naeem**

GitHub: [JiyaSheikh06](https://github.com/JiyaSheikh06)