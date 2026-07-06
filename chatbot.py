from google import genai 

from config import (
    GEMINI_API_KEY,
    MODEL_NAME,
    TEMPERATURE,
    TOP_P,
    MAX_OUTPUT_TOKENS
)

from prompt import (
    SYSTEM_PROMPT,
    BEGINNER_PROMPT,
    INTERMEDIATE_PROMPT,
    EXPERT_PROMPT,
    CODING_PROMPT,
    SQL_PROMPT,
    ROADMAP_PROMPT
)

# menghubungkan ke gemini
def connect_model():
    client = genai.Client(
    api_key=GEMINI_API_KEY
    )

    return client

# memilih propt yg akan digunakan
def build_prompt(question, mode, chat_history):
    if mode == "Beginner":
        mode_prompt = BEGINNER_PROMPT
    elif mode == "Intermediate":
        mode_prompt = INTERMEDIATE_PROMPT
    elif mode == "Expert":
        mode_prompt = EXPERT_PROMPT
    else:
        mode_prompt = ""

    history = ""
    
    for message in chat_history:
        history += f"{message['role']} : {message['content']}\n"

    full_prompt = f"""
{SYSTEM_PROMPT}

{mode_prompt}

Riwayat Percakapan:
{history}

Pertanyaan Terbaru:
{question}
"""
    return full_prompt


# meemberikan respon ke user
def generate_response(question, mode, chat_history):
    try:
        client = connect_model()
        
        prompt = build_prompt(question, mode, chat_history)
        
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt
    )
    
        return response.text

    except Exception as e:
        return f"Terjadi kesalahan: {e}"

