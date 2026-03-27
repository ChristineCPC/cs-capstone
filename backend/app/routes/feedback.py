from fastapi import APIRouter, UploadFile, File
from app.agent.gemini.generate_feedback import gen_feedback

feedback = APIRouter()

@feedback.post("/feedback")
def get_feedback(transcript: str, audio_file: UploadFile = File(...)):
    output = gen_feedback(transcript, audio_file)
    return output