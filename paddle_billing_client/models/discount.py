from typing import List, Literal, Optional

from datetime import datetime

from pydantic import validator

from paddle_billing_client.models import LazyBaseModel as BaseModel
from paddle_billing_client.models import PaddleResponse


class DiscountBase(BaseModel):
    amount: str
    description: str
    type: Literal["flat", "flat_per_seat", "percentage"]
    enabled_for_checkout: bool
    code: str
    currency_code: str
    recur: bool
    maximum_recurring_intervals: Optional[int]
    usage_limit: Optional[int]
    restrict_to: Optional[List[str]]
    expires_at: Optional[datetime]
    status: Optional[Literal["active", "archived", "expired", "used"]]


class Discount(DiscountBase):
    id: str
    times_used: int
    created_at: Optional[datetime]
    updated_at: Optional[datetime]


class DiscountQueryParams(BaseModel):
    # Return entities after the specified cursor. Used for working through paginated results.
    after: Optional[str] = None
    # Return entities that match the discount code. Use a comma separated list to specify multiple discount codes.
    code: Optional[str] = None
    # Return only the IDs specified. Use a comma separated list to get multiple entities.
    id: Optional[str] = None
    # Order returned entities by the specified field and direction ([ASC] or [DESC]).
    order_by: Optional[Literal["[ASC]", "[DESC]"]] = None
    # Set how many entities are returned per page. Default: 50
    per_page: Optional[int] = None
    # Return entities that match the specified status. Use a comma separated list to specify multiple status values.
    status: Optional[str] = None

    @validator("status", allow_reuse=True)
    def check_status(cls, v: str) -> str:  # pragma: no cover
        valid_statuses = ["active", "archived", "expired", "used"]
        if not all([s in valid_statuses for s in v.split(",")]):
            raise ValueError(
                f"Query param invalid status: {v}, allowed values: {valid_statuses}"
            )
        return v


class DiscountResponse(PaddleResponse):
    data: Discount


class DiscountsResponse(PaddleResponse):
    data: List[Discount]


class DiscountRequest(DiscountBase):
    pass
