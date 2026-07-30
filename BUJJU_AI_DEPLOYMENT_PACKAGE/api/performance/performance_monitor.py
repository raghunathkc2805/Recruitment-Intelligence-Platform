from __future__ import annotations

import time
from collections import defaultdict
from threading import Lock


class PerformanceMonitor:

    def __init__(self):

        self._lock = Lock()

        self.metrics = defaultdict(list)

    def record(
        self,
        endpoint: str,
        duration: float,
    ):

        with self._lock:

            self.metrics[endpoint].append(duration)

    def report(self):

        report = {}

        for endpoint, values in self.metrics.items():

            report[endpoint] = {

                "requests": len(values),

                "average_ms": round(sum(values)/len(values)*1000,2),

                "max_ms": round(max(values)*1000,2),

                "min_ms": round(min(values)*1000,2),

            }

        return report


performance_monitor = PerformanceMonitor()
