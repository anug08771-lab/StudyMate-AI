import logging
from pypdf import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter

def extract_text_from_pdf(pdf_file):
    """Extracts and concatenates text from an uploaded PDF file."""
    try:
        reader = PdfReader(pdf_file)
        text = "".join(page.extract_text() or "" for page in reader.pages)
        if not text.strip():
            raise ValueError("No extractable text found. The PDF might be scanned or image-based.")
        return text
    except Exception as e:
        logging.error(f"PDF Extraction Error: {e}")
        raise e

def get_text_chunks(text, chunk_size=1000, chunk_overlap=200):
    """Splits large text into smaller, overlapping chunks for effective embedding."""
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n\n", "\n", " ", ""]
    )
    return text_splitter.split_text(text)