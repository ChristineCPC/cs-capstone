import json, wave
from pathlib import Path

def build_timeline(phonemes, emphasis=None, slow=None):
    timeline = []

    for p in phonemes:
        duration = 0.2  # base duration

        if slow and p in slow:
            duration *= 2.5  # draw it out

        if emphasis and p in emphasis:
            duration *= 1.5  # slightly longer

        timeline.append({
            "phoneme": p,
            "duration": duration
        })

    return timeline

def load_frames():
 
    current_dir = Path(__file__).resolve().parent
    phoneme_map_path = current_dir.parent / "voice" / "phoneme-map.json"
    
    with open(phoneme_map_path, "r") as file:
        return json.load(file)["frames"]
    
def phoneme_to_frame(phoneme, frame_map):
    return frame_map.get(phoneme, "b_m_p.png")  #placeholder only
    
def build_animation_sequence(timeline, frame_map):
    sequence = []
    current_time = 0

    for item in timeline:
        phoneme = item["phoneme"]
        duration = item["duration"]

        frame = phoneme_to_frame(phoneme, frame_map)

        sequence.append({
            "frame": frame,
            "start": current_time,
            "end": current_time + duration
        })

        current_time += duration

    return sequence

def get_audio_duration(file_path):
    with wave.open(file_path, "rb") as wf:
        frames = wf.getnframes()
        rate = wf.getframerate()
        return frames / float(rate)
    
def normalize_timeline(timeline, audio_duration):
    total = sum(p["duration"] for p in timeline)

    scale = audio_duration / total

    for p in timeline:
        p["duration"] *= scale

    return timeline