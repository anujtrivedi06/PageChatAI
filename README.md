# Page Chat AI 🧠🌐

A Chrome extension + Flask backend that turns **any webpage into an AI-powered chatbot**.  
The assistant automatically extracts webpage content and allows users to ask contextual questions about the page.

---

## ✨ Features

- 🔍 Chat with **any webpage**
- 🌐 Automatically detects the **current browser tab**
- 🧠 Page-scoped conversation memory
- 🐍 Python backend using **Flask**
- 🤗 Hugging Face inference (Mistral-7B)
- 🔐 No API keys exposed to the browser
- 🧩 Modular and extensible architecture

---

## 🏗️ Architecture
```bash
Chrome Extension (Frontend)
↓
Flask API (Backend)
↓
Webpage Loader + Chunking
↓
LLM Inference (HF)
```
---

## 📁 Project Structure
```bash
chrome_chat/
│
├── backend/
│ ├── app.py
│ ├── requirements.txt
│ ├── .env
│ └── venv/
│
└── extension/
├── manifest.json
├── popup.html
└── popup.js
```
---

## 🚀 Getting Started

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/page-chat-ai.git
cd page-chat-ai
```
2️⃣ Backend Setup (Flask)
Create virtual environment
```bash
cd backend
python -m venv venv
```
Activate it:

Windows

```bash
venv\Scripts\activate
```
Install dependencies
```bash
pip install -r requirements.txt
```
Set Hugging Face token
Create a .env file inside backend/:

env
```bash
HF_TOKEN=your_huggingface_api_token
```
⚠️ Do NOT expose this token in the Chrome extension.

Run Flask server
```bash
python app.py
```
Server runs at:

cpp
http://127.0.0.1:5000
3️⃣ Load Chrome Extension
Open Chrome

Go to chrome://extensions

Enable Developer mode

Click Load unpacked

Select the extension/ folder

The extension icon will appear in the toolbar.

🧪 How to Use
Open any webpage

Click the Page Chat AI extension

Click Initialize Page

Ask questions like:

What is this page about?

Summarize the key points

Explain this section in simple terms

🛠️ Technologies Used
Python

Flask

LangChain

Hugging Face Inference API

Mistral-7B-Instruct

JavaScript (Chrome Extension API)

⚠️ Known Limitations
Uses server-side scraping (WebBaseLoader)

Not optimized for very large pages

Single-user session memory

Development server only (not production-ready)

🔮 Future Improvements
🔍 DOM extraction via content scripts

🧠 RAG with FAISS for large pages

🧵 Streaming responses

🏠 Local LLM support (Ollama)

🌍 Multi-tab & multi-user support

🚀 FastAPI backend

🤝 Contributing
Pull requests are welcome.
For major changes, please open an issue first to discuss what you’d like to change.

🙌 Acknowledgements
Hugging Face 🤗

LangChain

Mistral AI

Chrome Extension APIs

---

