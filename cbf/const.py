from enum import StrEnum


__all__ = [
    'HANDLER_META_DATA_ATTR',
    'HttpMethod',
]


HANDLER_META_DATA_ATTR = '__cb_metadata__'


class HttpMethod(StrEnum):
    GET = 'GET'
    POST = 'POST'
    DELETE = 'DELETE'
    PATCH = 'PATCH'
