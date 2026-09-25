import os
import requests
import json

url = "http://localhost:20128/v1/embeddings"
headers = {
    "Authorization": "Bearer sk-45245fa5a3b0a8f8-rrjkfm-9ecb8a7d",
    "Content-Type": "application/json"
}

def test_embed(input_data, model):
    payload = {
        "input": input_data,
        "model": model
    }
    r = requests.post(url, headers=headers, json=payload)
    print(f"Model: {model}, Input Type: {type(input_data).__name__} -> Status: {r.status_code}")
    if r.status_code != 200:
        print(f"Error: {r.text}")

print("Testing with text-embedding-ada-002...")
test_embed(["hello"], "text-embedding-ada-002")
test_embed("hello", "text-embedding-ada-002")

print("\nTesting with gehihi...")
test_embed(["hello"], "gehihi")
test_embed("hello", "gehihi")
