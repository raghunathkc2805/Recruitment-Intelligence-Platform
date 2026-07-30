from resume_parser.pipeline.resume_pipeline import ResumePipeline
from resume_parser.printers.console_printer import ConsolePrinter


def test_console_printer(sample_txt, capsys):

    result = ResumePipeline.process(sample_txt)

    ConsolePrinter.print(result)

    captured = capsys.readouterr()

    assert "Resume Information" in captured.out

    assert "Name" in captured.out

    assert "Email" in captured.out