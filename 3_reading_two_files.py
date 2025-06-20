r"""
 __         __
/  \.-'''-./  \
\    -   -    /
 |   o   o   |
 \  .-'''-.  /
  '-\__Y__/-'
     `---`

@author: SR
"""
from ollama import Client
import os

# --- CONFIG ---
ref_file1 = "Lakers"    # first file name (without .html)
ref_file2 = "Lakers1"  # second file name (without .html)

downloads_folder = os.path.join(os.getcwd(), "download")

# Paths for both HTML files
html_path1 = os.path.join(downloads_folder, ref_file1 + ".html")
html_path2 = os.path.join(downloads_folder, ref_file2 + ".html")

# --- READ HTML FILES ---
with open(html_path1, "r", encoding="utf-8") as f:
    html_content1 = f.read()

with open(html_path2, "r", encoding="utf-8") as f:
    html_content2 = f.read()

# --- READ PROMPT ---
prompt_path = os.path.join(os.getcwd(), "input", "prompt.txt")
with open(prompt_path, "r", encoding="utf-8") as f:
    user_prompt = f.read()

# --- INITIALIZE CLIENT ---
client = Client()

# --- COMBINE CONTENT ---
combined_content = html_content1[:4000] + "\n\n" + html_content2[:4000]

messages = [
    {'role': 'user', 'content': user_prompt + "\n\n" + combined_content}
]

# --- GET RESPONSE ---
response = client.chat(
    model='llama3.1',
    messages=messages
)
print(response['message']['content'])

# --- SAVE OUTPUT ---
output_path = os.path.join(os.getcwd(), "llama_response.txt")
with open(output_path, "w", encoding="utf-8") as out_file:
    out_file.write(response['message']['content'])