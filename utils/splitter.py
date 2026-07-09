from langchain.text_splitter import RecursiveCharacterTextSplitter


class DocumentSplitter:
    """
    Splits large documents into smaller chunks
    suitable for embedding generation.
    """

    def __init__(
        self,
        chunk_size=500,
        chunk_overlap=100
    ):

        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            length_function=len
        )

    def split(self, text: str):

        if not text:
            return []

        return self.splitter.split_text(text)