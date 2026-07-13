import fitz

def extract_pdf_text(pdf_file):
    text = ""

    with fitz.open(pdf_file) as pdf:
        for page in pdf:
            text += page.get_text()

    return text