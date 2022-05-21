import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def chat(text:str):
    conversacion = f"La siguiente es una conversación con un Chat Bot de discord. El bot es útil, creativo y inteligente.\n\n ¿Hola quien eres?\n Soy Akaza creado por K1ngAG. ¿Cómo puedo ayudarte hoy?\n {text}"

    response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=conversacion,
    temperature=0.9,
    max_tokens=150,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.6,
    stop=[" Humano:", " Akaza:"]
    )
    return str(response['choices'][0]['text']).replace("\n\n", "\n")