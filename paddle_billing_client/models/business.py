from typing import List, Literal, Optional

from datetime import datetime

from pydantic import validator

from paddle_billing_client.models import LazyBaseModel as BaseModel
from paddle_billing_client.models import PaddleResponse


class Contact(BaseModel):
    name: str
    email: str


class BusinessBase(BaseModel):
    name: str
    company_number: str
    tax_identifier: str
    contacts: List[Contact]
    status: Optional[Literal["active", "archived"]]


class Business(BusinessBase):
    id: str
    created_at: datetime
    updated_at: datetime


class BusinessQueryParams(BaseModel):
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

    @validator("status")
    def check_status(cls, v: str) -> str:
        valid_statuses = ["active", "archived"]
        if not all([s in valid_statuses for s in v.split(",")]):
            raise ValueError(
                f"Query param invalid status: {v}, allowed values: {valid_statuses}"
            )
        return v


class BusinessResponse(PaddleResponse):
    data: Business


class BusinessesResponse(PaddleResponse):
    data: List[Business]


class BusinessRequest(BusinessBase):
    pass
