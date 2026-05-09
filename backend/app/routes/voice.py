from fastapi import APIRouter, Form
from fastapi.responses import FileResponse
#from app.agent.voice.voiceover import gen_voiceover
from app.agent.voice.voiceover import talk


voice = APIRouter()

@voice.post("/voice")
def get_voice(transcript: str = Form(...)):

    #voiceover_audio = gen_voiceover(transcript)

    #return Response(content=voiceover_audio, media_type="audio/wav", headers={"Content-Disposition": "attachment; filename=output.wav"})
   audio = talk(transcript)
   print(type(audio))

   #return Response(content=audio, media_type="audio/wav", headers={"Content-Disposition": "attachment; filename=output.wav"})
   return FileResponse(audio, media_type="audio/wav", filename="output.wav")