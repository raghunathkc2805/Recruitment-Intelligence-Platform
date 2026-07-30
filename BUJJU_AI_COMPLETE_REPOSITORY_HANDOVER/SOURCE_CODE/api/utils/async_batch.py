from __future__ import annotations

import asyncio


async def gather_limit(limit,tasks):

    semaphore = asyncio.Semaphore(limit)

    async def wrapper(task):

        async with semaphore:

            return await task

    return await asyncio.gather(
        *[wrapper(t) for t in tasks]
    )
