from __future__ import annotations

from enum import Enum
from typing import Optional

from fastapi import FastAPI

from .utils import get_class_handlers, get_handler_metadata
from .router import CbRouter


__all__ = [
    'CbApp',
]


class CbApp:
    _app: FastAPI

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)

        cls._prepare_new_instance(instance)

        return instance

    def mount(self, path: str, app: CbApp, name: Optional[str] = None) -> None:
        self._app.mount(path, app._app, name)

    def mount_router(self, path: str,  router: CbRouter, tags: Optional[list[str | Enum]] = None) -> None:
        self._app.include_router(router._router, prefix=path, tags=tags)

    @staticmethod
    def _prepare_new_instance(instance) -> FastAPI:
        app = FastAPI()

        setattr(instance, '_app', app)

        instance._prepare_handlers()

        return app

    def _prepare_handlers(self) -> None:
        handlers = get_class_handlers(self)

        for handler in handlers:
            metadata = get_handler_metadata(handler)

            self._app.add_api_route(
                path=metadata.path,
                endpoint=handler,
                response_model=metadata.response_model,
                status_code=metadata.status_code,
                tags=metadata.tags,
            )

    @property
    def app(self) -> FastAPI:
        return self._app
