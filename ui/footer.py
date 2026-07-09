import streamlit as st


def show_footer():

    st.markdown("---")

    st.markdown(
        """
        <div style="text-align:center;padding:15px;color:gray;">

        <b>🤖 InsightAI Version 3.0</b>

        <br><br>

        Powered by ❤️ Python • Streamlit • Gemini • LangChain • ChromaDB

        </div>
        """,
        unsafe_allow_html=True
    )