from fastapi import APIRouter, UploadFile, File
from app.agent.whisper.transcription import transcribe_audio
import shutil

router = APIRouter()

#rough draft for whipser transcription logic in the backend
@router.post("/transcribe")
def transcribe(audio_file: UploadFile = File(...)):
    audio_file_location = f"temp_{audio_file.filename}"

    with open(audio_file_location, "wb") as buffer:
        shutil.copyfileobj(audio_file.file, buffer)

    transcript = transcribe_audio(audio_file_location)

    print(f"Recieved, , {audio_file.filename}: {transcript}")

    return {"transcription": transcript}