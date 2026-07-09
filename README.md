# InsightAI

## Project

InsightAI: An AI-Powered Document Intelligence System Using Retrieval-Augmented Generation (RAG) and Large Language Models.

## Technologies

- Python
- Streamlit
- FastAPI
- LangChain
- Ollama
- ChromaDB
- Sentence Transformers

## Run

### Create virtual environment

```bash
python -m venv venv
```

### Activate

Windows

```bash
venv\Scripts\activate
```

### Install packages

```bash
pip install -r requirements.txt
```

### Start API

```bash
uvicorn api:app --reload
```

### Start Streamlit

```bash
streamlit run app.py
```