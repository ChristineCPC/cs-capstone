from app.agent.gemini.client import get_gemini
from app.agent.voice.convert_tags import convert_tags, ipa_to_text
import piper
import json, uuid, os
from pathlib import Path
from subprocess import Popen, PIPE

client = get_gemini()

#gemini will determine which phonemes will need emphasis or be pronounced more slowly
def gen_tags(current_word: str):
    prompt = f"""
                You are a speech therapist. You are to take {current_word} and use the tags
                [slow] and [emphasis] to demonstrate to a child how to pronunce the word
                correctly.

                Your output should be formatted as such:
                {{
                    "Phonemes": ["a"],
                    "Breakdown": "The c [slow]a[/slow] t walked by."
                }}

                Rules:
                - Only return valid JSON
                - Do not provide any explainations
                - Do not use any markdown
                - No extra text
                - Follow patterns set by the JSON file provided
                - Use standard alphabumeric characters for words only while maintaining JSON structure.
                - only use the tags [slow] and [emphasis] to specific characters that you believe need to be emphasized or slowed for better understanding.
            """
    response = client.models.generate_content(model="gemini-2-flash", contents=prompt, config={"response_mime_type": "application/json"})

    return json.loads(response.text)


def get_script(current_word: str):
    tags = gen_tags(current_word)

    #output = tags["Phonemes"]

    #for phoneme in output:
    breakdown= tags["Breakdown"]
    phonemes = tags["Phonemes"]

    script = breakdown

    for phoneme in phonemes:
        text = ipa_to_text(phoneme)
        script = convert_tags(breakdown, text)

    return script



def talk(current_word: str):
    script = get_script(current_word)
    
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
