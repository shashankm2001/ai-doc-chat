from fastapi import FastAPI
from routes import upload, ask, summary
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(upload.router)
app.include_router(ask.router)
app.include_router(summary.router)

@app.get("/")
def home():
    return {"message": "Server Running"}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)