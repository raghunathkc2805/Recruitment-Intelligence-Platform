from api.background.bulk_processor import bulk_processor


def process_bulk_matching(
    matching_service,
    jobs,
):

    return bulk_processor.process(
        jobs,
        lambda item:
            matching_service.match_candidate(
                **item
            ),
    )

