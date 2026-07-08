import docx2txt


def extract_docx_text(docx_file):
    """
    Extract text from a DOCX file using docx2txt.
    This preserves the resume header much better than python-docx.
    """

    return docx2txt.process(str(docx_file))