import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq
import numpy as np
from sentence_transformers import SentenceTransformer
import sys

model = SentenceTransformer("all-MiniLM-L6-v2")

load_dotenv()

my_api_key = os.getenv('GROQ_API_KEY')
if not my_api_key:
    raise ValueError('api key is missing')

client = Groq(api_key = my_api_key)
groqModel = 'openai/gpt-oss-120b'

documents = [
    "Employees receive 24 days of paid leave per year.",
   
    "Employees work from the office on Tuesday, Wednesday and Thursday. "
    "Monday and Friday are optional work-from-home days.",
   
    "Employees receive Rs 3000 per month for gym reimbursement.",
   
    "Employees can claim Rs 2000 per month for home internet.",
   
    "Employees have a 90 day notice period."
]

document_embeddings = model.encode(documents)

print(sys.getsizeof(document_embeddings))

# embeding
def cosine_similarity(a,b):
    return np.dot(a,b)/(
        np.linalg.norm(a)*np.linalg.norm(b)
    )

# retrival

def retrieve(qembedding):
    scores = []  # 0.4 
    for i, document in  enumerate(document_embeddings):
        score=cosine_similarity(qembedding,document )
        scores.append((score,documents[i]))
    scores.sort(reverse=True)
    return scores[0]  #line#0.9
 

def ask_llm(context , query):
    sys_prompt=f"""answer in one line only. Answer only based on this context. 
    do not hallucinate. Context: {context}"""

    messages = [
        {
            "role" : "system",
            "content" : sys_prompt
        },{
            "role" : "user",
            "content" : query
        }
    ]

    response = client.chat.completions.create(model=groqModel,messages=messages)
    answer = response.choices[0].message.content
    return answer

query = "How much vacation do I get?"
qembedding = model.encode(query)
dembedding = model.encode(documents)
score,context = retrieve(qembedding)
answer=ask_llm(context,query)
print(answer)
    