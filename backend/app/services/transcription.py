from deepgram import DeepgramClient
from dotenv import load_dotenv
import os
load_dotenv()

client = DeepgramClient(api_key=os.getenv("DEEPGRAM_API_KEY"))

def transcribe_audio(file_path: str) -> str:
    with open(file_path, "rb") as audio_file:
        # 2. Read the file into a buffer
        request_data = audio_file.read()

        # 3. Call the transcription service directly
        # In v6.0.1, you pass settings like 'model' as keyword arguments
        response = client.listen.v1.media.transcribe_file(
            request=request_data,
            model="nova-3",      # Use the latest Nova-3 model
            smart_format=True,   # Essential for recipe formatting
            language="en-US"
        )
        
        # 4. Extract the final transcript string
        return response.results.channels[0].alternatives[0].transcript
