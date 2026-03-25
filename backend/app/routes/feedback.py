from fastapi import APIRouter, UploadFile, File
from app.agent.gemini.generate_feedback import gen_feedback

feedback = APIRouter()

@feedback.post("/feedback")
def get_feedback(activity:str, section: str, difficulty: str, current_index: int, audio_file: UploadFile = File(...)):
    output = gen_feedback(activity, section, difficulty, current_index, audio_file)
    return output