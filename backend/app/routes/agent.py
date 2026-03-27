from fastapi import APIRouter, File, UploadFile, Form

from app.routes.transcribe import transcribe
from app.routes.transcribe import score
from app.routes.feedback import get_feedback
from app.routes.activity import gen_activity

agent = APIRouter()

@agent.post("/agent")
def run_agent(current_word: str = Form(...), audio_file: UploadFile = File(...)):
    transcript = transcribe(audio_file)
    get_score = score(current_word, audio_file)
    feedback = get_feedback(current_word, audio_file)

    return {
        "Transcript": transcript, 
        "Score": get_score, 
        "Feedback": feedback
    }