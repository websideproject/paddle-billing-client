from typing import Dict, List, Literal, Optional

from pydantic import validator

from paddle_billing_client.models import LazyBaseModel as BaseModel
from paddle_billing_client.models import PaddleResponse


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
    country_codes: List[str]
    unit_price: UnitPrice


class PriceBase(BaseModel):
    description: str
    product_id: Optional[str]
    billing_cycle: Optional[BillingCycle]
    trial_period: Optional[str]
    tax_mode: str
    unit_price_overrides: Optional[List[UnitPriceOverride]]
    quantity: Optional[Quantity]
    custom_data: Optional[Dict[str, str]]


class Price(PriceBase):
    id: str
    unit_price: UnitPrice
    status: Optional[str]


class PriceQueryParams(BaseModel):
    # Return entities after the specified cursor. Used for working through paginated results.
    after: Optional[str] = None
    # Return only the IDs specified. Use a comma separated list to get multiple entities.
    id: Optional[str] = None
    # Include related entities in the response.
    include: Optional[Literal["product"]] = None
    # Order returned entities by the specified field and direction ([ASC] or [DESC]).
    order_by: Optional[Literal["[ASC]", "[DESC]"]] = None
    # Set how many entities are returned per page. Default: 50
    per_page: Optional[int] = None
    # Return entities that match the specified status. Use a comma separated list to specify multiple status values.
    status: Optional[str] = None
    # Determine whether returned entities are for recurring prices (true) or one-time prices (false).
    recurring: Optional[bool] = None

    @validator("status", allow_reuse=True)
    def check_status(cls, v: str) -> str:  # pragma: no cover
        valid_statuses = ["active", "archived"]
        if not all([s in valid_statuses for s in v.split(",")]):
            raise ValueError(
                f"Query param invalid status: {v}, allowed values: {valid_statuses}"
            )
        return v


class PriceResponse(PaddleResponse):
    data: Price


class PricesResponse(PaddleResponse):
    data: List[Price]


class PriceRequest(PriceBase):
    pass
