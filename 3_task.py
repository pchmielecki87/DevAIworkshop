# https://github.com/openai/openai-python
# pip3 install openai

import os
from openai import OpenAI

client = OpenAI(
    api_key='',
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Say this is a test",
        }
    ],
    model="gpt-3.5-turbo",
)