from app.agent.gemini.client import get_gemini
from app.routes.transcribe import score
from app.agent.voice.convert_tags import convert_tags
from app.agent.voice.voiceover import ipa_to_text, talk
from fastapi import UploadFile, File, Form
import json
from subprocess import Popen, PIPE

def gen_feedback(current_word: str = Form(...),  audio_file: UploadFile = File(...)):
    client = get_gemini()
    
    prompt = f"""
                Look at the following metrics:
                {score(current_word, audio_file)}

                Using these, act as a speech coach to generate feedback for the 
                user who is trying to improve their speech. Keep the feedback 
                breif and simple enough for a child  to  understand. 
                You will determine whether their attempt was correct or incorrect, 
                and identify which phonemes were pronounced incorrectly or were marked as
                missed phonemes, using the Metrics. Missed phonemes must be wrapped in
                tags like [slow] or [emphasize]. You will use these tags to produce
                a guide for the user that will help them understand how to 
                correctly pronunce a word/sentence based off of the mistakes they 
                made.

                The output should be formatted as such: 
                {{
                    "Conclusion": "Correct!",
                    "Feedback": "Great job, keep it up!"
                }}

                For an incorrect answer the output should be formatted as:
                {{
                    "Conclusion": "Almost!",
                    "Feedback": "Sounds like you said: _ Try making an "O" shape with your mouth to pronunce _.,
                    "Correction": "The c [slow] a [/slow] t walked by.",
                    "Correction Display": "The c**a**t walked by."
                }}

                Rules:
                - Only return valid JSON
                - Do not provide any explainations
                - Do not use any markdown, unless generating output for "Correction Display", which should only use **
                - No extra text
                - Follow patterns set by the specified JSON
                - Do not use any special characters, unless generating output for "Correction" and "Correction display", which should only use ** and []
                - Identify only one major pronunciation error from the metrics to generate an output for "Feedback". Do not list all of them.
                - Do not repeat the feedback sentence for multiple errors.
                - In the "Correction" field only use the tags [slow] and [emphasize] to specific characters of phonemes that you believe were incorrect or skipped from the expected pronunciation. Do not use [extra] or [incorrect]. Do not use ipa format phonemes. The output should be in alphanumeric characters only.
                - In the "Correction Display" field, only use **phoneme** for the phoneme that you are emphasizing instead of the whole word.
            """
    
    response = client.models.generate_content(model="gemini-2.5-flash-lite", contents=prompt, config={"response_mime_type": "application/json"})
    
    
    try: 
        output = response.text.strip()
        return json.loads(output)
    except json.JSONDecodeError as error:
        print(f"JSON Error: {error}")

        output = response.candidates[0].content.parts[0].text
        output = output.replace("```json", "").replace("```", "").strip()
    
    print("feedback generated...")

    return json.loads(output)

def get_feedback_script(feedback: str, phonemes: list):
    for phoneme in phonemes:
        text = ipa_to_text(phoneme)
        script = convert_tags(feedback, text)

    return script