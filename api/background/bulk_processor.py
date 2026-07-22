from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Callable, Iterable


class BulkProcessor:

    def __init__(self, workers: int = 8):
        self.executor = ThreadPoolExecutor(max_workers=workers)

    def process(
        self,
        items: Iterable,
        worker: Callable,
    ):

        futures = {
            self.executor.submit(worker, item): item
            for item in items
        }

        completed = []
        failed = []

        for future in as_completed(futures):

            item = futures[future]

            try:
                completed.append(
                    future.result()
                )

            except Exception as ex:

                failed.append({

                    "item": item,

                    "error": str(ex)

                })

        return {

            "processed": len(completed),

            "failed": len(failed),

            "results": completed,

            "errors": failed,

        }


bulk_processor = BulkProcessor()

