from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class BillingPeriod(BaseModel):
    ends_at: str
    starts_at: str


class Paginate(BaseModel):
    next: str | None = None

    model_config = ConfigDict(extra="forbid")


class ImportMeta(BaseModel):
    external_id: str | None = None
    imported_from: str
