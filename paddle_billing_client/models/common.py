from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, ConfigDict


class PaymentTerms(BaseModel):
    interval: Literal["day", "week", "month", "year"]
    frequency: int


class BillingPeriod(BaseModel):
    ends_at: str
    starts_at: str


class BillingDetails(BaseModel):
    enable_checkout: bool
    purchase_order_number: str | None = None
    additional_information: str | None = None
    payment_terms: PaymentTerms


class Paginate(BaseModel):
    next: str | None = None

    model_config = ConfigDict(extra="forbid")


class ImportMeta(BaseModel):
    external_id: str | None = None
    imported_from: str
