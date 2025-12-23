# Educational RAG System (Papers & Lecture Slides)

This project implements a **Retrieval-Augmented Generation (RAG)** system for educational use cases.  
It builds a **persistent knowledge base** from:

- 📄 Academic papers (PDF)
- 📊 Lecture slides (PPTX)

and allows users to ask questions that are answered using **retrieved relevant chunks** and an **open-source LLM**.

---

## 🚀 Features

- Separate ingestion pipelines for:
  - Academic papers
  - Lecture slides
- Enhanced chunking strategy for educational content
- Dense vector embeddings using Sentence Transformers
- Persistent, append-only vector storage
- Unified knowledge base for papers and slides
- Question answering via RAG (retrieval + LLM)
- No external APIs required (fully local & open source)

---

## 🧠 System Architecture
