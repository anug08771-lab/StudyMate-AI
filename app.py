import streamlit as st
import os
from dotenv import load_dotenv

from utils.pdf_handler import extract_text_from_pdf, get_text_chunks
from utils.vector_store import create_vector_store
from utils.ai_generators import (
    generate_summary,
    generate_flashcards,
    generate_mcqs,
    generate_important_questions,
)
from utils.rag_qa import ask_question

# Load environment variables
load_dotenv()

st.set_page_config(
    page_title="StudyMate AI",
    page_icon="📚",
    layout="wide",
)

# ---------------- CSS ---------------- #

st.markdown("""
<style>
.flashcard{
    background:#ffffff;
    padding:20px;
    border-radius:12px;
    margin-bottom:20px;
    border:1px solid #e5e7eb;
    box-shadow:0 2px 8px rgba(0,0,0,0.05);
}
.flashcard h3{
    color:#2563eb;
}
</style>
""", unsafe_allow_html=True)

# ---------------- Header ---------------- #

st.title("📚 StudyMate AI")
st.markdown("##### Your Intelligent Study Companion powered by Groq + HuggingFace + LangChain")
st.divider()

# ---------------- Sidebar ---------------- #

with st.sidebar:

    st.header("⚙️ Configuration")

    api_key = st.text_input(
        "Enter Groq API Key",
        type="password",
        value=os.getenv("GROQ_API_KEY", "")
    )

    if not api_key:
        st.warning("Please enter your Groq API Key.")
        st.stop()

    st.header("📂 Upload PDF")

    uploaded_file = st.file_uploader(
        "Upload PDF",
        type=["pdf"]
    )

    if uploaded_file and st.button("Process Document", use_container_width=True):

        with st.spinner("Processing document..."):

            try:

                raw_text = extract_text_from_pdf(uploaded_file)

                # Build vector DB using FULL text
                text_chunks = get_text_chunks(raw_text)
                vector_store = create_vector_store(text_chunks, "")

                st.session_state["vector_store"] = vector_store

                # Store only a smaller portion for AI generation
                st.session_state["raw_text"] = raw_text[:8000]

                st.success("Document analyzed successfully!")

            except Exception as e:
                st.error(str(e))

# ---------------- Main ---------------- #

if "raw_text" in st.session_state and "vector_store" in st.session_state:

    raw_text = st.session_state["raw_text"]

    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📝 Summary",
        "🗂 Flashcards",
        "✅ MCQs",
        "❓ Exam Prep",
        "💬 Ask PDF",
    ])

    # ---------------- Summary ---------------- #

    with tab1:

        st.subheader("Document Summary")

        if st.button("Generate Summary"):

            with st.spinner("Generating Summary..."):

                st.markdown(
                    generate_summary(raw_text, api_key)
                )

    # ---------------- Flashcards ---------------- #

    with tab2:

        st.subheader("Flashcards")

        if st.button("Generate Flashcards"):

            with st.spinner("Generating Flashcards..."):

                cards = generate_flashcards(raw_text, api_key)

                for card in cards:

                    question = (
                        card.get("front")
                        or card.get("question")
                        or card.get("term")
                        or "Question"
                    )

                    answer = (
                        card.get("back")
                        or card.get("answer")
                        or card.get("definition")
                        or ""
                    )

                    st.markdown(f"""
<div class="flashcard">
<h3>{question}</h3>
<p>{answer}</p>
</div>
""", unsafe_allow_html=True)

    # ---------------- MCQs ---------------- #

    with tab3:

        st.subheader("MCQs")

        if st.button("Generate MCQs"):

            with st.spinner("Generating MCQs..."):

                mcqs = generate_mcqs(raw_text, api_key)

                for i, mcq in enumerate(mcqs):

                    st.markdown(f"### Q{i+1}. {mcq['question']}")

                    for option in mcq["options"]:
                        st.write("•", option)

                    with st.expander("Show Answer"):

                        st.success(mcq["answer"])

                        if "explanation" in mcq:
                            st.info(mcq["explanation"])

                    st.divider()

    # ---------------- Exam Prep ---------------- #

    with tab4:

        st.subheader("Important Questions")

        if st.button("Generate Questions"):

            with st.spinner("Generating Questions..."):

                st.write(
                    generate_important_questions(
                        raw_text,
                        api_key
                    )
                )

    # ---------------- Ask PDF ---------------- #

    with tab5:

        st.subheader("Ask PDF")

        question = st.text_input(
            "Ask anything about the uploaded PDF"
        )

        if question:

            with st.spinner("Searching..."):

                answer = ask_question(
                    question,
                    st.session_state["vector_store"],
                    api_key
                )

                st.success(answer)

else:

    st.info("👈 Upload a PDF and click Process Document.")