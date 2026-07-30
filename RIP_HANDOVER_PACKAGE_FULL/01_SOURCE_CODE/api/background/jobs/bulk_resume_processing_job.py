from api.background.bulk_processor import bulk_processor


def process_bulk_resumes(
    resume_service,
    jobs,
):

    return bulk_processor.process(
        jobs,
        lambda item:
            resume_service.parse_resume(
                **item
            ),
    )

