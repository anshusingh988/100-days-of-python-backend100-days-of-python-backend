import pdfplumber
import io

def extract_text_from_pdf(file_bytes):
    """
    Extracts text from a PDF file (bytes).
    """
    text = ""
    try:
        with pdfplumber.open(io.BytesIO(file_bytes)) as pdf:
            for page in pdf.pages:
                text += page.extract_text() + "\n"
    except Exception as e:
        print(f"Error parsing PDF: {e}")
        return ""
    return text.strip()

def parse_resume(file_content, filename):
    """
    Parses resume content (PDF or Text) and returns the text.
    """
    if filename.lower().endswith(".pdf"):
        return extract_text_from_pdf(file_content)
    elif filename.lower().endswith(".txt"):
        return file_content.decode("utf-8")
    else:
        return ""
