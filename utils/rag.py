from utils.embeddings import EmbeddingModel
from utils.vector_store import VectorStore
from utils.llm import GeminiLLM
import streamlit as st


@st.cache_resource
def load_rag():

    return RAGPipeline()


class RAGPipeline:

    def __init__(self):

        self.embedding_model = EmbeddingModel()

        self.vector_store = VectorStore()

        self.llm = GeminiLLM()

    def ask(self, question, selected_documents=None):

        query_embedding = self.embedding_model.create_query_embedding(
            question
        )

        results = self.vector_store.search(
            query_embedding=query_embedding,
            selected_documents=selected_documents,
            n_results=6
        )

        if (
            not results
            or len(results["documents"]) == 0
            or len(results["documents"][0]) == 0
        ):

            return "I couldn't find the answer in the uploaded documents."

        context = "\n\n".join(results["documents"][0])

        return self.llm.generate_answer(
            context=context,
            question=question
        )
