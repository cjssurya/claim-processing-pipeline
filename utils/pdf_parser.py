import fitz
import pytesseract
from PIL import Image
import io

# CONNECT TESSERACT
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_pages(pdf_bytes):
    doc = fitz.open(stream=pdf_bytes, filetype="pdf")
    
    pages = []
    
    for i, page in enumerate(doc):
        text = page.get_text()

        if not text.strip():
            pix = page.get_pixmap()
            img = Image.open(io.BytesIO(pix.tobytes()))
            text = pytesseract.image_to_string(img)

        pages.append({
            "page_number": i + 1,
            "text": text
        })
    
    return pages