from app.agent.gemini.client import get_gemini
from app.routes.transcribe import score
from fastapi import UploadFile, File
import json

def gen_feedback(transcript: str,  audio_file: UploadFile = File(...)):
    client = get_gemini()
    
    prompt = f"""
                Look at the following metrics:
                {score(transcript, audio_file)}

                Using these, generate feedback for the user who is trying to
                improve their speech. Keep the feedback breif and simple enough
                for a child  to  understand. Determine whether their attempt was
                correct or inccorect using the Metrics.

                The output should be formatted as such: 
                {{
                    "Conclusion": "Correct!",
                    "Feedback": "Great job, keep it up!"
                }}

                For an incorrect answer the output should be formatted as:
                {{
                    "Conclusion": "Almost!"
                    "Feedback": "Try making an "O" shape with your mouth
                }}

                Rules:
                - Only return valid JSON
                - Do not provide any explainations
                - Do not use any markdown
                - No extra text
                - Follow patterns set by the specified JSON
                - Do not use any special characters
            """
    
    response = client.models.generate_content(model="gemini-2.5-flash-lite", contents=prompt, config={"response_mime_type": "application/json"})
    output = response.candidates[0].content.parts[0].text
    output = output.replace("```json", "").replace("```", "").strip()
    print("feedback generated...")

    return json.loads(output)