from fastapi import APIRouter, Form, UploadFile, File, Response
from app.agent.voice.feedback_voiceover import gen_feedback_voiceover
from app.agent.gemini.generate_feedback import gen_feedback

feedback_voice = APIRouter()

@feedback_voice.post("/feedback-voice")
def get_feedback_voice(transcript: str = Form(...), audio_file: UploadFile = File(...)):
    feedback = gen_feedback(transcript, audio_file)
    correction = feedback["Correction"]

    voiceover_audio = gen_feedback_voiceover(correction)

    return Response(content=voiceover_audio, media_type="audio/mpeg")