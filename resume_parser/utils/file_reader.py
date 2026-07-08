from __future__ import annotations
>>>
>>> from pathlib import Path
>>> from typing import Union
>>>
>>>
>>> PathLike = Union[str, Path]
>>>
>>>
>>> class FileReader:
...         """
...             Common file reader used by all Resume Parser components.
...
...     Supports:
...                     • TXT
...                             • PDF
...                                     • DOCX
...
...     Raises:
...                     FileNotFoundError
...                             ValueError
...                                 """
...
>>>     @staticmethod
  File "<python-input-10>", line 1
    @staticmethod
IndentationError: unexpected indent
>>>     def read(file_path: PathLike) -> str:
  File "<python-input-11>", line 1
    def read(file_path: PathLike) -> str:
IndentationError: unexpected indent
>>>         path = Path(file_path)
  File "<python-input-12>", line 1
    path = Path(file_path)
IndentationError: unexpected indent
>>>
>>>         if not path.exists():
  File "<python-input-14>", line 1
    if not path.exists():
IndentationError: unexpected indent
>>>             raise FileNotFoundError(f"{path} does not exist.")
  File "<python-input-15>", line 1
    raise FileNotFoundError(f"{path} does not exist.")
IndentationError: unexpected indent
>>>
>>>         suffix = path.suffix.lower()
  File "<python-input-17>", line 1
    suffix = path.suffix.lower()
IndentationError: unexpected indent
>>>
>>>         if suffix == ".txt":
  File "<python-input-19>", line 1
    if suffix == ".txt":
IndentationError: unexpected indent
>>>             return FileReader._read_txt(path)
  File "<python-input-20>", line 1
    return FileReader._read_txt(path)
IndentationError: unexpected indent
>>>
>>>         if suffix == ".pdf":
  File "<python-input-22>", line 1
    if suffix == ".pdf":
IndentationError: unexpected indent
>>>             from resume_parser.parsers.pdf_parser import PDFParser
  File "<python-input-23>", line 1
    from resume_parser.parsers.pdf_parser import PDFParser
IndentationError: unexpected indent
>>>
>>>             return PDFParser().parse(path)
  File "<python-input-25>", line 1
    return PDFParser().parse(path)
IndentationError: unexpected indent
>>>
>>>         if suffix == ".docx":
  File "<python-input-27>", line 1
    if suffix == ".docx":
IndentationError: unexpected indent
>>>             from resume_parser.parsers.docx_parser import DOCXParser
  File "<python-input-28>", line 1
    from resume_parser.parsers.docx_parser import DOCXParser
IndentationError: unexpected indent
>>>
>>>             return DOCXParser().parse(path)
  File "<python-input-30>", line 1
    return DOCXParser().parse(path)
IndentationError: unexpected indent
>>>
>>>         raise ValueError(f"Unsupported file type: {suffix}")
  File "<python-input-32>", line 1
    raise ValueError(f"Unsupported file type: {suffix}")
IndentationError: unexpected indent
>>>
>>>     @staticmethod
  File "<python-input-34>", line 1
    @staticmethod
IndentationError: unexpected indent
>>>     def _read_txt(path: Path) -> str:
  File "<python-input-35>", line 1
    def _read_txt(path: Path) -> str:
IndentationError: unexpected indent
>>>         return path.read_text(
  File "<python-input-36>", line 1
    return path.read_text(
IndentationError: unexpected indent
>>>             encoding="utf-8",
  File "<python-input-37>", line 1
    encoding="utf-8",
IndentationError: unexpected indent
>>>             errors="ignore",