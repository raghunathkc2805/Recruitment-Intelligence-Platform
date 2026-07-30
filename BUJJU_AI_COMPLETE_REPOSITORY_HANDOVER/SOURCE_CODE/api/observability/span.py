import time
import uuid

class Span:

    def __init__(self,name):

        self.name=name
        self.span_id=str(uuid.uuid4())
        self.start=time.perf_counter()

    def finish(self):

        self.duration_ms=round(
            (time.perf_counter()-self.start)*1000,
            2
        )

        return self
