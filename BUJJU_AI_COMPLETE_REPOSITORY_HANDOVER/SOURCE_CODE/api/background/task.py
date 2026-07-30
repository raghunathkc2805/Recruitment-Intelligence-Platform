from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from uuid import uuid4


@dataclass(slots=True)
class BackgroundTask:

    name: str

    function: callable

    args: tuple = ()

    kwargs: dict = field(default_factory=dict)

    id: str = field(default_factory=lambda: str(uuid4()))

    created_at: datetime = field(default_factory=datetime.utcnow)

    started_at: datetime | None = None

    completed_at: datetime | None = None

    status: str = "PENDING"

    result = None

    error: str | None = None
