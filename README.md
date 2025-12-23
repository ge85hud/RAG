# Educational RAG System

This project is a simple **Retrieval-Augmented Generation (RAG)** system for education.  
It builds a knowledge base from **academic papers (PDF)** and **lecture slides (PPTX)** and allows users to ask questions based on the stored content.

---

## What This Project Does

- Reads papers and lecture slides
- Splits them into chunks
- Converts chunks into embeddings (vectors)
- Stores embeddings persistently
- Retrieves the most relevant chunks for a question
- Uses an open-source LLM to generate answers

---

## Project Structure

src/
├── ingestion/
│ ├── papers/
│ └── slides/
├── retrieval/
data/ # ignored by git
README.md
requirements.txt

---

## Setup

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd YOUR_REPO
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
Data
Put your files here:

bash
Copy code
data/papers/   # PDF files
data/ppt/      # PPTX files
The data/ folder is not pushed to GitHub.

Ingest Slides
bash
Copy code
python -m src.ingestion.slides.test_real_ppt_embedding
This will embed slides and save vectors locally.

Ask Questions
bash
Copy code
python -m src.retrieval.ask_question
The system retrieves the top 3 relevant chunks and generates an answer.

Models Used
Embeddings: all-MiniLM-L6-v2

LLM: google/flan-t5-base

Both are open-source and run locally.

Notes
The knowledge base is persistent (new data is added, not removed)

Papers and slides share the same vector store

Designed for learning and experimentation

License
Educational use only.

Copy code

