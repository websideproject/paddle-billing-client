from __future__ import annotations

from typing import Literal

from pydantic import ConfigDict, model_validator

from paddle_billing_client.models import LazyBaseModel as BaseModel
from paddle_billing_client.models import PaddleResponse
from paddle_billing_client.models.common import ImportMeta


class UnitPrice(BaseModel):
    amount: str
    currency_code: str


class Quantity(BaseModel):
    minimum: int
    maximum: int


class BillingCycle(BaseModel):
    interval: str
    frequency: int


class UnitPriceOverride(BaseModel):
    country_codes: list[str]
    unit_price: UnitPrice


class TrialPeriod(BaseModel):
    interval: str
    frequency: int


class PriceBase(BaseModel):
    description: str
    product_id: str | None = None
    billing_cycle: BillingCycle | None = None
    trial_period: TrialPeriod | None = None
    tax_mode: str
    unit_price_overrides: list[UnitPriceOverride] | None = None
    quantity: Quantity | None = None
    custom_data: dict[str, int | str | None | dict | list] | None = None
    type: Literal["custom", "standard"] | None = None
    name: str | None = None


class Price(PriceBase):
    id: str
    unit_price: UnitPrice
    status: str | None = None
    import_meta: ImportMeta | None = None


class PriceQueryParams(BaseModel):
    # Return entities after the specified cursor. Used for working through paginated results.
    after: str | None = None
    # Return only the IDs specified. Use a comma separated list to get multiple entities.
    id: str | None = None
    # Include related entities in the response.
    include: Literal["product"] | None = None
    # Order returned entities by the specified field and direction ([ASC] or [DESC]).
    order_by: Literal["[ASC]", "[DESC]"] | None = None
    # Set how many entities are returned per page. Default: 50
    per_page: int | None = None
    # Return entities that match the specified status. Use a comma separated list to specify multiple status values.
    status: str | None = None
    # Determine whether returned entities are for recurring prices (true) or one-time prices (false).
    recurring: bool | None = None

    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="after")
    def check_status(self):
        valid_statuses = ["active", "archived"]
        if self.status and not all(
            [s in valid_statuses for s in self.status.split(",")]
        ):
            raise ValueError(
                f"Query param invalid status: {self.status}, allowed values: {valid_statuses}"
            )
        return self


class PriceResponse(PaddleResponse):
    data: Price


class PricesResponse(PaddleResponse):
    data: list[Price]


class PriceRequest(PriceBase):
    pass
