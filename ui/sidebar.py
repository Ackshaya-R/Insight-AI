import streamlit as st

from database.chat_history import ChatHistory


def show_sidebar():

    history = ChatHistory()

    with st.sidebar:

        st.title("🤖 InsightAI")

        st.caption("AI Document Assistant")

        st.markdown("---")

        # New Chat
        if st.button(
            "➕ New Chat",
            use_container_width=True
        ):

            st.session_state.messages = []

            st.rerun()

        st.markdown("---")

        st.subheader("💬 Chat History")

        chats = history.get_recent_questions(limit=20)

        if len(chats) == 0:

            st.info("No chats yet.")

        else:

            for chat in chats:

                chat_id = chat[0]

                question = chat[1]

                created = chat[2]

                # Show only first 35 characters
                if len(question) > 35:

                    question = question[:35] + "..."

                st.button(
                    f"💬 {question}",
                    key=f"chat_{chat_id}",
                    use_container_width=True
                )

        st.markdown("---")

        if st.button(
            "🗑 Clear History",
            use_container_width=True
        ):

            history.clear_history()

            st.success("History Cleared")

            st.rerun()

        st.markdown("---")

        st.caption("InsightAI v3.0")
