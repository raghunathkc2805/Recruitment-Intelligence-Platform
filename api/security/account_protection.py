"""
Sprint 7
Enterprise Account Protection
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from datetime import datetime, timedelta
from threading import Lock


@dataclass
class PasswordHistory:

    password_hash: str
    changed_at: datetime


@dataclass
class FailedLogin:

    failures: int = 0
    locked_until: datetime | None = None


class AccountProtectionManager:

    MAX_FAILED_ATTEMPTS = 5

    LOCKOUT_MINUTES = 30

    PASSWORD_HISTORY_LIMIT = 5

    PASSWORD_EXPIRY_DAYS = 90

    def __init__(self):

        self.failed = defaultdict(FailedLogin)

        self.password_history = defaultdict(list)

        self.lock = Lock()

    # ------------------------------------------------------------

    def is_locked(self, username: str):

        item = self.failed[username]

        if item.locked_until is None:
            return False

        return datetime.utcnow() < item.locked_until

    # ------------------------------------------------------------

    def record_failed_login(self, username: str):

        with self.lock:

            item = self.failed[username]

            item.failures += 1

            if item.failures >= self.MAX_FAILED_ATTEMPTS:

                item.locked_until = (
                    datetime.utcnow()
                    + timedelta(minutes=self.LOCKOUT_MINUTES)
                )

    # ------------------------------------------------------------

    def reset_failed_login(self, username: str):

        with self.lock:

            self.failed[username] = FailedLogin()

    # ------------------------------------------------------------

    def save_password_hash(
        self,
        username: str,
        password_hash: str,
    ):

        history = self.password_history[username]

        history.insert(
            0,
            PasswordHistory(
                password_hash=password_hash,
                changed_at=datetime.utcnow(),
            ),
        )

        del history[self.PASSWORD_HISTORY_LIMIT:]

    # ------------------------------------------------------------

    def password_reused(
        self,
        username: str,
        password_hash: str,
    ) -> bool:

        history = self.password_history[username]

        return any(
            item.password_hash == password_hash
            for item in history
        )

    # ------------------------------------------------------------

    def password_expired(
        self,
        username: str,
    ) -> bool:

        history = self.password_history[username]

        if not history:
            return False

        latest = history[0]

        return (
            datetime.utcnow()
            - latest.changed_at
        ) > timedelta(days=self.PASSWORD_EXPIRY_DAYS)


account_protection = AccountProtectionManager()
