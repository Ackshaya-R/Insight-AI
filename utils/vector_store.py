import uuid
import chromadb

from config import config


class VectorStore:

    def __init__(self):

        self.client = chromadb.PersistentClient(
            path=config.CHROMA_DB
        )

        self.collection = self.client.get_or_create_collection(
            name="documents"
        )

    # ------------------------------------
    # Add Documents
    # ------------------------------------

    def add_documents(
        self,
        chunks,
        embeddings,
        filename,
        file_hash
    ):

        ids = [
            str(uuid.uuid4())
            for _ in chunks
        ]

        metadatas = [
            {
                "source": filename,
                "file_hash": file_hash
            }
            for _ in chunks
        ]

        self.collection.add(
            ids=ids,
            documents=chunks,
            embeddings=embeddings,
            metadatas=metadatas
        )

    # ------------------------------------
    # Duplicate Check
    # ------------------------------------

    def document_exists(
        self,
        file_hash
    ):

        results = self.collection.get(
            where={
                "file_hash": file_hash
            }
        )

        return len(results["ids"]) > 0

    # ------------------------------------
    # Search Documents
    # ------------------------------------

    def search(
        self,
        query_embedding,
        selected_documents=None,
        n_results=6
    ):

        # Search all documents

        if (
            not selected_documents
            or "All Documents" in selected_documents
        ):

            return self.collection.query(
                query_embeddings=[query_embedding],
                n_results=n_results,
                include=[
                    "documents",
                    "metadatas",
                    "distances"
                ]
            )

        # ----------------------------
        # Search selected documents
        # ----------------------------

        all_results = []

        for document in selected_documents:

            result = self.collection.query(
                query_embeddings=[query_embedding],
                where={
                    "source": document
                },
                n_results=n_results,
                include=[
                    "documents",
                    "metadatas",
                    "distances"
                ]
            )

            if len(result["documents"][0]) > 0:

                for i in range(
                    len(result["documents"][0])
                ):

                    all_results.append(
                        (
                            result["documents"][0][i],
                            result["metadatas"][0][i],
                            result["distances"][0][i]
                        )
                    )

        # No documents found

        if len(all_results) == 0:

            return {
                "documents": [[]],
                "metadatas": [[]],
                "distances": [[]]
            }

        # ----------------------------
        # Sort by similarity
        # ----------------------------

        all_results.sort(
            key=lambda x: x[2]
        )

        documents = []
        metadatas = []
        distances = []

        for doc, meta, dist in all_results[:n_results]:

            documents.append(doc)
            metadatas.append(meta)
            distances.append(dist)

        return {
            "documents": [documents],
            "metadatas": [metadatas],
            "distances": [distances]
        }

    # ------------------------------------
    # Statistics
    # ------------------------------------

    def count(self):

        return self.collection.count()

    # ------------------------------------
    # Delete All
    # ------------------------------------

    def delete_all(self):

        data = self.collection.get()

        if data["ids"]:

            self.collection.delete(
                ids=data["ids"]
            )

    # ------------------------------------
    # Uploaded Files
    # ------------------------------------

    def get_uploaded_files(self):

        data = self.collection.get(
            include=["metadatas"]
        )

        files = set()

        for metadata in data["metadatas"]:

            files.add(
                metadata["source"]
            )

        return sorted(list(files))