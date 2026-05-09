from app.agent.voice.voiceover import gen_tags, talk
from app.agent.demo_animation.build_animation import build_timeline, load_frames, build_animation_sequence, normalize_timeline, get_audio_duration
import os
from fastapi import APIRouter, Form, Response

demo = APIRouter()

@demo.post("/demo")
def generate_demo(word: str = Form(...)):
    tags = gen_tags(word)

    phonemes = tags["Phonemes"] 

    timeline = build_timeline(
        phonemes,
        emphasis=phonemes,  
        slow=phonemes
    )

    # generate audio
    audio_bytes = talk(word)

    # save temp file to measure duration
    temp_file = "temp.wav"
    with open(temp_file, "wb") as f:
        f.write(audio_bytes)

    duration = get_audio_duration(temp_file)

    timeline = normalize_timeline(timeline, duration)

    frame_map = load_frames()

    animation = build_animation_sequence(timeline, frame_map)

    os.remove(temp_file)

    return {
        "audio": audio_bytes,
        "animation": animation
    }