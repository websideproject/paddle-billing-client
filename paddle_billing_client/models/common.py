from __future__ import annotations

from pydantic import BaseModel, Extra


class BillingPeriod(BaseModel):
    ends_at: str
    starts_at: str


class Paginate(BaseModel):
    next: str | None

    class Config:
        extra = Extra.forbid
