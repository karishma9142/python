import os
from pathlib import Path
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

my_api_key = os.getenv('GROQ_API_KEY')
if not my_api_key:
    raise ValueError('api key is missing')

client = Groq(api_key=my_api_key)

model='openai/gpt-oss-120b'

def llm_ans(prompt):
    message = {
        "role" : "user",
        "content" : prompt
    }

    messages=[message]
    response=client.chat.completions.create(model=model,messages=messages)
    answer = response.choices[0].message.content
    return answer

bad_prompt = """"
this is a user complaints: 
my laptop is not working 
classify this
"""

good_prompt = """"
#ROLE
You are a support assistant at a mobile/laptop company

#TASK
you have to classify the issue in catagory

#CONSTRAINT
you have to classify the issue in one of the three catagorise namely billing,technical,return
Do NOT create any new category.
Do NOT use words like mechanical, hardware, software, etc.

#OUTPUT FORMAT
your answer should be in one word only . the one word should be in one of the catagory given in constraint

#EXAMPLE
for instance if a user complain says he wants a refund then the catagory is return

#FALLBACK
if the issue is unrelated to any of the catagory mentioned in constraints , then the answer should be other

this is a user complaints :
 
"""

print(llm_ans(good_prompt))