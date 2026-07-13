"""
Search Engine Exceptions
"""


class SearchEngineError(Exception):
    """
    Base Search Engine exception.
    """


class InvalidQueryError(SearchEngineError):
    """
    Invalid query.
    """


class SearchExecutionError(SearchEngineError):
    """
    Search execution failed.
    """