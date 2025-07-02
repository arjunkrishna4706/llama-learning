
#@author: arjun.krishna4706@gmail.com

import csv
import subprocess

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

def get_rating_from_lead(lead_text):
    prompt = f"""Determine if the following headline is a news item related to a rating change on a single company or entity. Respond with 'yes' or 'no'.

Headline: '{lead_text}'

Answer:"""
    response = query_llama_llocally(prompt)
    return 1 if response.strip().lower() == 'yes' else 0

def get_topic_from_lead(lead_text):
    prompt = f"""Classify the following headline into one of these categories:
- Earnings
- M&A
- Lawsuit
- Executive Change
- IPO
- Capital Return
- Guidance
- Rating Change
- Other

Headline: '{lead_text}'

Respond only with the category name."""
    response = query_llama_llocally(prompt)
    return response.strip()

# Input and output file names
input_file = 'dow-jones-headlines-mini.csv'
output_file = 'dow-jones-output.csv'

with open(input_file, mode='r', newline='', encoding='utf-8') as infile:
    reader = csv.DictReader(infile)
    fieldnames = reader.fieldnames + ['Rating', 'Topic']
    
    with open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            lead_text = row.get('lead', '')
            row['Rating'] = get_rating_from_lead(lead_text)
            row['Topic'] = get_topic_from_lead(lead_text)
            writer.writerow(row)

print(f"Updated file written to '{output_file}' with computed 'Rating' and 'Topic'.")