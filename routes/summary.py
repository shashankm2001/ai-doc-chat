from fastapi import APIRouter
from storage.memory_storage import get_chunks
from openai import OpenAI
import os

router = APIRouter()

client = OpenAI(
    api_key = os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

@router.get("/summary")

def get_summary():
    context = get_chunks()

    if not context:
        return {"error": "No PDF uploaded yet"}
    
    prompt = f"""
Summarize the following document in a concise manner.

Document:
{context[:3000]}
"""
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )
    return {
        "summary" : response.choices[0].message.content
    }
    
