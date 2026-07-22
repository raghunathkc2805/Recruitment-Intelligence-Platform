from __future__ import annotations

import asyncio
from concurrent.futures import ThreadPoolExecutor

_executor = ThreadPoolExecutor(max_workers=16)

async def run_blocking(func,*args,**kwargs):

    loop = asyncio.get_running_loop()

    return await loop.run_in_executor(
        _executor,
        lambda: func(*args,**kwargs),
    )
