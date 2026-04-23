from fastapi import APIRouter, UploadFile
import os
import tempfile

from services.pdf_service import extract_text
from storage.memory_storage import store_text

router = APIRouter()

@router.post("/upload")
async def upload_file(file: UploadFile):
    contents = await file.read()

    suffix = os.path.splitext(file.filename)[1]

    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as temp:
        temp.write(contents)
        temp_path = temp.name

    try:
        # ✅ Handle PDF
        if file.content_type == "application/pdf":
            text = extract_text(temp_path)

        # ✅ Handle audio/video (TEMP MOCK)
        elif file.content_type.startswith("audio") or file.content_type.startswith("video"):
            text = "Audio/Video processing not enabled yet"

        else:
            return {"error": "Unsupported file type"}

        store_text(text)

        return {
            "message": "File uploaded",
            "length": len(text)
        }

    finally:
        os.remove(temp_path)