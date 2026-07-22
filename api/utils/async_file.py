from __future__ import annotations

import aiofiles

async def read_text(path):

    async with aiofiles.open(
        path,
        "r",
        encoding="utf8",
    ) as f:

        return await f.read()


async def write_text(path,data):

    async with aiofiles.open(
        path,
        "w",
        encoding="utf8",
    ) as f:

        await f.write(data)
