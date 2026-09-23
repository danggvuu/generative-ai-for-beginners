import tiktoken
text= f"""
Jupiter is the fifth planet from the Sun and the \
largest in the Solar System. It is a gas giant with \
a mass one-thousandth that of the Sun, but two-and-a-half \
times that of all the other planets in the Solar System combined. \
Jupiter is one of the brightest objects visible to the naked eye \
in the night sky, and has been known to ancient civilizations since \
before recorded history. It is named after the Roman god Jupiter.[19] \
When viewed from Earth, Jupiter can be bright enough for its reflected \
light to cast visible shadows,[20] and is on average the third-brightest \
natural object in the night sky after the Moon and Venus.
"""

encoding = tiktoken.encoding_for_model('gpt-4o')
tokens=encoding.encode(text)
print(tokens)
for i in tokens:
    print(encoding.decode_single_token_bytes(i))

import os 
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
deployment="gehihi"

def get_completion(prompt):
    response = client.chat.completions.create(
        model=deployment,
        messages=[{"role": "user", "content": prompt}], # SỬA MỖI DÒNG NÀY THÔI NHÉ
        max_tokens=1024,
    )
    return response.choices[0].message.content

## ---------- Call the helper method

### 1. Set primary content or prompt text
text = f"""
oh say can you see
"""

### 2. Use that in the prompt template below
prompt = f"""
```{text}```
"""

## 3. Run the prompt
response = get_completion(prompt)
print(response)
