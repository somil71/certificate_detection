import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()  # Load from .env file

api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-pro")

def validate_with_gemini(extracted_text):
    prompt = f"""
    You are an AI assistant helping to validate certificate text.
    Here's the extracted certificate text: "{extracted_text}"
    
    Does it seem like a valid certificate? Reply briefly with reasoning and a verdict.
    """
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Gemini API Error: {str(e)}"
