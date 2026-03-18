from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from typing import Optional
import os


# AutoU 

from classifier import classify_email
from utils import extract_text_from_file

app = FastAPI(title="Email Classifier API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="../frontend"), name="static")

@app.get("/")
def serve_frontend():
    return FileResponse("../frontend/index.html")

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/classify")
async def classify(
    email_text: Optional[str] = Form(None),
    file: Optional[UploadFile] = File(None)
):
    if not email_text and not file:
        raise HTTPException(
            status_code=400,
            detail="Envie um texto ou um arquivo."
        )

    if file:
        contents = await file.read()
        try:
            email_text = extract_text_from_file(contents, file.filename)
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))

    if not email_text.strip():
        raise HTTPException(
            status_code=400,
            detail="O conteúdo do email está vazio."
        )

    try:
        result = classify_email(email_text)
        return result
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Erro ao classificar email: {str(e)}"
        )