from fastapi import APIRouter, File, UploadFile

from app.routes.transcribe import transcribe
from app.routes.transcribe import score
from app.routes.feedback import get_feedback
from app.routes.activity import gen_activity

agent = APIRouter()

@agent.post("/agent")
def run_agent(activity:str, section: str, difficulty: str, current_index: int, audio_file: UploadFile = File(...)):
    transcript = transcribe(audio_file)
    get_activity = gen_activity(activity, section)
    get_score = score(activity, section, difficulty, current_index, audio_file)
    feedback = get_feedback(activity, section, difficulty, current_index, audio_file)

    return {
        "Transcript": transcript, 
        "Activity": get_activity, 
        "Score": get_score, 
        "Feedback": feedback
    }