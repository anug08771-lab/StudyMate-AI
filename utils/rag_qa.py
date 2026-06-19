import os
import logging

from langchain_groq import ChatGroq
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate


def ask_question(question, vector_store, api_key):
    """RAG pipeline using Groq + ChromaDB"""

    try:
        # Use Groq API key
        groq_key = api_key or os.getenv("GROQ_API_KEY")

        llm = ChatGroq(
            model="llama-3.3-70b-versatile",
            groq_api_key=groq_key,
            temperature=0.2,
        )

        retriever = vector_store.as_retriever(
            search_kwargs={"k": 5}
        )

        system_prompt = """
You are an expert AI teaching assistant.

Answer ONLY using the provided context.

If the answer is not found in the context,
say:

'I could not find that information in the uploaded document.'

Context:

{context}
"""

        prompt = ChatPromptTemplate.from_messages(
            [
                ("system", system_prompt),
                ("human", "{input}"),
            ]
        )

        document_chain = create_stuff_documents_chain(
            llm,
            prompt,
        )

        retrieval_chain = create_retrieval_chain(
            retriever,
            document_chain,
        )

        response = retrieval_chain.invoke(
            {"input": question}
        )

        return response["answer"]

    except Exception as e:
        logging.error(f"RAG QA Error: {e}")
        return str(e)