from __future__ import annotations

import time
from functools import wraps

from .performance_monitor import performance_monitor


def benchmark(endpoint):

    def decorator(func):

        @wraps(func)

        async def wrapper(*args,**kwargs):

            start=time.perf_counter()

            result=await func(*args,**kwargs)

            performance_monitor.record(
                endpoint,
                time.perf_counter()-start,
            )

            return result

        return wrapper

    return decorator
