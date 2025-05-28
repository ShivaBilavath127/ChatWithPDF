from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import fitz  # PyMuPDF
import requests

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Replace with your free Together API Key
TOGETHER_API_KEY = "071b3499bfc66371b3dea071d0d625d2562d71897228c38ea9a5bae978beeac9"

pdf_text = ""  # Global variable to hold PDF content

# Extract text from PDF
def extract_text_from_pdf(file_path):
    doc = fitz.open(file_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

# Route to upload PDF
@app.route('/upload', methods=['POST'])
def upload_pdf():
    global pdf_text
    if 'pdf' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['pdf']
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    pdf_text = extract_text_from_pdf(file_path)
    return jsonify({'message': 'PDF uploaded and text extracted successfully'}), 200

# Route to ask questions
@app.route('/ask', methods=['POST'])
def ask_question():
    global pdf_text
    data = request.get_json()
    user_question = data.get('question', '')

    prompt = f"""You are an AI assistant. Answer the question based on the PDF content below:

PDF Content:
{pdf_text[:4000]}  # Limit to avoid token overflow

Question: {user_question}
Answer:"""

    headers = {
        "Authorization": f"Bearer {TOGETHER_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "mistralai/Mistral-7B-Instruct-v0.1",
        "prompt": prompt,
        "max_tokens": 200,
        "temperature": 0.7,
        "top_p": 0.9,
        "top_k": 50,
        "repetition_penalty": 1.1,
        "stop": ["<|endoftext|>"]
    }

    response = requests.post("https://api.together.xyz/inference", headers=headers, json=payload)

    if response.status_code == 200:
        output = response.json()['output']['choices'][0]['text']
        return jsonify({'answer': output.strip()}), 200
    else:
        return jsonify({'error': 'API Error', 'details': response.text}), 500

if __name__ == '__main__':
    app.run(debug=True)
