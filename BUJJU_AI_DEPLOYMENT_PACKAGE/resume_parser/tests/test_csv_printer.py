import csv

from resume_parser.pipeline.resume_pipeline import ResumePipeline
from resume_parser.printers.csv_printer import CSVPrinter


def test_csv_printer(sample_txt, tmp_path):

    result = ResumePipeline.process(sample_txt)

    output = tmp_path / "resume.csv"

    CSVPrinter.save(result, output)

    assert output.exists()

    with open(
        output,
        newline="",
        encoding="utf-8",
    ) as file:

        rows = list(csv.DictReader(file))

    assert len(rows) == 1

    assert "name" in rows[0]

    assert "email" in rows[0]


def test_csv_printer_headers():

    assert "name" in CSVPrinter.HEADERS

    assert "email" in CSVPrinter.HEADERS

    assert "technical_skills" in CSVPrinter.HEADERS