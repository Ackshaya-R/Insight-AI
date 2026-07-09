import os
from dotenv import load_dotenv

load_dotenv()


class Config:

    APP_NAME = os.getenv("APP_NAME")

    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

    MODEL_NAME = os.getenv("MODEL_NAME")

    EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL")

    CHROMA_DB = os.getenv("CHROMA_DB")

    UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER")

    DATABASE = os.getenv("DATABASE")


config = Config()