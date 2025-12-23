# Educational RAG System (Papers & Lecture Slides)

This project implements a **Retrieval-Augmented Generation (RAG)** system for educational use cases.  
It builds a **persistent knowledge base** from academic papers and lecture slides and allows users to ask questions that are answered using retrieved relevant content and an open-source large language model (LLM).

---

## 🚀 Features

- Ingestion pipelines for:
  - 📄 Academic papers (PDF)
  - 📊 Lecture slides (PPTX)
- Chunk-based representation of educational content
- Dense vector embeddings using Sentence Transformers
- Persistent, append-only vector storage
- Unified knowledge base for papers and slides
- Semantic retrieval (Top-K similarity search)
- Question answering using an open-source LLM
- Fully local execution (no external APIs required)

---

## 🧠 System Architecture

Documents (PDF / PPTX)
↓
Chunking
↓
Embedding
↓
Persistent Vector Store
↓
Similarity Search (Top-K)
↓
Open-Source LLM Answer

yaml
Copy code

---

## 📁 Project Structure

.
├── src/
│ ├── ingestion/
│ │ ├── papers/
│ │ │ ├── academic_chunker.py
│ │ │ ├── embed_chunks.py
│ │ │ └── persistent_vector_store.py
│ │ └── slides/
│ │ ├── slide_chunker.py
│ │ ├── slide_embedding.py
│ │ └── test_real_ppt_embedding.py
│ ├── retrieval/
│ │ ├── rag_qa.py
│ │ └── ask_question.py
│ └── init.py
│
├── data/
│ └── .gitkeep
│
├── .gitignore
├── README.md
└── requirements.txt

yaml
Copy code

---

## 🔒 Data Privacy

The `data/` directory is intentionally **excluded from version control**.

It may contain:
- PDF papers
- PPTX lecture slides
- Vector embeddings (`.npy`)
- Persistent knowledge base files

Each user must provide their own local data.

---

## 📦 Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd YOUR_REPO
2️⃣ Create and activate a virtual environment
bash
Copy code
python -m venv venv
venv\Scripts\activate
3️⃣ Install dependencies
bash
Copy code
pip install -r requirements.txt
📊 Ingest Lecture Slides
Place your lecture slides in:

bash
Copy code
data/ppt/
Then run:

bash
Copy code
python -m src.ingestion.slides.test_real_ppt_embedding
This will:

Load slide chunks

Embed them into vectors

Append them to the persistent knowledge base

❓ Ask Questions (RAG)
After ingesting papers and/or slides, run:

bash
Copy code
python -m src.retrieval.ask_question
The system will:

Embed the user question

Retrieve the top-3 most relevant chunks

Send the question and retrieved chunks to an open-source LLM

Generate an answer grounded in the stored knowledge

🤖 Models Used
Embedding Model
sentence-transformers/all-MiniLM-L6-v2

LLM
google/flan-t5-base

Both models are open source and runnable locally on CPU.

🧪 Persistent Storage
All vectors and chunks are stored in:

bash
Copy code
data/vector_store/index/
├── embeddings.npy
├── chunks.npy
└── metadata.npy
The storage is append-only — previously stored data is never removed.

📌 Notes
Papers and slides share the same vector space

Metadata distinguishes document type and source

Designed for extensibility and research use

Suitable for educational QA systems

🛠️ Future Improvements
FAISS-based indexing for faster retrieval

Metadata-based filtering (papers-only / slides-only)

Source citation in generated answers

Web UI (Streamlit or FastAPI)

Multi-course knowledge base support

📜 License
This project is intended for educational and research purposes.
Ensure you have the appropriate rights to use any documents you ingest.
