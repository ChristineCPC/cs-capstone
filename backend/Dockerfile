FROM python:3.13-slim

RUN apt-get update && apt-get install -y \
    espeak-ng \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
# Pre-downloads models; should be faster
RUN python -c "from transformers import WhisperForConditionalGeneration; WhisperForConditionalGeneration.from_pretrained('openai/whisper-small')"

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]