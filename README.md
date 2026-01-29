# Recipe Video to Text

This project converts short cooking videos into recipes using AI.

---

## Scope

Supports:

- Uploading a cooking video file
- Transcribing spoken audio from the video
- Extracting recipe information using AI
- Displaying a readable recipe to the user

Out of scope:
- User accounts
- Saving recipes
- Social media link parsing
- Nutrition analysis

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
- Whisper (speech-to-text)
- GPT (recipe generation)

---

## User Flow

1. User uploads a cooking video
2. Backend extracts audio from the video
3. Audio is transcribed into text
4. AI converts transcript into a structured recipe
5. Recipe is displayed on the frontend
