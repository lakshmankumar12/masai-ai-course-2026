import os
import google.generativeai as genai
import json

# Setup
with open("keys.json", 'r') as fd:
    obj = json.load(fd)
    api_key = obj['key']

genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-flash-latest')

# Simple usage
response = model.generate_content("Explain quantum computing in 3 sentences")
print(response.text)

# Chat conversation
chat = model.start_chat(history=[])
response = chat.send_message("Hello! What can you do?")
print(response.text)
