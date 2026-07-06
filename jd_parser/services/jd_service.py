from jd_parser.pipeline.jd_pipeline import build_job_description


class JDService:
    """
    Job Description Service
    """

    def parse(self, text, jd_file, parser_version):
        return build_job_description(
            text=text,
            jd_file=jd_file,
            parser_version=parser_version
        )