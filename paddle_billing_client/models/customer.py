from typing import Dict, List, Literal, Optional

from datetime import datetime

from pydantic import ConfigDict, model_validator

from paddle_billing_client.models import LazyBaseModel as BaseModel
from paddle_billing_client.models import PaddleResponse


class CustomerBase(BaseModel):
    email: str
    name: Optional[str] = None
    locale: Optional[str] = None
    custom_data: Optional[Dict[str, str]] = None


class Customer(CustomerBase):
    id: str
    marketing_consent: bool
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    imported_at: Optional[datetime] = None
    source: Optional[str] = None
    status: Optional[Literal["active", "archived"]] = None
    is_sanctioned: Optional[bool] = None
    tax_exemptions: Optional[List[str]] = None


class CustomerQueryParams(BaseModel):
    # Return entities after the specified cursor. Used for working through paginated results.
    after: Optional[str] = None
    # Return only the IDs specified. Use a comma separated list to get multiple entities.
    id: Optional[str] = None
    # Order returned entities by the specified field and direction ([ASC] or [DESC]).
    order_by: Optional[Literal["[ASC]", "[DESC]"]] = None
    # Set how many entities are returned per page. Default: 50
    per_page: Optional[int] = None
    # Return entities that match a search query. Searches id and type fields.
    search: Optional[str] = None
    # Return entities that match the specified status. Use a comma separated list to specify multiple status values.
    status: Optional[str] = None

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
    data: List[Customer]


class CustomerRequest(CustomerBase):
    pass


class CustomerBalancesQueryParams(BaseModel):
    # Return entities that match the currency code. Use a comma separated list to specify multiple currency codes.
    currency_code: Optional[str] = None

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
    data: List[CustomerBalance]
