import os
from config import config


def save_uploaded_file(uploaded_file):
    """
    Save the uploaded file into the uploads folder.
    """

    os.makedirs(config.UPLOAD_FOLDER, exist_ok=True)

    file_path = os.path.join(
        config.UPLOAD_FOLDER,
        uploaded_file.name
    )

    with open(file_path, "wb") as file:
        file.write(uploaded_file.getbuffer())

    return file_path