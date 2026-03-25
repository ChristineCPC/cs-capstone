from fastapi import FastAPI
from app.routes.transcribe import transcriptions
from app.routes.activity import activities
from app.routes.feedback import feedback
from app.routes.agent import agent

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

app.include_router(transcriptions)
app.include_router(activities)
app.include_router(feedback)
app.include_router(agent)


