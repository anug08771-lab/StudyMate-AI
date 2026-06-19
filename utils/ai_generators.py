import json
import logging
import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate

# Configure standard logger
logger = logging.getLogger(__name__)

def get_llm(api_key: str = None) -> ChatGroq:
    """
    Initializes and returns the ChatGroq LLM instance.
    Falls back to the GROQ_API_KEY environment variable if no key is provided.
    """
    try:
        groq_api_key = api_key or os.environ.get("GROQ_API_KEY")
        if not groq_api_key:
            raise ValueError("Groq API key must be provided either via arguments or GROQ_API_KEY environment variable.")

        llm = ChatGroq(
            model="llama-3.3-70b-versatile",
            api_key=groq_api_key,
            temperature=0.2, # Lower temperature for better JSON consistency
        )
        return llm
    except Exception as e:
        logger.error(f"Error initializing Groq LLM: {e}")
        raise

def _extract_json_string(raw_response: str) -> str:
    """
    Helper function to safely extract JSON strings from LLM responses 
    that might be padded with markdown blocks (e.g., ```json ... ```).
    """
    cleaned = raw_response.strip()
    if cleaned.startswith("```json"):
        cleaned = cleaned[7:]
    elif cleaned.startswith("```"):
        cleaned = cleaned[3:]
    
    if cleaned.endswith("```"):
        cleaned = cleaned[:-3]
        
    return cleaned.strip()

def generate_summary(text: str, api_key: str = None) -> str:
    """
    Generates a concise summary of the provided text.
    """
    try:
        llm = get_llm(api_key)
        prompt = PromptTemplate(
            input_variables=["text"],
            template="Please provide a comprehensive and concise summary of the following text:\n\n{text}\n\nSummary:"
        )
        chain = prompt | llm
        response = chain.invoke({"text": text})
        return response.content.strip()
    except Exception as e:
        logger.error(f"Error generating summary: {e}")
        raise

def generate_flashcards(text: str, api_key: str = None) -> list:
    """
    Generates flashcards from the text and returns them as parsed JSON (a list of dicts).
    """
    try:
        llm = get_llm(api_key)
        prompt = PromptTemplate(
            input_variables=["text"],
            template=(
                "Generate highly effective flashcards based on the following text.\n"
                "You must output ONLY a valid JSON array of objects. "
                "Each object must have a 'front' (the question or concept) and a 'back' (the answer or definition).\n"
                "Do not include any explanations, markdown formatting, or preamble.\n\n"
                "Text:\n{text}\n\nJSON Output:"
            )
        )
        chain = prompt | llm
        response = chain.invoke({"text": text})

        json_str = _extract_json_string(response.content)
        return json.loads(json_str)
    
    except json.JSONDecodeError as e:
        logger.error(f"JSON parsing error in generate_flashcards: {e}. Raw content: {response.content}")
        raise
    except Exception as e:
        logger.error(f"Error generating flashcards: {e}")
        raise

def generate_mcqs(text: str, api_key: str = None) -> list:
    """
    Generates multiple choice questions from the text and returns them as parsed JSON (a list of dicts).
    """
    try:
        llm = get_llm(api_key)
        prompt = PromptTemplate(
            input_variables=["text"],
            template=(
                "Generate challenging multiple choice questions (MCQs) based on the following text.\n"
                "You must output ONLY a valid JSON array of objects. "
                "Each object must strictly match this structure: "
                "{{\"question\": \"...\", \"options\": [\"A. ...\", \"B. ...\", \"C. ...\", \"D. ...\"], \"answer\": \"...\"}}\n"
                "Do not include any explanations, markdown formatting, or preamble.\n\n"
                "Text:\n{text}\n\nJSON Output:"
            )
        )
        chain = prompt | llm
        response = chain.invoke({"text": text})

        json_str = _extract_json_string(response.content)
        return json.loads(json_str)
        
    except json.JSONDecodeError as e:
        logger.error(f"JSON parsing error in generate_mcqs: {e}. Raw content: {response.content}")
        raise
    except Exception as e:
        logger.error(f"Error generating MCQs: {e}")
        raise

def generate_important_questions(text: str, api_key: str = None) -> str:
    """
    Generates a list of important short/long answer questions based on the text.
    """
    try:
        llm = get_llm(api_key)
        prompt = PromptTemplate(
            input_variables=["text"],
            template=(
                "Based on the following text, generate a list of the most important questions "
                "that a student or reader should be able to answer to demonstrate their full understanding.\n\n"
                "Text:\n{text}\n\nImportant Questions:"
            )
        )
        chain = prompt | llm
        response = chain.invoke({"text": text})
        return response.content.strip()
    except Exception as e:
        logger.error(f"Error generating important questions: {e}")
        raise