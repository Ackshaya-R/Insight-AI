import sqlite3
from datetime import datetime

DB_PATH = "database/chat.db"


class ChatHistory:

    def __init__(self):

        self.conn = sqlite3.connect(
            DB_PATH,
            check_same_thread=False
        )

        self.cursor = self.conn.cursor()

        self.create_table()

    # -------------------------------
    # Create Table
    # -------------------------------

    def create_table(self):

        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS chat_history(

                id INTEGER PRIMARY KEY AUTOINCREMENT,

                question TEXT,

                answer TEXT,

                created_at TEXT

            )
            """
        )

        self.conn.commit()

    # -------------------------------
    # Save Chat
    # -------------------------------

    def save_chat(
        self,
        question,
        answer
    ):

        self.cursor.execute(
            """
            INSERT INTO chat_history
            (
                question,
                answer,
                created_at
            )
            VALUES
            (
                ?, ?, ?
            )
            """,
            (
                question,
                answer,
                datetime.now().strftime(
                    "%d-%m-%Y %H:%M:%S"
                )
            )
        )

        self.conn.commit()

    # -------------------------------
    # Get All Chats
    # -------------------------------

    def get_all_chats(self):

        self.cursor.execute(
            """
            SELECT
                id,
                question,
                answer,
                created_at
            FROM chat_history
            ORDER BY id DESC
            """
        )

        return self.cursor.fetchall()

    # -------------------------------
    # Recent Questions (Sidebar)
    # -------------------------------

    def get_recent_questions(
        self,
        limit=20
    ):

        self.cursor.execute(
            """
            SELECT
                id,
                question,
                created_at
            FROM chat_history
            ORDER BY id DESC
            LIMIT ?
            """,
            (limit,)
        )

        return self.cursor.fetchall()

    # -------------------------------
    # Total Chats
    # -------------------------------

    def total_chats(self):

        self.cursor.execute(
            """
            SELECT COUNT(*)
            FROM chat_history
            """
        )

        return self.cursor.fetchone()[0]

    # -------------------------------
    # Clear History
    # -------------------------------

    def clear_history(self):

        self.cursor.execute(
            """
            DELETE FROM chat_history
            """
        )

        self.conn.commit()