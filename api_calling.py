from google import genai
import os,io
from dotenv import load_dotenv
from gtts import gTTS

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key = api_key)

def Note_Generator(images):
    prompt = """Summarize the picture in note format in bangla lenguage at max 100 words,
    make sure to add necesssary markdown to differentiate different section"""
    response = client.models.generate_content(
        model = "gemini-3-flash-preview",
        contents = [images,prompt]
    )

    return response.text

def audio_transcrept(text):

    speech = gTTS(text,lang = 'bn')

    audio_buffer = io.BytesIO()

    speech.write_to_fp(audio_buffer)

    return audio_buffer

def Quiz_Generator(images,Difficulty):
    prompt = f"Generate 3 quizzes in bangla lenguage based on the {Difficulty}. Make sure to add markdown to differentiate the options. Add correct ans too after the Quez"

    response = client.models.generate_content(
        model = "gemini-3-flash-preview",
        contents = [images,prompt]
    )

    return response.text