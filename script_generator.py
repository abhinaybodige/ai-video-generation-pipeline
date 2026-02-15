import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")


def generate_script(topic):

    url = "https://api.groq.com/openai/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    prompt = f"""
    Write a YouTube narration script about {topic}.
    Around 120 words.
    Engaging, educational tone.
    No headings or bullet points.
    """

    data = {
        "model": "llama-3.1-8b-instant",   
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code != 200:
        print("API ERROR:", response.text)
        raise Exception("Groq API request failed")
    result = response.json()
    return result["choices"][0]["message"]["content"].strip()
