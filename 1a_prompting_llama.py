r"""


@author: arjun.krishna4706@gmail.com
"""
from ollama import Client
import os

ref_file = "Lakers"
downloads_folder = os.path.join(os.getcwd(), "download")
html_path = os.path.join(downloads_folder, ref_file + ".html")

# Read the HTML file
with open(html_path, "r", encoding="utf-8") as f:
    html_content = f.read()

# Read the prompt from the txt file
prompt_path = os.path.join(os.getcwd(), "input", "prompt.txt")
with open(prompt_path, "r", encoding="utf-8") as f:
    user_prompt = f.read()

client = Client()

# Start conversation history
messages = [
    {'role': 'user', 'content': user_prompt + "\n\n" + html_content[:4000]}
]

# First response
response = client.chat(
    model='llama3.1',
    messages=messages
)
print(response['message']['content'])

# Save the final response to a file
output_path = os.path.join(os.getcwd(), "llama_response.txt")
with open(output_path, "w", encoding="utf-8") as out_file:
    out_file.write(response['message']['content']) 