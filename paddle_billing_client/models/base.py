from typing import Optional

from pydantic import BaseModel


class LazyBaseModel(BaseModel):
    class Config:
        extra = "allow"


class Pagination(LazyBaseModel):
    per_page: int
    estimated_total: int
    next: Optional[str]
    has_more: bool


class Meta(LazyBaseModel):
    pagination: Optional[Pagination]
    request_id: str


class PaddleResponse(LazyBaseModel):
    meta: Meta
