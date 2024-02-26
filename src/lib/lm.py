# -----------------
# LLM
# -----------------

import os
import json
import openai

openai.api_key = os.environ['OPENAI_API_KEY']

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0)
    
    return response.choices[0].message["content"]

def parse_python_list(input_str):
    try:
        result_list = json.loads(input_str)
        if isinstance(result_list, list):
            return result_list
        else:
            raise ValueError("Input is not a valid Python list.")
    except json.JSONDecodeError as e:
        print(f"Error decoding input: {e}")
        return None
