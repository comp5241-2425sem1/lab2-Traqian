import requests
import json
import os
import toml
import streamlit as st

# Load API key from credentials.txt
file_path = 'credentials'
if os.path.exists(file_path):
    with open(file_path, 'r') as f:
        secrets = toml.load(f)
else:
    secrets = st.secrets

OPENROUTER_API_KEY = secrets['OPENROUTER']["OPENROUTER_API_KEY"]

def answer(system_prompt, user_prompt):
    msg = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]

    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={"Authorization": f"Bearer {OPENROUTER_API_KEY}"},
        data=json.dumps({
            "messages": msg,
            "model": "openai/gpt-4o-mini-2024-07-18"
        })
    )

    # Check if 'choices' key exists in the response JSON
    response_json = response.json()
    if 'choices' in response_json:
        resp = response_json['choices'][0]['message']['content']
    else:
        resp = "Error: 'choices' key not found in the response."

    return resp