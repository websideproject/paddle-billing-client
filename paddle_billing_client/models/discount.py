from __future__ import annotations

from typing import Literal

from datetime import datetime

from pydantic import ConfigDict, model_validator

from paddle_billing_client.models import LazyBaseModel as BaseModel
from paddle_billing_client.models import PaddleResponse
from paddle_billing_client.models.common import ImportMeta


class DiscountBase(BaseModel):
    amount: str
    description: str
    type: Literal["flat", "flat_per_seat", "percentage"]
    enabled_for_checkout: bool
    code: str
    currency_code: str | None = None
    recur: bool
    maximum_recurring_intervals: int | None = None
    usage_limit: int | None = None
    restrict_to: list[str] | None = None
    expires_at: datetime | None = None
    status: Literal["active", "archived", "expired", "used"] | None = None
    custom_data: dict[str, int | str | None | dict | list] | None = None


class Discount(DiscountBase):
    id: str
    times_used: int | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None
    external_id: str | None = None
    import_meta: ImportMeta | None = None


class DiscountQueryParams(BaseModel):
    # Return entities after the specified cursor. Used for working through paginated results.
    after: str | None = None
    # Return entities that match the discount code. Use a comma separated list to specify multiple discount codes.
    code: str | None = None
    # Return only the IDs specified. Use a comma separated list to get multiple entities.
    id: str | None = None
    # Order returned entities by the specified field and direction ([ASC] or [DESC]).
    order_by: Literal["[ASC]", "[DESC]"] | None = None
    # Set how many entities are returned per page. Default: 50
    per_page: int | None = None
    # Return entities that match the specified status. Use a comma separated list to specify multiple status values.
    status: str | None = None

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
    data: list[Discount]


class DiscountRequest(DiscountBase):
    pass
