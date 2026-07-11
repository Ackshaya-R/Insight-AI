import time
import streamlit as st

from utils.rag import load_rag
from utils.vector_store import VectorStore
from database.chat_history import ChatHistory


def show_chat():

    st.markdown("## 💬 Chat with Your Documents")

    # -----------------------------------
    # Document Selection
    # -----------------------------------

    vector_store = VectorStore()

    documents = vector_store.get_uploaded_files()

    if len(documents) == 0:

        st.info("📂 Upload documents to start chatting.")

        return

    st.markdown("### 📄 Select Documents")

    all_documents = st.checkbox(
        "All Documents",
        value=True
    )

    if all_documents:

        selected_documents = documents

    else:

        selected_documents = st.multiselect(
            "Choose Documents",
            documents,
            default=[]
        )

    st.markdown("---")

    # -----------------------------------
    # Quick Actions
    # -----------------------------------

    st.markdown("### ✨ Quick Actions")

    col1, col2 = st.columns(2)

    with col1:

        summarize = st.button(
            "📄 Summarize",
            use_container_width=True
        )

    with col2:

        keypoints = st.button(
            "📌 Key Points",
            use_container_width=True
        )

    col3, col4 = st.columns(2)

    with col3:

        quiz = st.button(
            "❓ Generate Quiz",
            use_container_width=True
        )

    with col4:

        interview = st.button(
            "🎯 Interview Questions",
            use_container_width=True
        )

    auto_question = None

    if summarize:

        auto_question = (
            "Summarize the selected documents."
        )

    elif keypoints:

        auto_question = (
            "Give the important key points from the selected documents."
        )

    elif quiz:

        auto_question = (
            "Generate 10 multiple-choice questions from the selected documents."
        )

    elif interview:

        auto_question = (
            "Generate interview questions with answers from the selected documents."
        )

    st.markdown("---")

    # -----------------------------------
    # Chat History
    # -----------------------------------

    if "messages" not in st.session_state:

        st.session_state.messages = []

    for message in st.session_state.messages:

        with st.chat_message(message["role"]):

            st.markdown(message["content"])

    # -----------------------------------
    # Chat Input
    # -----------------------------------

    typed_question = st.chat_input(
        "Ask anything about your selected documents..."
    )

    question = auto_question if auto_question else typed_question

    if question:

        if not selected_documents:

            st.warning(
                "Please select at least one document."
            )

            return

        st.session_state.messages.append(
            {
                "role": "user",
                "content": question
            }
        )

        with st.chat_message("user"):

            st.markdown(question)

        with st.chat_message("assistant"):

            with st.spinner(
                "🤖 InsightAI is thinking..."
            ):

                try:

                    rag = load_rag()

                    answer = rag.ask(
                        question,
                        selected_documents
                    )

                    # -----------------------------
                    # Typing Animation
                    # -----------------------------

                    placeholder = st.empty()

                    typed = ""

                    time.sleep(0.3)

                    for char in answer:

                        typed += char

                        placeholder.markdown(
                            typed + "▌"
                        )

                        time.sleep(0.01)

                    for _ in range(2):

                        placeholder.markdown(
                            typed + "▌"
                        )

                        time.sleep(0.15)

                        placeholder.markdown(
                            typed
                        )

                        time.sleep(0.15)

                    placeholder.markdown(
                        typed
                    )

                    ChatHistory().save_chat(
                        question,
                        answer
                    )

                    st.session_state.messages.append(
                        {
                            "role": "assistant",
                            "content": answer
                        }
                    )

                except Exception as e:

                    st.error(
                        "Unable to generate response."
                    )

                    st.exception(e)
