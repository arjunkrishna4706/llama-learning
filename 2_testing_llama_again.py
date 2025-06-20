
@author: arjun.krishna4706@gmail.com
"""
#This code reads two txt files and a prompt file and records llama's responses to the prompts based on the two input files.

from ollama import chat
from pydantic import BaseModel, ValidationError
from typing import List
import os
import json

# ----- Define the Pydantic model -----
class ExecutiveCompensation(BaseModel):
    FYEAR: int
    EXEC_FULLNAME: str
    TITLE: str
    SALARY: float
    BONUS: float
    STOCK_AWARDS: float
    OPTION_AWARDS: float
    NONEQ_INCENT: float
    DEFER_RPT_AS_COMP_TOT: float
    OTHCOMP: float
    TOTCOMP: float

# ----- Load HTML file content -----
ref_file = "320193_DEF 14A_2022-01-06"
downloads_folder = os.path.join(os.getcwd(), "download")
html_path = os.path.join(downloads_folder, ref_file + ".html")

with open(html_path, "r", encoding="utf-8") as f:
    html_content = f.read()

# ----- Load the user prompt -----
prompt_path = os.path.join(os.getcwd(), "input", "prompt-testing.txt")
with open(prompt_path, "r", encoding="utf-8") as f:
    user_prompt = f.read()
del ref_file, downloads_folder, html_path, prompt_path, f

# ----- Setting the First User Prompt -----
response = chat(model='llama3.1',messages=[
    {"role": "user", "content": user_prompt + "\n\n" + html_content[:4000]}])
print("Question:", user_prompt)
print("Answer:", response.message.content)
output_path = os.path.join(os.getcwd(), "llama_response3.txt")


with open(output_path, "w", encoding="utf-8") as out_file:
    out_file.write(response['message']['content']) 