from dataclasses import dataclass
from enum import Enum
from typing import Any, Optional, Union, List, Sequence, Dict, Type
from fastapi import params
from starlette.responses import Response


__all__ = [
    'HandlerMetadata'
]


@dataclass
class HandlerMetadata:
    methods: list[str]

    path: str
    response_model: Any
    status_code: Optional[int]
    tags: Optional[List[Union[str, Enum]]]

    # TODO: Сделать позже.
    # dependencies: Optional[Sequence[params.Depends]]
    # summary: Optional[str]
    # description: Optional[str]
    # response_description: str
    # responses: Optional[Dict[Union[int, str], Dict[str, Any]]]
    # deprecated: Optional[bool]
    # include_in_schema: bool
    # response_class: Type[Response]
