from subprocess import Popen, PIPE
from app.agent.gemini.generate_feedback import gen_feedback

#gemini will produce a new voiceover based on the feedback generated from the user's attempts. 
def gen_feedback_voiceover(gemini_output):
    script = gemini_output
    
    process = Popen([
        "piper",
        "--model", "app/agent/voice/piper/en_US-amy-low.onnx",
        "--output_file", "output.wav"
    ],
        stdin=PIPE,
        stdout=PIPE,
        stderr=PIPE,
        text=False
    )

    process.communicate(script.encode("utf-8"))

 #   3with open("output.wav", "rb") as f:
#        return f.read()

    return "output.wav"
