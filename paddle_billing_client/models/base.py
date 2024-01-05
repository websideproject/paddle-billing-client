from typing import Optional

from pydantic import BaseModel, ConfigDict


class LazyBaseModel(BaseModel):
    model_config = ConfigDict(extra="allow")


class Pagination(LazyBaseModel):
    per_page: int
    estimated_total: int
    next: Optional[str] = None
    has_more: bool


class Meta(LazyBaseModel):
    pagination: Optional[Pagination] = None
    request_id: str


class PaddleResponse(LazyBaseModel):
    meta: Meta
