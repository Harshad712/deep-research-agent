import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-2.0-flash')

# Function to draft answer using Gemini
def draft_answer(query: str, research: str) -> str:
    prompt = f"""
    You are a helpful assistant. Based on the research below, answer the user's question.

    User's Question:
    {query}

    Research:
    {research}

    Provide a well-structured, informative response.
    """
    response = model.generate_content(prompt)
    return response.text
