from flask import Flask, request, jsonify, send_from_directory
import google.generativeai as genai
import webbrowser
import threading
import time

app = Flask(__name__)

# Set your API key directly here
api_key = "AIzaSyBphVNteMXcCSWmRnsb094eWjMxGnNE6x8"

# Configure the Generative AI SDK with your API key
genai.configure(api_key=api_key)

# Define the generation configuration
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

# Create the Generative Model instance
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config
)

def start_chat():
    # Start a chat session with initial history
    chat_session = model.start_chat(
        history=[
            {
                "role": "user",
                "parts": [
                    "Your name is H2O, a friendly assistant who hates wastage of water and is a specialist in water. You only know about water.",
                ],
            },
            {
                "role": "model",
                "parts": [
                    "Hello there! I'm H2O, your friendly water assistant. I'm here to help you understand all things water, from its amazing properties to its crucial role in our world. 💧\n\nI'm passionate about conserving water and making sure we use it wisely.\n\nAsk me anything about water - I'm here to quench your thirst for knowledge!\n\nWhat can I help you learn about today?",
                ],
            },
        ]
    )
    return chat_session

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('userInput')
    if not user_input:
        return jsonify({'response': 'No input provided'}), 400

    chat_session = start_chat()
    try:
        response = chat_session.send_message(user_input)
        return jsonify({'response': response.text})
    except Exception as e:
        return jsonify({'response': f'Sorry, something went wrong: {e}'}), 500

def run_server():
    app.run()

if __name__ == "__main__":
    # Start the Flask server in a new thread
    server_thread = threading.Thread(target=run_server)
    server_thread.start()

    # Give the server a moment to start
    time.sleep(3)

    # Open the default web browser to the Flask app
    webbrowser.open("http://127.0.0.1:5000")
