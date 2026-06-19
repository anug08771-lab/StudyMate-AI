📚 StudyMate AI

An AI-powered study assistant that transforms PDF study materials into interactive learning resources using Retrieval-Augmented Generation (RAG), Groq LLM, HuggingFace Embeddings, and ChromaDB.

StudyMate AI helps students prepare for exams faster by automatically generating summaries, flashcards, multiple-choice questions, important exam questions, and allowing users to chat with their study material.

---

🚀 Features

- 📄 Upload PDF study materials
- 📝 AI-generated comprehensive summaries
- 🎴 Smart flashcards for quick revision
- ✅ AI-generated MCQs with explanations
- 📚 Important exam question prediction
- 💬 Ask questions directly from the uploaded PDF using RAG
- ⚡ Fast AI responses using Groq Llama 3.3
- 🧠 Semantic document search using HuggingFace Embeddings
- 🗂️ ChromaDB vector database integration

---

🏗️ System Architecture

PDF Upload
     │
     ▼
Text Extraction (PyPDF)
     │
     ▼
Text Chunking
     │
     ▼
HuggingFace Embeddings
     │
     ▼
ChromaDB Vector Store
     │
     ├──────────────► RAG Question Answering
     │                    │
     │                    ▼
     │              Groq Llama 3.3
     │
     ▼
Groq Llama 3.3
     │
     ├── Summary
     ├── Flashcards
     ├── MCQs
     └── Important Questions

---

🛠️ Tech Stack

Frontend

- Streamlit

Backend

- Python

AI Model

- Groq (Llama-3.3-70B-Versatile)

Framework

- LangChain

Embedding Model

- sentence-transformers/all-MiniLM-L6-v2

Vector Database

- ChromaDB

PDF Processing

- PyPDF

---

📂 Project Structure

StudyMateAI/
│
├── app.py
├── requirements.txt
├── README.md
├── development_log.md
│
├── screenshots/
│
└── utils/
    ├── ai_generators.py
    ├── pdf_handler.py
    ├── rag_qa.py
    └── vector_store.py

---

⚙️ Installation

git clone <repository-url>

cd StudyMateAI

pip install -r requirements.txt

streamlit run app.py

---

📖 Usage

1. Launch the application.
2. Enter your Groq API Key.
3. Upload a PDF.
4. Click Process Document.
5. Use any of the available AI features:
   - Summary
   - Flashcards
   - MCQs
   - Important Questions
   - Ask PDF

---

📸 Screenshots

Include screenshots of:

- Home Page
- Summary
- Flashcards
- MCQs
- Important Questions
- Ask PDF (RAG)

---

🌟 Future Enhancements

- Multi-PDF support
- Voice-based Q&A
- User Authentication
- Cloud Deployment
- Quiz Difficulty Levels
- PDF Export
- Study Progress Tracking
- Mobile Responsive UI

---

👩‍💻 Developed By

Anushka Gauda

B.Tech Computer Science & Engineering

Silicon University

---

📜 License

This project was developed for the AI Vibe Coding Challenge 2026 as part of the Applied AI Summer Internship.