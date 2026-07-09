from pathlib import Path
from pypdf import PdfReader
from docx import Document


class FileLoader:

    @staticmethod
    def read_pdf(file_path):
        text = ""

        reader = PdfReader(file_path)

        for page in reader.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

        return text

    @staticmethod
    def read_docx(file_path):

        document = Document(file_path)

        text = ""

        for para in document.paragraphs:
            text += para.text + "\n"

        return text

    @staticmethod
    def read_txt(file_path):

        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()

    @staticmethod
    def load(file_path):

        extension = Path(file_path).suffix.lower()

        if extension == ".pdf":
            return FileLoader.read_pdf(file_path)

        elif extension == ".docx":
            return FileLoader.read_docx(file_path)

        elif extension == ".txt":
            return FileLoader.read_txt(file_path)

        else:
            raise Exception("Unsupported File Format")