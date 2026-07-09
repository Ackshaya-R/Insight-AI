import hashlib
import streamlit as st

from utils.file_loader import FileLoader
from utils.helper import save_uploaded_file
from utils.splitter import DocumentSplitter
from utils.embeddings import EmbeddingModel
from utils.vector_store import VectorStore


def show_uploader():

    st.markdown("## 📂 Upload Documents")

    uploaded_files = st.file_uploader(
        "Choose PDF, DOCX or TXT files",
        type=["pdf", "docx", "txt"],
        accept_multiple_files=True
    )

    if not uploaded_files:
        return []

    splitter = DocumentSplitter()
    embedding_model = EmbeddingModel()
    vector_store = VectorStore()

    processed_files = []

    progress_bar = st.progress(0)

    status = st.empty()

    total = len(uploaded_files)

    for index, uploaded_file in enumerate(uploaded_files):

        try:

            status.info(
                f"Processing {uploaded_file.name}..."
            )

            # Calculate SHA-256 hash
            file_bytes = uploaded_file.getvalue()

            file_hash = hashlib.sha256(
                file_bytes
            ).hexdigest()

            # Duplicate check
            if vector_store.document_exists(file_hash):

                st.warning(
                    f"⚠ '{uploaded_file.name}' is already uploaded."
                )

                progress_bar.progress(
                    (index + 1) / total
                )

                continue

            # Save file
            file_path = save_uploaded_file(
                uploaded_file
            )

            # Read document
            text = FileLoader.load(
                file_path
            )

            # Preview
            with st.expander(
                f"📄 {uploaded_file.name}"
            ):

                st.text_area(
                    "Preview",
                    text,
                    height=250,
                    key=uploaded_file.name
                )

            # Split
            chunks = splitter.split(text)

            st.info(
                f"📑 {len(chunks)} chunks created"
            )

            # Embeddings
            embeddings = embedding_model.create_embeddings(
                chunks
            )

            st.success(
                "🧠 Embeddings Generated"
            )

            # Store
            vector_store.add_documents(
                chunks,
                embeddings,
                uploaded_file.name,
                file_hash
            )

            st.success(
                "✅ Stored in ChromaDB"
            )

            processed_files.append(
                uploaded_file
            )

            progress_bar.progress(
                (index + 1) / total
            )

        except Exception as e:

            st.error(
                f"Error processing {uploaded_file.name}"
            )

            st.exception(e)

    status.success(
        "🎉 Upload completed!"
    )

    st.markdown("---")

    return processed_files