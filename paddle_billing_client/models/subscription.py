from __future__ import annotations

from typing import List, Literal, Optional

from datetime import datetime

from pydantic import validator

from paddle_billing_client.models.base import LazyBaseModel as BaseModel
from paddle_billing_client.models.base import PaddleResponse
from paddle_billing_client.models.price import BillingCycle, Price


class Item(BaseModel):
    price: Price
    status: str
    quantity: int
    recurring: bool
    created_at: datetime
    updated_at: datetime
    next_billed_at: str | None
    previously_billed_at: str | None


class BillingPeriod(BaseModel):
    ends_at: str
    starts_at: str


class SubscriptionBase(BaseModel):
    status: str
    customer_id: str
    address_id: str
    business_id: str | None
    currency_code: str
    created_at: datetime
    updated_at: datetime
    started_at: datetime
    first_billed_at: datetime
    next_billed_at: datetime | None
    paused_at: datetime | None
    canceled_at: datetime | None
    collection_mode: str
    billing_details: dict | None
    current_billing_period: BillingPeriod
    billing_cycle: BillingCycle
    recurring_transaction_details: dict | None
    next_transaction: dict | None
    scheduled_change: dict | None
    items: list[Item]
    custom_data: dict | None
    management_urls: dict | None


class Subscription(SubscriptionBase):
    id: str


class SubscriptionQueryParams(BaseModel):
    # Return entities after the specified cursor. Used for working through paginated results.
    after: str | None = None
    # Return entities related to the specified customer.
    # Use a comma separated list to specify multiple customer IDs.
    customer_id: str | None = None
    # Order returned entities by the specified field and direction ([ASC] or [DESC]).
    order_by: Literal["[ASC]", "[DESC]"] | None = None
    # Set how many entities are returned per page. Default: 50
    per_page: int | None = None
    # Return entities related to the specified price. Use a comma separated list to specify multiple price IDs.
    price_id: str | None = None
    # Return entities that match the specified status. Use a comma separated list to specify multiple status values.
    status: str | None = None

    @validator("status", allow_reuse=True)
    def check_status(cls, v: str) -> str:  # pragma: no cover
        valid_statuses = ["active", "canceled", "past_due", "paused", "trialing"]
        if not all([s in valid_statuses for s in v.split(",")]):
            raise ValueError(
                f"Query param invalid status: {v}, allowed values: {valid_statuses}"
            )
        return v


class SubscriptionResponse(PaddleResponse):
    data: Subscription


class SubscriptionsResponse(PaddleResponse):
    data: list[Subscription]


class SubscriptionRequest(SubscriptionBase):
    effective_from: datetime | Literal["next_billing_period", "immediately"] | None
    resume_at: datetime | None
