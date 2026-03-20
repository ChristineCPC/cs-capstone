from google import genai
import os, dotenv

dotenv.load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def get_gemini():
    return client
