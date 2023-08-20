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
    next_billed_at: Optional[str]
    previously_billed_at: Optional[str]


class BillingPeriod(BaseModel):
    ends_at: str
    starts_at: str


class SubscriptionBase(BaseModel):
    status: str
    customer_id: str
    address_id: str
    business_id: Optional[str]
    currency_code: str
    created_at: datetime
    updated_at: datetime
    started_at: datetime
    first_billed_at: datetime
    next_billed_at: Optional[datetime]
    paused_at: Optional[datetime]
    canceled_at: Optional[datetime]
    collection_mode: str
    billing_details: Optional[dict]
    current_billing_period: BillingPeriod
    billing_cycle: BillingCycle
    recurring_transaction_details: Optional[dict]
    next_transaction: Optional[dict]
    scheduled_change: Optional[dict]
    items: List[Item]
    custom_data: Optional[dict]
    management_urls: Optional[dict]


class Subscription(SubscriptionBase):
    id: str


class SubscriptionQueryParams(BaseModel):
    # Return entities after the specified cursor. Used for working through paginated results.
    after: Optional[str] = None
    # Return entities related to the specified customer.
    # Use a comma separated list to specify multiple customer IDs.
    customer_id: Optional[str] = None
    # Order returned entities by the specified field and direction ([ASC] or [DESC]).
    order_by: Optional[Literal["[ASC]", "[DESC]"]] = None
    # Set how many entities are returned per page. Default: 50
    per_page: Optional[int] = None
    # Return entities related to the specified price. Use a comma separated list to specify multiple price IDs.
    price_id: Optional[str] = None
    # Return entities that match the specified status. Use a comma separated list to specify multiple status values.
    status: Optional[str] = None

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
    data: List[Subscription]


class SubscriptionRequest(SubscriptionBase):
    effective_from: Optional[datetime | Literal["next_billing_period", "immediately"]]
    resume_at: Optional[datetime]
