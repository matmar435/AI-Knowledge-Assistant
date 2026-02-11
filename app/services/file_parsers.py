from pypdf import PdfReader
from docx import Document


def read_txt(path: str) -> str:
    with open(path, "r", encoding="utf8") as f:
        return f.read()


def read_pdf(path: str) -> str:
    reader = PdfReader(path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text


def read_docx(path: str) -> str:
    doc = Document(path)
    return "\n".join([p.text for p in doc.paragraphs])
