from pipeline.parser_pipeline import build_candidate


class CandidateService:

    @staticmethod
    def process_resume(text, resume_file, parser_version):
        """
        Process resume and return Candidate object.
        """

        return build_candidate(
            text=text,
            resume_file=resume_file,
            parser_version=parser_version
        )