from collections import Counter
import time


class QueryMetrics:

    def __init__(self):

        self.stats = Counter()

    def start(self):

        return time.perf_counter()

    def stop(self,start):

        elapsed = round(
            time.perf_counter()-start,
            4,
        )

        self.stats["queries"] += 1

        return elapsed

    def report(self):

        return dict(self.stats)


query_metrics = QueryMetrics()
