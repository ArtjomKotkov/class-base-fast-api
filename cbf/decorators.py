from enum import Enum
from typing import Any, Optional, Callable

from fastapi.datastructures import Default

from .const import HANDLER_META_DATA_ATTR, HttpMethod
from .metadata import HandlerMetadata


__all__ = [
    'Cb',
]


class Cb:

    @staticmethod
    def _make_handler_metadata(
        method: HttpMethod,
        path: str,
        response_model: Any = Default(None),
        status_code: Optional[int] = None,
        tags: Optional[list[str | Enum]] = None,
    ):
        return HandlerMetadata(
            [method],
            path,
            response_model,
            status_code,
            tags,
        )

    @staticmethod
    def get(
        path: str,
        *,
        response_model: Any = Default(None),
        status_code: Optional[int] = None,
        tags: Optional[list[str | Enum]] = None,
    ):
        def wrapper(handler: Callable):
            setattr(
                handler,
                HANDLER_META_DATA_ATTR,
                Cb._make_handler_metadata(
                    HttpMethod.GET,
                    path,
                    response_model,
                    status_code,
                    tags
                )
            )

            return handler

        return wrapper

    @staticmethod
    def post(
        path: str,
        *,
        response_model: Any = Default(None),
        status_code: Optional[int] = None,
        tags: Optional[list[str | Enum]] = None,
    ):
        def wrapper(handler: Callable):
            setattr(
                handler,
                HANDLER_META_DATA_ATTR,
                Cb._make_handler_metadata(
                    HttpMethod.POST,
                    path,
                    response_model,
                    status_code,
                    tags
                )
            )

            return handler

        return wrapper

    @staticmethod
    def patch(
        path: str,
        *,
        response_model: Any = Default(None),
        status_code: Optional[int] = None,
        tags: Optional[list[str | Enum]] = None,
    ):
        def wrapper(handler: Callable):
            setattr(
                handler,
                HANDLER_META_DATA_ATTR,
                Cb._make_handler_metadata(
                    HttpMethod.PATCH,
                    path,
                    response_model,
                    status_code,
                    tags
                )
            )

            return handler

        return wrapper

    @staticmethod
    def delete(
        path: str,
        *,
        response_model: Any = Default(None),
        status_code: Optional[int] = None,
        tags: Optional[list[str | Enum]] = None,
    ):
        def wrapper(handler: Callable):
            setattr(
                handler,
                HANDLER_META_DATA_ATTR,
                Cb._make_handler_metadata(
                    HttpMethod.DELETE,
                    path,
                    response_model,
                    status_code,
                    tags
                )
            )

            return handler

        return wrapper
