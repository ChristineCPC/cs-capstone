from fastapi import APIRouter
from app.agent.gemini.sessions.generate_activity import gen_activity

activities = APIRouter()

@activities.get("/activity")
def generate_bank(activity: str, section: str):
    bank = gen_activity(activity, section)
    return bank