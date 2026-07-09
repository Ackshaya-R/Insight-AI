from sentence_transformers import SentenceTransformer
from config import config


class EmbeddingModel:

    def __init__(self):

        self.model = SentenceTransformer(
            config.EMBEDDING_MODEL
        )

    def create_embeddings(self, chunks):

        if len(chunks) == 0:
            return []

        embeddings = self.model.encode(
            chunks,
            convert_to_numpy=True,
            show_progress_bar=True
        )

        return embeddings.tolist()

    def create_query_embedding(self, query):

        embedding = self.model.encode(
            query,
            convert_to_numpy=True
        )

        return embedding.tolist()