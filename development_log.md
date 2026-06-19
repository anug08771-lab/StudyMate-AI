Development Log – StudyMate AI

Project Name

StudyMate AI

Developer

Anushka Gouda

Challenge

AI Vibe Coding Challenge 2026

---

Problem Statement

Students spend a significant amount of time reading lengthy PDF notes before examinations. Finding important concepts, creating revision material, and preparing practice questions manually is time-consuming.

StudyMate AI solves this problem by automatically converting study PDFs into AI-generated summaries, flashcards, multiple-choice questions, important exam questions, and an interactive RAG-based question-answering system.

---

AI Coding Assistants Used

- ChatGPT (GPT-5.5)
- Groq Console
- Gemini pro extended thinking 

---

AI Models Used

- Groq Llama-3.3-70B-Versatile
- sentence-transformers/all-MiniLM-L6-v2 (Embeddings)

---

Technologies Used

- Python
- Streamlit
- LangChain
- ChromaDB
- HuggingFace Embeddings
- PyPDF
- Groq API

---

Development Timeline

Phase 1

- Project planning
- Folder structure creation
- Streamlit setup

Phase 2

- PDF text extraction
- Text chunking
- Vector database integration

Phase 3

- Groq AI integration
- Summary generation
- Flashcard generation
- MCQ generation
- Important question generation

Phase 4

- Retrieval-Augmented Generation (RAG)
- Ask PDF feature
- UI improvements
- Testing

---

Important AI Prompts Used

- Generate a comprehensive summary from the uploaded PDF.
- Generate educational flashcards in JSON format.
- Generate multiple-choice questions with explanations.
- Generate important subjective examination questions.
- Answer user questions strictly using the uploaded document.

---

AI Generated Code

AI assistance was used for:

- Streamlit UI generation
- LangChain integration
- Groq API integration
- ChromaDB vector database implementation
- HuggingFace embedding integration
- PDF parsing
- Prompt engineering
- RAG implementation
- Error handling
- JSON parsing

---

Manual Modifications

The following modifications were made manually:

- Replaced Google Gemini with Groq due to API quota limitations.
- Switched embeddings to HuggingFace local embeddings.
- Improved prompt templates.
- Added JSON validation.
- Fixed dependency conflicts.
- Resolved ChromaDB persistence issues.
- Optimized token usage for Groq.
- Improved UI and flashcard rendering.
- Corrected RAG retrieval workflow.

---

Challenges Faced

- Google Gemini API quota limitations.
- LangChain package compatibility issues.
- ChromaDB database initialization errors.
- Token limit exceeded while processing large PDFs.
- JSON parsing inconsistencies from LLM responses.
- Groq integration and dependency management.
- RAG retrieval debugging.

---

Solutions Implemented

- Migrated from Gemini to Groq.
- Used HuggingFace local embedding model.
- Added persistent ChromaDB vector storage.
- Limited prompt size to avoid token overflow.
- Improved JSON extraction and validation.
- Updated project dependencies.
- Implemented proper exception handling.

---

Lessons Learned

This project provided practical experience in:

- Retrieval-Augmented Generation (RAG)
- Large Language Model integration
- Prompt Engineering
- Vector Databases
- Embedding Models
- AI-assisted software development
- Dependency management
- Debugging real-world AI applications

---

Future Improvements

- Multi-document support
- Voice input
- Voice output
- User authentication
- Cloud deployment
- PDF export
- Quiz progress tracking
- Dark mode
- OCR support for scanned PDFs

---

Final Outcome

A fully functional AI-powered study assistant capable of:

- Uploading PDF documents
- Generating summaries
- Creating flashcards
- Generating MCQs
- Predicting important exam questions
- Answering questions using Retrieval-Augmented Generation (RAG)

The application successfully meets the objectives of the AI Vibe Coding Challenge 2026.