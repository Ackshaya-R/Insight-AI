from utils.embeddings import EmbeddingModel
from utils.vector_store import VectorStore
from utils.llm import GeminiLLM


class RAGPipeline:

    def __init__(self):

        self.embedding_model = EmbeddingModel()

        self.vector_store = VectorStore()

        self.llm = GeminiLLM()

    def ask(
        self,
        question,
        selected_documents=None
    ):

        # -----------------------------
        # Create Query Embedding
        # -----------------------------

        query_embedding = (
            self.embedding_model.create_query_embedding(
                question
            )
        )

        # -----------------------------
        # Search ChromaDB
        # -----------------------------

        results = self.vector_store.search(
            query_embedding=query_embedding,
            selected_documents=selected_documents,
            n_results=6
        )

        # -----------------------------
        # No Documents Found
        # -----------------------------

        if (
            not results
            or len(results["documents"]) == 0
            or len(results["documents"][0]) == 0
        ):

            return (
                "I couldn't find the answer in the selected document(s)."
            )

        # -----------------------------
        # Merge Retrieved Chunks
        # -----------------------------

        documents = results["documents"][0]

        context = "\n\n".join(
            documents
        )

        # -----------------------------
        # Generate Gemini Response
        # -----------------------------

        answer = self.llm.generate_answer(
            context=context,
            question=question
        )

        return answer