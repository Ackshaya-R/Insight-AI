import streamlit as st

from config import config
from assets.styles import load_css

from ui.sidebar import show_sidebar
from ui.dashboard import show_dashboard
from ui.uploader import show_uploader
from ui.chat import show_chat
from ui.footer import show_footer


# -------------------------------------------------
# Page Configuration
# -------------------------------------------------

st.set_page_config(
    page_title=config.APP_NAME,
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -------------------------------------------------
# Load Custom CSS
# -------------------------------------------------

load_css()

# -------------------------------------------------
# Session State
# -------------------------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

# -------------------------------------------------
# Sidebar
# -------------------------------------------------

show_sidebar()

# -------------------------------------------------
# Header
# -------------------------------------------------

st.markdown(
    """
    <div style='text-align:center;padding:10px;'>

    <h1 style='color:#2563EB;font-size:48px;'>
        🤖 InsightAI
    </h1>

    <p style='font-size:20px;color:#64748B;'>

        AI Powered Document Intelligence System

    </p>

    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

# -------------------------------------------------
# Upload Documents
# -------------------------------------------------

uploaded_files = show_uploader()

# -------------------------------------------------
# Dashboard
# -------------------------------------------------

show_dashboard(uploaded_files)

# -------------------------------------------------
# Chat
# -------------------------------------------------

show_chat()

# -------------------------------------------------
# Footer
# -------------------------------------------------

show_footer()