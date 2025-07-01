# Intelligent Document Assistant

A conversational AI system that extracts and answers questions from uploaded documents using BERT.

## Features

- Upload PDF or text documents
- Extracts text using PyMuPDF
- Uses a BERT-based QA model for answers
- Built with Flask, Transformers, and HTML

## How to Run

```bash
git clone https://github.com/YOUR-USERNAME/intelligent-document-assistant.git
cd intelligent-document-assistant
python -m venv venv
venv\Scripts\activate  # or source venv/bin/activate
pip install -r requirements.txt
python app.py
