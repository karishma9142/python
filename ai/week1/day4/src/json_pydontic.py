import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq
from pydantic import BaseModel
import json

load_dotenv()

my_api_key=os.getenv('GROQ_API_KEY')
if not my_api_key:
    raise ValueError('api key is missing')

client = Groq(api_key=my_api_key)

model='openai/gpt-oss-120b'
role='user'

class Ticket(BaseModel):
    name:str
    email:str
    issue:str

schema = Ticket.model_json_schema()
response_format = {
    "type" : 'json_object'
} 

system_prompt = f""""
extract the prsional information from ticket strictly based on this schema and give me output in json formet.
{schema}
"""  

text = 'hello my name is karishma , i bought iphone ,which is not working at all . my address is bhopal.my email is karishma@gmail.com and mobile number is 9123436782 ,contact me'
prompt=f""""
this is customer ticket . please extract the personal information from this.
{text}
"""


system_message = {
    "role" : 'system',
    "content" : system_prompt
}
message = {
    "role" : role,
    "content" : prompt
}

messages = [system_message,message]

response = client.chat.completions.create(model=model,messages=messages,response_format=response_format)
answer = response.choices[0].message.content

row_json=answer
data_file=json.loads(row_json)
ticket=Ticket(**data_file)

print (ticket.name)
print(ticket.email)
print(ticket.issue)