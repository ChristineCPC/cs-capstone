from moviepy import ImageClip, AudioFileClip, concatenate_videoclips
from pathlib import Path
import json

# load frame map
def load_frames():
    current_dir = Path(__file__).resolve().parent
    phoneme_map_path = current_dir.parent / "voice" / "phoneme-map.json"

    with open(phoneme_map_path, "r") as file:
        return json.load(file)["frames"]


def phoneme_to_frame(phoneme, frame_map):
    return frame_map.get(phoneme, "b_p_m.png")

# build actual video
def build_demo_video(phonemes, audio_path):
    frame_map = load_frames()

    clips = []

    frames_dir = Path("app/assets/frames")

    for phoneme in phonemes:
        frame_name = phoneme_to_frame(phoneme, frame_map)

        image_path = frames_dir / frame_name

        clip = ImageClip(str(image_path)).set_duration(0.25)

        clips.append(clip)

    final_animation = concatenate_videoclips(clips, method="compose")

    audio = AudioFileClip(audio_path)

    final_video = final_animation.set_audio(audio)

    output_path = "video.mp4"

    final_video.write_videofile(
        output_path,
        fps=12,
        codec="libx264",
        audio_codec="aac"
    )

    return output_path