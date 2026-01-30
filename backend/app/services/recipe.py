from openai import OpenAI
from dotenv import load_dotenv
import json
import os
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_recipe(transcript: str):
    prompt = f"""
You are a helpful cooking assistant.

From the following transcript, extract a recipe.
Return ONLY valid JSON with this format:

{{
  "title": "...", 
  "ingredients": ["...", "..."],
  "steps": ["...", "..."]
}}

Transcript:
{transcript}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )

    content = response.choices[0].message.content

    return json.loads(content)
