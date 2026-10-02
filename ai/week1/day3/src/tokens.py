import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

my_api_key = os.getenv('GROQ_API_KEY')
if not my_api_key:
    raise ValueError('api key is missing')

client = Groq(api_key=my_api_key)
model='openai/gpt-oss-120b'
role='user'
prompt1 = 'hello'
prompt2 = 'explain machine learning'
prompt3 = 'write ans essay on machine learning'

prompts = [prompt1 , prompt2,prompt3]
for prompt in prompts:
    message = {
        "role" : role,
        "content" : prompt
    }
    messages=[message]
    response = client.chat.completions.create(model=model , messages=messages)
    usage=response.usage
    print(f"Prompt : {prompt} --> your tokens: {usage.prompt_tokens} completion_token: {usage.completion_tokens} total_token: {usage.total_tokens} finish_reason: {response.choices[0].finish_reason}")


    