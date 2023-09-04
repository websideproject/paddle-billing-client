from __future__ import annotations

from typing import List, Literal, Optional

from datetime import datetime

from pydantic import validator

from paddle_billing_client.models.base import LazyBaseModel as BaseModel
from paddle_billing_client.models.base import PaddleResponse
from paddle_billing_client.models.common import BillingPeriod
from paddle_billing_client.models.price import BillingCycle, Price
from paddle_billing_client.models.transaction import Transaction


class Item(BaseModel):
    price: Price | None
    price_id: str | None
    status: str | None
    quantity: int | None
    recurring: bool | None
    created_at: datetime | None
    updated_at: datetime | None
    next_billed_at: datetime | None
    previously_billed_at: datetime | None


class ScheduledChange(BaseModel):
    action: Literal["cancel", "pause", "resume"] | None
    effective_at: datetime | None
    resume_at: datetime | None


class SubscriptionBase(BaseModel):
    status: str | None
    customer_id: str | None
    address_id: str | None
    business_id: str | None
    currency_code: str | None
    created_at: datetime | None
    updated_at: datetime | None
    started_at: datetime | None
    first_billed_at: datetime | None
    next_billed_at: datetime | None
    paused_at: datetime | None
    canceled_at: datetime | None
    collection_mode: str | None
    billing_details: dict | None
    current_billing_period: BillingPeriod | None
    billing_cycle: BillingCycle | None
    recurring_transaction_details: dict | None
    scheduled_change: ScheduledChange | None
    items: list[Item] | None
    custom_data: dict | None
    management_urls: dict | None


class Subscription(SubscriptionBase):
    id: str | None
    next_transaction: Transaction | None
    immediate_transaction: Transaction | None


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
