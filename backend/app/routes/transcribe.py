from fastapi import APIRouter, UploadFile, File
from app.agent.whisper.transcription import transcribe_audio
from app.agent.pronunciation_score import pronunciation_score
from app.agent.gemini.sessions.generate_activity import gen_activity
import shutil

transcriptions = APIRouter()

@transcriptions.post("/transcribe")
def transcribe(audio_file: UploadFile = File(...)):
    audio_file_location = f"temp_{audio_file.filename}"

    with open(audio_file_location, "wb") as buffer:
        shutil.copyfileobj(audio_file.file, buffer)

    transcript = transcribe_audio(audio_file_location)

    print(f"Recieved, , {audio_file.filename}: {transcript}")

    return transcript

@transcriptions.post("/score")
def score(activity: str, section: str, difficulity: str, current_index: int,  audio_file: UploadFile = File(...)):
    transcript = transcribe(audio_file)
    expected_transcript = gen_activity(activity, section)[difficulity][current_index]
    #expected_transcript = expected_transcript[difficulity]
    
    return pronunciation_score(transcript, expected_transcript)