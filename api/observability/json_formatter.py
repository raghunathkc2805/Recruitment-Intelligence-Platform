from __future__ import annotations

import json
import logging
from datetime import datetime


class JsonFormatter(logging.Formatter):

    def format(self, record):

        payload = {

            "timestamp": datetime.utcnow().isoformat(),

            "level": record.levelname,

            "logger": record.name,

            "message": record.getMessage(),

        }

        if hasattr(record,"request_id"):
            payload["request_id"]=record.request_id

        if hasattr(record,"user_id"):
            payload["user_id"]=record.user_id

        if hasattr(record,"duration_ms"):
            payload["duration_ms"]=record.duration_ms

        if record.exc_info:

            payload["exception"]=self.formatException(
                record.exc_info
            )

        return json.dumps(payload)
