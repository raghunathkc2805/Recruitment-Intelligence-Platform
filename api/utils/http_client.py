from __future__ import annotations

import httpx


class AsyncHttpClient:

    def __init__(self):

        self.client = httpx.AsyncClient(
            timeout=60,
            follow_redirects=True,
        )

    async def get(self,url,**kwargs):

        return await self.client.get(
            url,
            **kwargs,
        )

    async def post(self,url,**kwargs):

        return await self.client.post(
            url,
            **kwargs,
        )

    async def close(self):

        await self.client.aclose()


http_client = AsyncHttpClient()
