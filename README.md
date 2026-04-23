                                                      AI Document & Multimedia Q&A App

Overview
This is a full-stack application that allows users to:

Upload PDF and audio/video files
Ask questions using an AI chatbot
Generate summaries of uploaded content
View timestamps for audio content and play specific segments


🛠️ Tech Stack

Frontend

React.js

Backend

FastAPI (Python)
Groq (LLM API)

Other

Docker (containerization)
GitHub 

⚙️ Features

✔ Upload PDF / Audio / Video
✔ AI-powered Q&A based on uploaded content
✔ Document summarization
✔ Audio timestamps with play button
✔ Chat UI
✔ Dockerized backend


How it works
Files are uploaded via frontend
Backend extracts/stores text
User asks a question
Relevant chunks are selected
LLM generates answer
Summary API provides document overview


Run Locally
# Backend
uvicorn main:app --reload

# Frontend
npm start

docker build -t ai-doc-chat .
docker run -p 8000:8000 ai-doc-chat


📁 Project Structure
routes/
services/
storage/
frontend/
main.py
Dockerfile
