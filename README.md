# Recipe from Video

A full-stack application that converts cooking videos into structured, readable recipes using AI. Upload a video, and the app extracts the audio, transcribes it, and uses GPT-4 to generate a clean ingredient list and step-by-step instructions.

---

## How It Works

The backend processes uploaded videos through a multi-stage AI pipeline:

1. **Audio Extraction** — MoviePy strips the audio track from the uploaded video file
2. **Speech-to-Text** — OpenAI Whisper transcribes the audio into raw text
3. **Recipe Generation** — GPT-4 takes the unstructured transcript and transforms it into a formatted recipe with ingredients and instructions
4. **Delivery** — The structured recipe is returned to the Next.js frontend for display

This pipeline handles the core challenge of converting unstructured, conversational cooking narration into clean, usable recipe data.

---

## Tech Stack

### Frontend
- Next.js
- React
- Tailwind CSS

### Backend
- Python
- FastAPI

### AI Services
- OpenAI Whisper (speech-to-text)
- GPT-4 (recipe structuring)
- MoviePy (audio extraction)

---

## Project Status

Active development. Core pipeline (upload → transcribe → generate → display) is functional. Planned additions:

- Recipe saving and history
- Improved prompt tuning for edge cases (non-English recipes, heavily improvised cooking)
- Support for social media video URLs
- Nutrition analysis

---

## Scope

**In scope:**
- Uploading a local cooking video file
- Audio transcription via Whisper
- AI-powered recipe extraction
- Displaying a structured recipe to the user

**Out of scope (for now):**
- User accounts
- Social media link parsing
- Nutrition analysis

---

## Local Setup

### Prerequisites
- Node.js
- Python 3.9+
- OpenAI API key

### Backend
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```

Set your OpenAI API key as an environment variable:
```bash
export OPENAI_API_KEY=your_key_here
```