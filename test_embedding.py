import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

try:
    client.embeddings.create(input=["the quick brown fox jumped over the lazy dog"], model="text-embedding-ada-002")
except Exception as e:
    print(f"ERROR_1: {type(e).__name__} - {str(e)}")

try:
    client.embeddings.create(input="the quick brown fox jumped over the lazy dog", model="text-embedding-ada-002")
except Exception as e:
    print(f"ERROR_2: {type(e).__name__} - {str(e)}")
