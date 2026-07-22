"""
Enterprise Session Manager
Sprint 7
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from threading import Lock
from uuid import uuid4


@dataclass
class SessionRecord:
    session_id: str
    user_id: str
    device_id: str
    ip_address: str
    user_agent: str
    created_at: datetime
    expires_at: datetime
    active: bool = True


class SessionManager:

    def __init__(self):

        self._sessions = {}
        self._lock = Lock()

    def create_session(
        self,
        user_id: str,
        device_id: str,
        ip_address: str,
        user_agent: str,
        expires_at: datetime,
    ) -> SessionRecord:

        with self._lock:

            session = SessionRecord(
                session_id=str(uuid4()),
                user_id=user_id,
                device_id=device_id,
                ip_address=ip_address,
                user_agent=user_agent,
                created_at=datetime.utcnow(),
                expires_at=expires_at,
            )

            self._sessions[session.session_id] = session

            return session

    def revoke_session(self, session_id: str):

        with self._lock:

            if session_id in self._sessions:
                self._sessions[session_id].active = False

    def revoke_all(self, user_id: str):

        with self._lock:

            for session in self._sessions.values():

                if session.user_id == user_id:
                    session.active = False

    def validate(self, session_id: str) -> bool:

        session = self._sessions.get(session_id)

        if session is None:
            return False

        if not session.active:
            return False

        if datetime.utcnow() > session.expires_at:
            return False

        return True

    def active_sessions(self, user_id: str):

        return [
            s
            for s in self._sessions.values()
            if s.user_id == user_id and s.active
        ]


session_manager = SessionManager()

