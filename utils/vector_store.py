import logging
import os

from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_core.documents import Document


def create_vector_store(text_chunks, api_key):
    """
    Creates a persistent ChromaDB vector store using HuggingFace embeddings.
    """

    try:
        # Local embedding model (FREE)
        embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2",
            model_kwargs={"device": "cpu"},
            encode_kwargs={"normalize_embeddings": True},
        )

        # Convert text chunks into documents
        documents = [Document(page_content=chunk) for chunk in text_chunks]

        # Create persistent directory
        persist_dir = "chroma_db"
        os.makedirs(persist_dir, exist_ok=True)

        # Create vector store
        vector_store = Chroma.from_documents(
            documents=documents,
            embedding=embeddings,
            collection_name="studymate_collection",
            persist_directory=persist_dir,
        )

        return vector_store

    except Exception as e:
        logging.error(f"Vector Store Error: {e}")
        raise