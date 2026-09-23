from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()
deployment = "gehihi"

prompt = "Complete the following: Once upon a time there was a"
response = client.chat.completions.create(
    model=deployment,
    messages=[{"role": "user", "content": prompt}],
)
print(response.choices[0].message.content)
