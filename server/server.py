from flask import Flask, request, jsonify
from flask_cors import CORS
from chatbot.response_engine import generate_chat_response

app = Flask(__name__)
CORS(app)   # ✅ IMPORTANT LINE

@app.route('/')
def home():
    return "Medical Chatbot Server Running!"

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    symptoms = data['symptoms']

    response = generate_chat_response(symptoms)

    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)