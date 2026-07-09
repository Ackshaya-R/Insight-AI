from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from config import config

app = FastAPI(
    title=config.APP_NAME,
    description="AI-Powered Document Intelligence System",
    version="1.0.0"
)

# -----------------------------
# Enable CORS
# -----------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------
# Models
# -----------------------------
class QuestionRequest(BaseModel):
    question: str


class QuestionResponse(BaseModel):
    answer: str


# -----------------------------
# Home API
# -----------------------------
@app.get("/")
def home():
    return {
        "project": config.APP_NAME,
        "status": "Running",
        "version": "1.0"
    }


# -----------------------------
# Health Check
# -----------------------------
@app.get("/health")
def health():
    return {
        "status": "Healthy"
    }


# -----------------------------
# Ask AI
# -----------------------------
@app.post("/ask", response_model=QuestionResponse)
def ask_ai(request: QuestionRequest):

    # RAG pipeline will be connected later

    return QuestionResponse(
        answer=f"You asked: {request.question}"
    )