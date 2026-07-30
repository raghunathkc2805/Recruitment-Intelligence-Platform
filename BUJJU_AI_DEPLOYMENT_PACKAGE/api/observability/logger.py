from __future__ import annotations

import logging
import sys

from .json_formatter import JsonFormatter
from .log_context import request_id,user_id


class ContextFilter(logging.Filter):

    def filter(self,record):

        record.request_id=request_id.get()

        record.user_id=user_id.get()

        return True


def get_logger(name):

    logger=logging.getLogger(name)

    if logger.handlers:

        return logger

    handler=logging.StreamHandler(sys.stdout)

    handler.setFormatter(JsonFormatter())

    logger.addHandler(handler)

    logger.addFilter(ContextFilter())

    logger.setLevel(logging.INFO)

    return logger
