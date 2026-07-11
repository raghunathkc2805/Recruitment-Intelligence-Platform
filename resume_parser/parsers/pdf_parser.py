    @classmethod
    def parse(cls, file_path: str | Path):

        path = Path(file_path)

        try:

            raw_text, pages = cls._read_pdfplumber(path)

            engine = "pdfplumber"

        except Exception:

            raw_text, pages = cls._read_pypdf2(path)

            engine = "PyPDF2"

        cleaned = text_cleaner.clean(raw_text)

        if not cleaned.strip():
            raise ValueError(
                "No readable text found in PDF."
            )

        return {

            KEY_SUCCESS: True,

            KEY_STATUS: STATUS_SUCCESS,

            KEY_FILE_NAME: path.name,

            KEY_FILE_TYPE: ".pdf",

            KEY_FILE_SIZE: path.stat().st_size,

            KEY_PAGE_COUNT: pages,

            KEY_TEXT: cleaned,

            KEY_METADATA: {

                "encoding": DEFAULT_ENCODING,

                "engine": engine

            },

            KEY_ERRORS: []

        }