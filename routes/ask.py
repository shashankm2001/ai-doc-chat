from fastapi import APIRouter
from pydantic import BaseModel
from storage.memory_storage import get_chunks
from openai import OpenAI
import os
os.environ["PATH"] += os.pathsep + r"C:\Users\Shashank M\Downloads\ffmpeg-master-latest-win64-gpl-shared\ffmpeg-master-latest-win64-gpl-shared\bin"

router = APIRouter()

# ✅ FIX 1: add client
client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

# ✅ FIX 2: add model
class Question(BaseModel):
    question: str


@router.post("/ask")
def ask_question(q: Question):
    chunks = get_chunks()

    if not chunks:
        return {"answer": "No PDF uploaded yet"}

    if not q.question.strip():
        return {"answer": "Please ask a valid question"}

    relevant_chunks = []

    for chunk in chunks:
        if any(word in chunk.lower() for word in q.question.lower().split()):
            relevant_chunks.append(chunk)

    if not relevant_chunks:
        relevant_chunks = chunks[:2]

    context = " ".join(relevant_chunks[:2])

    prompt = f"""
Answer the question based ONLY on the context below.

Context:
{context}

Question:
{q.question}
"""

    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}]
        )

        return {
            "answer": response.choices[0].message.content
        }

    except Exception as e:
        return {"answer": f"Error: {str(e)}"}