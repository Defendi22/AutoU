import PyPDF2
import io

def extract_text_from_file(file_bytes: bytes, filename: str) -> str:
    if filename.endswith(".pdf"):
        return extract_text_from_pdf(file_bytes)
    elif filename.endswith(".txt"):
        return file_bytes.decode("utf-8")
    else:
        raise ValueError("Formato não suportado. Use .txt ou .pdf")

def extract_text_from_pdf(file_bytes: bytes) -> str:
    reader = PyPDF2.PdfReader(io.BytesIO(file_bytes))
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text.strip()