"""
Sprint 7
Enterprise Secret Rotation
"""

from __future__ import annotations

import secrets
from dataclasses import dataclass
from datetime import datetime, timedelta
from threading import Lock


@dataclass
class SecretVersion:
    version: int
    key: str
    created_at: datetime
    expires_at: datetime
    active: bool = True


class SecretManager:

    ROTATION_DAYS = 90

    def __init__(self):

        self._lock = Lock()
        self._version = 1
        self._keys = {}

        self.rotate(initial=True)

    def current(self) -> SecretVersion:
        return self._keys[self._version]

    def get(self, version: int):
        return self._keys.get(version)

    def rotate(self, initial=False):

        with self._lock:

            if not initial:
                self._version += 1

            secret = SecretVersion(
                version=self._version,
                key=secrets.token_urlsafe(64),
                created_at=datetime.utcnow(),
                expires_at=datetime.utcnow() + timedelta(days=self.ROTATION_DAYS),
            )

            self._keys[self._version] = secret

            return secret

    def cleanup(self):

        now = datetime.utcnow()

        expired = []

        for version, key in self._keys.items():

            if version == self._version:
                continue

            if key.expires_at < now:
                expired.append(version)

        for version in expired:
            del self._keys[version]


secret_manager = SecretManager()
