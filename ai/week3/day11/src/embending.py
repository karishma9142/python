import os
from pathlib import Path
from groq import Groq
from dotenv import load_dotenv
import numpy as np
from sentence_transformers import SentenceTransformer


def cosine_similarity(a,b):
    return np.dot(a,b)/(
        np.linalg.norm(a) * np.linalg.norm(b)
    )


model = SentenceTransformer("all-MiniLM-L6-v2")
# SentenceTransformer("all-MiniLM-L6-v2") loads a model used to convert sentences into 
# meaningful numerical vectors (embeddings).

text = 'Machine learning is fun.'

t1="There are 24 paid leaves"
t2="cat is a wild animal"

v1=model.encode(t1)
v2=model.encode(t2)
print(cosine_similarity(v1, v2))