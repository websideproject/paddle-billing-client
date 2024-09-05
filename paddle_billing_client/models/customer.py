from __future__ import annotations

from typing import Literal

from datetime import datetime

from pydantic import ConfigDict, model_validator

from paddle_billing_client.models import LazyBaseModel as BaseModel
from paddle_billing_client.models import PaddleResponse
from paddle_billing_client.models.common import ImportMeta


class CustomerBase(BaseModel):
    email: str
    name: str | None = None
    locale: str | None = None
    custom_data: dict[str, int | str | None | dict | list] | None = None


class Customer(CustomerBase):
    id: str
    marketing_consent: bool
    created_at: datetime | None = None
    updated_at: datetime | None = None
    imported_at: datetime | None = None
    source: str | None = None
    status: Literal["active", "archived"] | None = None
    is_sanctioned: bool | None = None
    tax_exemptions: list[str] | None = None
    import_meta: ImportMeta | None = None


class CustomerQueryParams(BaseModel):
    # Return entities after the specified cursor. Used for working through paginated results.
    after: str | None = None
    # Return entities that exactly match the specified email address.
    # Use a comma separated list to specify multiple email addresses.
    # Recommended for precise matching of email addresses.
    email: str | None = None
    # Return only the IDs specified. Use a comma separated list to get multiple entities.
    id: str | None = None
    # Order returned entities by the specified field and direction ([ASC] or [DESC]).
    order_by: Literal["[ASC]", "[DESC]"] | None = None
    # Set how many entities are returned per page. Default: 50
    per_page: int | None = None
    # Return entities that match a search query. Searches id and type fields.
    search: str | None = None
    # Return entities that match the specified status. Use a comma separated list to specify multiple status values.
    status: str | None = None

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


class CustomerResponse(PaddleResponse):
    data: Customer


class CustomersResponse(PaddleResponse):
    data: list[Customer]


class CustomerRequest(CustomerBase):
    email: str | None = None


class CustomerBalancesQueryParams(BaseModel):
    # Return entities that match the currency code. Use a comma separated list to specify multiple currency codes.
    currency_code: str | None = None

    model_config = ConfigDict(extra="forbid")


class Balance(BaseModel):
    available: str
    reserved: str
    used: str


class CustomerBalance(BaseModel):
    customer_id: str
    currency_code: str
    balance: Balance


class CustomerBalancesResponse(PaddleResponse):
    data: list[CustomerBalance]
