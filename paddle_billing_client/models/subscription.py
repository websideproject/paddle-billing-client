from __future__ import annotations

from typing import Literal

from datetime import datetime

from pydantic import ConfigDict, model_validator

from paddle_billing_client.models.base import LazyBaseModel as BaseModel
from paddle_billing_client.models.base import PaddleResponse
from paddle_billing_client.models.common import (
    BillingDetails,
    BillingPeriod,
    ImportMeta,
)
from paddle_billing_client.models.price import BillingCycle, Price
from paddle_billing_client.models.transaction import Transaction


class Item(BaseModel):
    price: Price | None = None
    price_id: str | None = None
    status: str | None = None
    quantity: int | None = None
    recurring: bool | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None
    next_billed_at: datetime | None = None
    previously_billed_at: datetime | None = None


class ScheduledChange(BaseModel):
    action: Literal["cancel", "pause", "resume"] | None = None
    effective_at: datetime | None = None
    resume_at: datetime | None = None


class SubscriptionDiscount(BaseModel):
    id: str
    starts_at: datetime | None = None
    ends_at: datetime | None = None


class SubscriptionBase(BaseModel):
    status: str | None = None
    customer_id: str | None = None
    address_id: str | None = None
    business_id: str | None = None
    currency_code: str | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None
    started_at: datetime | None = None
    first_billed_at: datetime | None = None
    next_billed_at: datetime | None = None
    paused_at: datetime | None = None
    canceled_at: datetime | None = None
    collection_mode: str | None = None
    billing_details: BillingDetails | None = None
    current_billing_period: BillingPeriod | None = None
    billing_cycle: BillingCycle | None = None
    recurring_transaction_details: dict | None = None
    scheduled_change: ScheduledChange | None = None
    items: list[Item] | None = None
    custom_data: dict[str, int | str | None | dict | list] | None = None
    management_urls: dict | None = None
    discount: SubscriptionDiscount | None = None


class Subscription(SubscriptionBase):
    id: str | None = None
    next_transaction: Transaction | None = None
    immediate_transaction: Transaction | None = None
    import_meta: ImportMeta | None = None


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

    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="after")
    def check_status(self):
        valid_statuses = ["active", "canceled", "past_due", "paused", "trialing"]
        if self.status and not all(
            [s in valid_statuses for s in self.status.split(",")]
        ):
            raise ValueError(
                f"Query param invalid status: {self.status}, allowed values: {valid_statuses}"
            )
        return self


class SubscriptionResponse(PaddleResponse):
    data: Subscription


class SubscriptionsResponse(PaddleResponse):
    data: list[Subscription]


class SubscriptionDiscountRequest(BaseModel):
    id: str
    effective_from: Literal["next_billing_period", "immediately"] | None = None


class SubscriptionRequest(SubscriptionBase):
    effective_from: datetime | Literal["next_billing_period", "immediately"] | None = (
        None
    )
    resume_at: datetime | None = None
    discount: SubscriptionDiscountRequest | None = None
