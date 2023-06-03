import inspect
from typing import Callable, Any

from .const import HANDLER_META_DATA_ATTR
from .metadata import HandlerMetadata


__all__ = [
    'is_handler',
    'get_class_handlers',
    'get_handler_metadata',
]


def get_handler_metadata(handler: Callable) -> HandlerMetadata:
    assert hasattr(handler, HANDLER_META_DATA_ATTR)

    return getattr(handler, HANDLER_META_DATA_ATTR)


def is_handler(handler: Callable) -> bool:
    return hasattr(handler, HANDLER_META_DATA_ATTR)


def get_class_handlers(instance: Any) -> list[Callable]:
    return [
        method
        for key, method
        in inspect.getmembers(instance, predicate=inspect.ismethod)
        if is_handler(method)
    ]
