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

from ollama import chat
from ollama import ChatResponse

chat_history = [
    {"role": "system", "content": "You are a helpful assistant."}
]

prompts = [
    "What is photosynthesis?",
    "Can you explain how it helps plants survive?",
    "What role does sunlight play in this?",
    "Is there any equivalent process in animals?",
    "How can understanding photosynthesis help with climate change?"
]

for prompt in prompts:
    chat_history.append({"role": "user", "content": prompt})
    response = chat(
        model='llama3.1',
        messages=chat_history
    )
    print("Question:", prompt)
    print("Answer:", response.message.content)
    # or access fields directly from the response object
    print(response.message.content)
    chat_history.append({"role": "assistant", "content": response.message.content})