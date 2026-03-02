from dotenv import load_dotenv
from pydantic import BaseModel
from typing import List
import anthropic
import json
import os

load_dotenv()

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

class Recipe(BaseModel):
    title: str
    ingredients: List[str]
    steps: List[str]

def generate_recipe(transcript: str):
    schema = Recipe.model_json_schema()

    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=2048,
        system=(
            "You are a professional chef. Extract the recipe from the transcript. "
            f"Respond ONLY with valid JSON matching this schema: {json.dumps(schema)}"
        ),
        messages=[
            {"role": "user", "content": f"Extract the recipe: {transcript}"}
        ],
        temperature=0.2
    )

    raw = response.content[0].text.strip()
    # Strip markdown code fences if present
    if raw.startswith("```"):
        raw = raw.split("```")[1]
        if raw.startswith("json"):
            raw = raw[4:]
    
    return Recipe(**json.loads(raw))
