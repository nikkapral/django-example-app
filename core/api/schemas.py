from pydantic import BaseModel, Field
from typing import Generic, Any, TypeVar

from core.api.filters import PaginationOut

TData = TypeVar('TData')
TListItem = TypeVar('TListItem')

class PingResponseSchema(BaseModel):
    result: bool

class ListPaginationResponse(BaseModel, Generic[TListItem]):
    items: list[TListItem]
    pagination: PaginationOut

class APIResponse(BaseModel, Generic[TData]):
    data: TData | dict = Field(default_factory=dict)
    meta: dict[str, Any] = Field(default_factory=dict)
    errors: list[Any] = Field(default_factory=list)
