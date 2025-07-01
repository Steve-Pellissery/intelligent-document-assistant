from flask import Flask, render_template, request
import os
import fitz  # PyMuPDF
from transformers import pipeline

app = Flask(__name__)

# ✅ Load lightweight DistilBERT QA model (Render-safe)
qa_pipeline = pipeline(
    "question-answering",
    model="distilbert-base-cased-distilled-squad"
)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    if file:
        if not os.path.exists('uploads'):
            os.makedirs('uploads')
        filepath = os.path.join('uploads', file.filename)
        file.save(filepath)

        # Extract text from PDF
        text = ""
        if file.filename.endswith('.pdf'):
            doc = fitz.open(filepath)
            for page in doc:
                text += page.get_text()
            doc.close()

        return render_template("index.html", extracted_text=text)

    return "No file uploaded."

@app.route('/ask', methods=['POST'])
def ask():
    context = request.form['context']
    question = request.form['question']

    result = qa_pipeline(question=question, context=context)
    answer = result['answer']

    return render_template("index.html", extracted_text=context, answer=answer)

if __name__ == '__main__':
    app.run(debug=True)
