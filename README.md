# 🤖 AI Data Science Mentor

AI Data Science Mentor adalah chatbot berbasis Artificial Intelligence (AI) yang dirancang untuk membantu pengguna mempelajari Data Science secara interaktif. Aplikasi ini memanfaatkan Google Gemini API sebagai Large Language Model (LLM) dan dibangun menggunakan Streamlit sebagai antarmuka pengguna.

Project ini dibuat sebagai implementasi penggunaan **LLM Based Tools & Gemini API Integration.

---

## ✨ Features

- 🤖 AI Chatbot berbasis Google Gemini
- 📚 3 Mode Belajar
  - Beginner
  - Intermediate
  - Expert
- 💬 Chat History (AI mengingat konteks percakapan)
- 🗑 Clear Chat
- ⚡ Respon real-time menggunakan Gemini API
- 🎨 User Interface interaktif menggunakan Streamlit

---

## 🖥 Preview

### Home

![Home](images/home.png)

---

### Chat Example

![Chat](images/chat.png)

---

## 📂 Project Structure

project-chatbot/
│
├── app.py                 
├── chatbot.py            
├── config.py              
├── prompt.py              
├── requirements.txt       
├── .gitignore
├── README.md
├── .env                   
│
└── assets/
      ├── home.png
      └── chat.png

---

## 🛠 Technologies

| Technology | Description |
|------------|-------------|
| Python | Bahasa pemrograman utama |
| Streamlit | Framework UI |
| Google Gemini API | Large Language Model |
| python-dotenv | Membaca API Key |
| Git & GitHub | Version Control |

---

## 📚 Learning Modes

### 🟢 Beginner

- Penjelasan sederhana
- Cocok untuk pemula
- Menggunakan bahasa yang mudah dipahami

---

### 🟡 Intermediate

- Penjelasan lebih teknis
- Disertai contoh sederhana
- Cocok untuk mahasiswa atau pembelajar menengah

---

### 🔴 Expert

- Penjelasan mendalam
- Menggunakan istilah teknis
- Best Practice
- Insight tambahan

---

## 🚀 Installation

### 1. Clone Repository

```bash
git clone https://github.com/USERNAME/project-chatbot.git
```

### 2. Masuk ke Folder Project

```bash
cd project-chatbot
```

### 3. Buat Virtual Environment

```bash
python -m venv venv
```

### 4. Aktifkan Virtual Environment

Windows

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
source venv/bin/activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variable

Buat file .env

```env
GEMINI_API_KEY=YOUR_API_KEY
```

---

## ▶️ Run Application

```bash
streamlit run app.py
```

---

## 💬 Example Questions

### Beginner

- Apa itu Data Science?
- Apa itu Machine Learning?
- Jelaskan ETL dengan bahasa sederhana.

### Intermediate

- Berikan contoh SQL JOIN.
- Jelaskan perbedaan Random Forest dan Decision Tree.
- Bagaimana proses Feature Engineering?

### Expert

- Jelaskan konsep Cross Validation.
- Kapan menggunakan Gradient Boosting?
- Apa trade-off antara Bias dan Variance?

---

## 📌 Workflow

User
   │
   ▼
Streamlit UI
   │
   ▼
Prompt Builder
   │
   ▼
Google Gemini API
   │
   ▼
AI Response
   │
   ▼
Streamlit UI

---

## 📷 Screenshot

| Home | Chat |
|------|------|
|(assets/home.png) | (assets/chat.png) |

---

## 👨‍💻 Author

Lutfi
Final Project — LLM Based Tools & Gemini API Integration
Hacktiv8 Indonesia

---

## 📄 License
This project is created for educational purposes.