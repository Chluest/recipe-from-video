from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from app.services.recipe import generate_recipe

app = FastAPI()

# Allow requests from frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # your frontend URL
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.post("/upload")
async def upload_video(file: UploadFile = File(...)):
    # Fake processing for MVP
    recipe = {
        "title": "Creamy Garlic Pasta",
        "ingredients": [
            "200g pasta",
            "2 cloves garlic",
            "1 cup heavy cream",
            "Salt",
            "Black pepper",
        ],
        "steps": [
            "Boil the pasta until al dente.",
            "Sauté garlic in a pan until fragrant.",
            "Add cream and simmer.",
            "Toss pasta with sauce.",
            "Season and serve.",
        ],
    }
    return recipe

# New AI recipe generation endpoint
class TranscriptRequest(BaseModel):
    transcript: str

@app.post("/generate-recipe")
def generate_recipe_endpoint(data: TranscriptRequest):
    return generate_recipe(data.transcript)
