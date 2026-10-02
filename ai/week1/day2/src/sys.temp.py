import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

my_api_key = os.getenv('GROQ_API_KEY')

if not my_api_key:
    raise ValueError('api key is missing')

client = Groq(api_key=my_api_key)
model = "openai/gpt-oss-120b"
role = 'user'
prompt = 'suggest a name for my food compnay'

message_system = {
    "role" : "system",
    "content" : "you are a brand manager who suggest name for my food company . name should be in one word. suggest one name only"
    # "content" : 'i prefer modern'
}
message = {
    "role" : role,
    "content" : prompt
}

messages = [message_system ,message]

response = client.chat.completions.create(model=model , messages=messages,temperature=1)
print(response.choices[0].message.content)