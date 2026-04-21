import os

from fastapi import APIRouter, UploadFile, File, Form
from app.agent.whisper.transcription import transcribe_audio
from app.agent.finetuned_whisper.pronunciation_score import pronunciation_score
import shutil

transcriptions = APIRouter()

@transcriptions.post("/transcribe")
def transcribe(audio_file: UploadFile = File(...)):
    audio_file_location = f"temp_{audio_file.filename}"

    audio_file.file.seek(0)

    with open(audio_file_location, "wb") as buffer:
        shutil.copyfileobj(audio_file.file, buffer)

    transcript = transcribe_audio(audio_file_location)

    print(f"Recieved, , {audio_file.filename}: {transcript}")

    return transcript

@transcriptions.post("/score")
def score(current_word: str = Form(...),  audio_file: UploadFile = File(...)):
    transcript = transcribe(audio_file)
    expected_transcript = current_word

    audio_file_location = f"temp_{audio_file.filename}"

    audio_file.file.seek(0)

    with open(audio_file_location, "wb") as buffer:
        shutil.copyfileobj(audio_file.file, buffer)
 
    try:
        transcript = transcribe_audio(audio_file_location)

        print(f"Recieved, , {audio_file.filename}: {transcript}")

        return {
            "Transcript": transcript, 
            "Pronunciation Score Metrics": pronunciation_score(audio_file_location, expected_transcript)
        }
    finally:
        if os.path.exists(audio_file_location):
            os.remove(audio_file_location)