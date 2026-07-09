import streamlit as st
from utils.vector_store import VectorStore


def show_dashboard(uploaded_files):

    st.markdown("## 📊 Dashboard")

    col1, col2, col3, col4 = st.columns(4)

    # -----------------------------
    # Documents
    # -----------------------------
    with col1:

        st.metric(
            label="📄 Documents",
            value=len(uploaded_files)
        )

    # -----------------------------
    # Chunks
    # -----------------------------
    with col2:

        try:

            store = VectorStore()

            chunks = store.count()

        except:

            chunks = 0

        st.metric(
            label="🧠 Chunks",
            value=chunks
        )

    # -----------------------------
    # Chat Count
    # -----------------------------
    with col3:

        chats = len(
            st.session_state.get("messages", [])
        )

        st.metric(
            label="💬 Chats",
            value=chats
        )

    # -----------------------------
    # AI Model
    # -----------------------------
    with col4:

        st.metric(
            label="🤖 Model",
            value="Gemini"
        )

    st.markdown("---")