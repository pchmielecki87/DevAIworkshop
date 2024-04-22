from boilerplate import *
from dotenv import load_dotenv
import os

load_dotenv()

TASK_NAME = 'meme'

API_KEY = os.getenv('API_KEY')
RENDER_FORM_API_KEY = os.getenv('RENDER_FORM_API_KEY')
RENDER_FORM_TEMPLATE = os.getenv('RENDER_FORM_TEMPLATE')

task_token = get_token_for_task(API_KEY, TASK_NAME)
task = get_task_for_token(task_token)
print(task)

image = task['image']
text = task['text']

generated_image = requests.post(f"https://api.renderform.io/api/v2/render",
                                headers={
                                    'X-API-KEY': RENDER_FORM_API_KEY,
                                },
                                json={
                                    "template": RENDER_FORM_TEMPLATE,
                                    "data": {
                                        "image.src": image,
                                        "title.text": text
                                    }
                                })
print(generated_image.json())
href = generated_image.json()['href']

result = send_answer_for_token(task_token, {"answer": href})
print(result)