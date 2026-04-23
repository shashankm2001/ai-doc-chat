from fastapi import APIRouter, File, UploadFile

router = APIRouter()

@router.post("/upload-audio")
def upload_audio(file: UploadFile = File(...)):

    # Temporary fallback (no whisper)
    return {
        "text": "Audio transcription not enabled yet",
        "timestamps": [
            {"text": "Sample segment", "start": 5},
            {"text": "Another segment", "start": 10}
        ]
    }