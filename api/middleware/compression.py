from __future__ import annotations

from fastapi.middleware.gzip import GZipMiddleware


def register_compression(app):

    app.add_middleware(

        GZipMiddleware,

        minimum_size=1024,

        compresslevel=6,

    )

    return app
