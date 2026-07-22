from __future__ import annotations

from threading import Lock


class CompressionMetrics:

    def __init__(self):

        self._lock = Lock()

        self.requests = 0

        self.compressed = 0

        self.original_bytes = 0

        self.compressed_bytes = 0

    def record(
        self,
        original_size: int,
        compressed_size: int,
    ):

        with self._lock:

            self.requests += 1

            self.compressed += 1

            self.original_bytes += original_size

            self.compressed_bytes += compressed_size

    def report(self):

        saved = self.original_bytes - self.compressed_bytes

        ratio = 0

        if self.original_bytes:

            ratio = round(
                (saved / self.original_bytes) * 100,
                2,
            )

        return {

            "requests": self.requests,

            "compressed": self.compressed,

            "bytes_saved": saved,

            "compression_ratio": ratio,

        }


compression_metrics = CompressionMetrics()
