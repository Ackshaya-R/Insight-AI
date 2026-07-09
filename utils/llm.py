import google.generativeai as genai
from config import config


class GeminiLLM:

    def __init__(self):

        genai.configure(
            api_key=config.GEMINI_API_KEY
        )

        self.model = genai.GenerativeModel(
            model_name=config.MODEL_NAME
        )

    def generate_answer(self, context, question):

        prompt = f"""
You are InsightAI.

Answer ONLY from the given context.

If the answer is not available in the context, reply:

"I couldn't find the answer in the uploaded documents."

-----------------------

Context

{context}

-----------------------

Question

{question}

-----------------------

Answer
"""

        response = self.model.generate_content(prompt)

        return response.text