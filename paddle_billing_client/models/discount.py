from typing import Dict, List, Literal, Optional

from datetime import datetime

from pydantic import ConfigDict, model_validator

from paddle_billing_client.models import LazyBaseModel as BaseModel
from paddle_billing_client.models import PaddleResponse


class DiscountBase(BaseModel):
    amount: str
    description: str
    type: Literal["flat", "flat_per_seat", "percentage"]
    enabled_for_checkout: bool
    code: str
    currency_code: Optional[str] = None
    recur: bool
    maximum_recurring_intervals: Optional[int] = None
    usage_limit: Optional[int] = None
    restrict_to: Optional[List[str]] = None
    expires_at: Optional[datetime] = None
    status: Optional[Literal["active", "archived", "expired", "used"]] = None
    custom_data: Optional[Dict[str, str]] = None


class Discount(DiscountBase):
    id: str
    times_used: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    external_id: Optional[str] = None


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

    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="after")
    def check_status(self):
        valid_statuses = ["active", "archived", "expired", "used"]
        if self.status and not all(
            [s in valid_statuses for s in self.status.split(",")]
        ):
            raise ValueError(
                f"Query param invalid status: {self.status}, allowed values: {valid_statuses}"
            )
        return self


class DiscountResponse(PaddleResponse):
    data: Discount


class DiscountsResponse(PaddleResponse):
    data: List[Discount]


class DiscountRequest(DiscountBase):
    pass
