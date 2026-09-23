from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()
deployment = "gehihi"

no_recipes = input("No of recipes (for example, 5): ")
ingredients = input("List of ingredients (for example, chicken, potatoes, and carrots): ")
filter_cond = input("Filter (for example, vegetarian, vegan, or gluten-free): ")

prompt = f"Show me {no_recipes} recipes for a dish with the following ingredients: {ingredients}. Per recipe, list all the ingredients used, no {filter_cond}: "

response = client.chat.completions.create(
    model=deployment, 
    messages=[{"role": "user", "content": prompt}], 
    max_tokens=600
)

print("Recipes:")
old_prompt_result = response.choices[0].message.content
if not old_prompt_result:
    print("No response received.")
else:
    print(old_prompt_result)

    prompt_shopping = "Produce a shopping list, and please don't include ingredients that I already have at home: "
    new_prompt = f"Given ingredients at home {ingredients} and these generated recipes: {old_prompt_result}, {prompt_shopping}"
    
    response2 = client.chat.completions.create(
        model=deployment, 
        messages=[{"role": "user", "content": new_prompt}], 
        max_tokens=600
    )

    print("=====Shopping list ======= ")
    if response2.choices[0].message.content:
        print(response2.choices[0].message.content)
