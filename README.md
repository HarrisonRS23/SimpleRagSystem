# SimpleRagSystem

# Local Chatbot Web App

A simple local web application that integrates a Python chatbot script with a Flask backend and a minimal HTML/JavaScript frontend. The app runs locally in your browser and allows you to interact with a chatbot. 

The Context is a simple 150 line document about cats. The Chatbot will use this as the context for the chat queries. Questions not about cats or information not included may result in unexpected responses. 

---

## 🚀 Features

- Lightweight Flask backend to handle chatbot requests  
- Simple chatbot logic written in Python  
- Minimal HTML + JavaScript frontend interface  
- Fully local, no external dependencies beyond Flask  

---

## ⚙️ Installation

1. **Set up a virtual environment (recommended):**

python3 -m venv venv
source venv/bin/activate    # On macOS/Linux
venv\Scripts\activate       # On Windows

2. Install dependencies:
pip install flask ollama

Note: If you are using Ollama, make sure it is installed and configured correctly on your system.

## Usage

Run the Flask server:
python app.py

Open your browser and navigate to:
http://127.0.0.1:5000/

Chat with the bot!
Type your message into the input box, click "Send," and the bot will respond in real time.
