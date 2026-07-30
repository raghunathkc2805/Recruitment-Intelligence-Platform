import json

from resume_parser.pipeline.resume_pipeline import ResumePipeline
from resume_parser.printers.json_printer import JSONPrinter


def test_json_printer(sample_txt, tmp_path):

    result = ResumePipeline.process(sample_txt)

    output = tmp_path / "resume.json"

    JSONPrinter.save(result, output)

    assert output.exists()

    with open(output, "r", encoding="utf-8") as file:

        data = json.load(file)

    assert data["success"] is True

    assert "candidate" in data


def test_json_printer_dumps(sample_txt):

    result = ResumePipeline.process(sample_txt)

    text = JSONPrinter.dumps(result)

    assert isinstance(text, str)

    assert '"candidate"' in text