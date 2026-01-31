from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import shutil
from app.services.transcription import transcribe_audio
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
    video_path = f"temp_{file.filename}"

    # Save uploaded file
    with open(video_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Transcribe
    transcript = transcribe_audio(video_path)

    # Generate recipe
    recipe = generate_recipe(transcript)

    return {
        "transcript": transcript,
        "recipe": recipe
    }

# New AI recipe generation endpoint
class TranscriptRequest(BaseModel):
    transcript: str

@app.post("/generate-recipe")
def generate_recipe_endpoint(data: TranscriptRequest):
    return generate_recipe(data.transcript)
