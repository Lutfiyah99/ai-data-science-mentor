"""
config.py berisi seluruh konfigurasi aplikasi
"""

# Membaca env  variabel
import os

# Membaca file env
from dotenv import load_dotenv

# Membaca file .env
load_dotenv()

# Konfigurasi API 
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


# Konfigurasi Aplikasi
APP_NAME = "AI Data Science Mentor" 
PAGE_TITLE = "AI Data Science Mentor"
PAGE_ICON = "🤖"
LAYOUT = "wide"

# Konfigurasi model Gemini
MODEL_NAME = "gemini-2.5-flash"
TEMPERATURE = 0.7
TOP_P = 0.95
MAX_OUTPUT_TOKENS = 500

# Konfigurasi chat
MAX_HISTORY = 10

WELCOME_MESSAGE = """
Halo 👋

Saya adalah AI Data Science Mentor.

Saya dapat membantu Anda mengenai:

• Python
• SQL
• ETL
• Machine Learning
• Deep Learning
• Data Visualization
• Roadmap Belajar Data Science

Silakan ajukan pertanyaan - !!
"""
INPUT_PLACEHOLDER = "Tanyakan sesuatu tentang Data Science..."