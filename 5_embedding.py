import os

from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

from boilerplate import *

load_dotenv()

TASK_NAME = 'embedding'

API_KEY = os.getenv('xxx')
OPEN_AI_API_KEY = os.getenv('xxx')

model = OpenAIEmbeddings(openai_api_key=OPEN_AI_API_KEY, model='text-embedding-ada-002')

task_token = get_token_for_task(API_KEY, TASK_NAME)

task = get_task_for_token(task_token)

embeddings = model.embed_query('Hawaiian pizza')

result = send_answer_for_token(task_token, {'answer': embeddings})
print(result)