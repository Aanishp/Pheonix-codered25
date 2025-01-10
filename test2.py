from flask import Flask, request, jsonify
import openai
import PyPDF2
from docx import Document
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
# OpenAI API Key
openai.api_key = "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"

def extract_text_from_file(file):
    """Extract text from uploaded file (PDF or DOCX)."""
    if file.filename.endswith('.pdf'):
        pdf_reader = PyPDF2.PdfReader(file)
        return ''.join(page.extract_text() for page in pdf_reader.pages)
    elif file.filename.endswith('.docx'):
        doc = Document(file)
        return '\n'.join(paragraph.text for paragraph in doc.paragraphs)
    else:
        return None

@app.route('/upload-resume', methods=['POST'])
def upload_resume():
    file = request.files.get('resume')
    if not file:
        return jsonify({'error': 'No file uploaded'}), 400

    # Extract text from file
    resume_text = extract_text_from_file(file)
    if not resume_text:
        return jsonify({'error': 'Unsupported file type or empty file'}), 400

    # Analyze resume using OpenAI API
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an expert career advisor."},
                {"role": "user", "content": f"Analyze this resume and provide constructive feedback: {resume_text}"}
            ]
        )
        feedback = response['choices'][0]['message']['content']
        return jsonify({'feedback': feedback})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


app.run(debug=True)