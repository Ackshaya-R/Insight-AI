from sentence_transformers import SentenceTransformer
from config import config
import streamlit as st


@st.cache_resource
def load_embedding_model():
    return SentenceTransformer(config.EMBEDDING_MODEL)


class EmbeddingModel:

    def __init__(self):
        self.model = load_embedding_model()

    def create_embeddings(self, chunks):

        if not chunks:
            return []

        embeddings = self.model.encode(
            chunks,
            convert_to_numpy=True,
            show_progress_bar=False
        )

        return embeddings.tolist()

    def create_query_embedding(self, query):

        embedding = self.model.encode(
            query,
            convert_to_numpy=True
        )

        return embedding.tolist()
