from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()
deployment = "gehihi"

user_input = input("Ask a question: ")

response = client.chat.completions.create(
    model=deployment,
    messages=[
        {"role": "system", "content": "You are a helpful history bot."},
        {"role": "user", "content": user_input}
    ],
    max_tokens=600
)

print(response.choices[0].message.content)
