import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

role_system_prompts = {
    "developer": "You are a helpful coding assistant. Provide accurate, clean code and explain it if asked.",
    "manager": "You are an AI project manager. Provide strategic advice, timelines, and summaries.",
    "analyst": "You are a cybersecurity analyst assistant. Help investigate incidents and summarize threat reports.",
    "student": "You are a helpful tutor. Explain concepts clearly and guide the user through problem-solving."
}

def get_response_from_openai(role: str, user_input: str) -> str:
    system_prompt = role_system_prompts.get(role.lower(), "You are a helpful assistant.")

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_input}
            ],
            max_tokens=500,
            temperature=0.7,
        )
        return response.choices[0].message['content'].strip()

    except Exception as e:
        return f"❌ Error: {str(e)}"
