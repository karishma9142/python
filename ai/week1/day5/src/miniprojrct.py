import os
from dotenv import load_dotenv
from groq import Groq
from pydantic import BaseModel
from pypdf import PdfReader

load_dotenv()

# Get API key
my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API key is missing")

# Groq client
client = Groq(api_key=my_api_key)

model = "openai/gpt-oss-120b"


# -----------------------------
# Pydantic schema
# -----------------------------

class Candidate(BaseModel):
    college: str
    cgpa: float
    stack: str
    skills: list[str]
    projects: int
    score: float


schema = Candidate.model_json_schema()


# -----------------------------
# System prompt
# -----------------------------

system_prompt = f"""
You are an HR recruiter.

Review the candidate's resume based on these requirements:

- CGPA > 7
- MERN stack 
- Skills: HTML, CSS, React, Next.js, Node.js, Express, MongoDB, SQL, Docker, Git
- At least 2 relevant projects

Give the candidate a percentage score based on how well
their resume matches these requirements.

Return only valid JSON.

Use this schema:

{schema}
"""


# -----------------------------
# Read PDF
# -----------------------------

reader = PdfReader("resume.pdf")

resume_text = ""

for page in reader.pages:
    resume_text += page.extract_text() or ""


# -----------------------------
# User prompt
# -----------------------------

prompt = f"""
This is the candidate's resume:

{resume_text}

Analyze the resume according to the requirements
given by the HR recruiter.
"""


# -----------------------------
# Messages
# -----------------------------

messages = [
    {
        "role": "system",
        "content": system_prompt
    },
    {
        "role": "user",
        "content": prompt
    }
]


# -----------------------------
# Groq API call
# -----------------------------

response = client.chat.completions.create(
    model=model,
    messages=messages,
    response_format={
        "type": "json_object"
    }
)


# -----------------------------
# Print result
# -----------------------------

answer = response.choices[0].message.content

print(answer)