from fastapi import APIRouter

from .utils import get_class_handlers, get_handler_metadata


__all__ = [
    'CbRouter',
]


class CbRouter:
    _router: APIRouter

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)

        cls._prepare_new_instance(instance)

        return instance

    @staticmethod
    def _prepare_new_instance(instance) -> APIRouter:
        router = APIRouter()

        setattr(instance, '_router', router)

        instance._prepare_handlers()

        return router

    def _prepare_handlers(self) -> None:
        handlers = get_class_handlers(self)

        for handler in handlers:
            metadata = get_handler_metadata(handler)

            self._router.add_api_route(
                path=metadata.path,
                endpoint=handler,
                response_model=metadata.response_model,
                status_code=metadata.status_code,
                tags=metadata.tags,
            )
