from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class BillingPeriod(BaseModel):
    ends_at: str
    starts_at: str


class Paginate(BaseModel):
    next: str | None = None

    model_config = ConfigDict(extra="forbid")
