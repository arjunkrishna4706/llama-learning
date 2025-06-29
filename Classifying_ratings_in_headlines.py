###Classify News Headlines
###This file reads an input CSV file with headlines from different news sources. If the headline is about ratings on a single entity, it adds a column that says 1, else 0. 
###@author: arjun.krishna4706@gmail.com

import csv
import subprocess
import json


def query_llama_llocally(prompt: str) -> str:
    """
    Sends a prompt to the locally running LLaMA 3.1 model via Ollama and returns the plain text response.
    """
    try:
        result = subprocess.run(
            ['ollama', 'run', 'llama3', prompt],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=True,
            text=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print("Error calling LLaMA:", e.stderr)
        return "no"

def classify_headline(headline_text: str) -> int:
    prompt = f"""
Determine if the following headline is a news item related to a rating change on a single company or entity. Respond with 'yes' or 'no' only.

Headline: "{headline_text}"
"""
    response = query_llama_llocally(prompt)
    return 1 if response.lower().strip().startswith("yes") else 0

# Input and Output files
input_file = 'dow-jones-headlines-mini.csv'
output_file = 'dow-jones-output.csv'

with open(input_file, mode='r', newline='', encoding='utf-8') as infile:
    reader = csv.DictReader(infile)
    fieldnames = reader.fieldnames + ['Rating']

    with open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            headline_text = row.get('headline', '')
            row['Rating'] = classify_headline(headline_text)
            writer.writerow(row)

print(f"Updated CSV written to '{output_file}' using 'headline' for LLaMA-inferred Ratings.")