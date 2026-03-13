import whisper

model = whisper.load_model("base.en")
     
def transcribe_audio(audio_file):
    output = model.transcribe(audio_file, fp16=False)
    return output["text"]