from fastapi.responses import FileResponse
from app.agent.voice.voiceover import gen_tags, talk
from app.agent.demo_animation.build_video import build_demo_video
from app.agent.voice.convert_tags import ipa_to_text
from fastapi import APIRouter, Form

video = APIRouter()

#fix attempt; discard with relevent files if it doesn't work.
@video.post("/video")
def gen_video(word: str = Form(...)):

    tags = gen_tags(word)

    phonemes = [
        ipa_to_text(p)
        for p in tags["Phonemes"]
    ]

    audio_path = talk(word)

    video_path = build_demo_video(
        phonemes,
        audio_path
    )

    return FileResponse(
        video_path,
        media_type="video/mp4",
        filename="video.mp4"
    )