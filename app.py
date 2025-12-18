from flask import Flask, request, jsonify
from flask_cors import CORS
from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os, hashlib

load_dotenv()

app = Flask(__name__)
CORS(app)

client = InferenceClient(token=os.getenv("HF_TOKEN"))

page_sessions = {}

def page_id(url):
    return hashlib.md5(url.encode()).hexdigest()

@app.route("/init", methods=["POST"])
def init_page():
    url = request.json["url"]
    pid = page_id(url)

    if pid not in page_sessions:
        loader = WebBaseLoader(url)
        docs = loader.load()

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=50
        )

        chunks = splitter.split_text(docs[0].page_content)
        context = "\n\n".join(chunks)

        page_sessions[pid] = {
            "chat": [
                {
                    "role": "system",
                    "content": (
                        "You are a helpful AI assistant. "
                        "Answer ONLY using the webpage content provided."
                    )
                },
                {
                    "role": "user",
                    "content": f"Webpage content:\n\n{context}"
                }
            ]
        }

    return jsonify({"message": "Page loaded. Ask your questions."})

@app.route("/chat", methods=["POST"])
def chat():
    message = request.json["message"]

    pid = list(page_sessions.keys())[-1]
    chat_history = page_sessions[pid]["chat"]

    chat_history.append({"role": "user", "content": message})

    result = client.chat_completion(
        model="meta-llama/Llama-3.1-8B-Instruct",
        messages=chat_history,
        max_tokens=300,
        temperature=0.7
    )

    reply = result.choices[0].message.content
    chat_history.append({"role": "assistant", "content": reply})

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
