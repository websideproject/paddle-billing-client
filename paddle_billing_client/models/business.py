from __future__ import annotations

from typing import Literal

from datetime import datetime

from pydantic import ConfigDict, model_validator

from paddle_billing_client.models import LazyBaseModel as BaseModel
from paddle_billing_client.models import PaddleResponse
from paddle_billing_client.models.common import ImportMeta


class Contact(BaseModel):
    name: str
    email: str


class BusinessBase(BaseModel):
    name: str
    company_number: str | None = None
    tax_identifier: str | None = None
    contacts: list[Contact]
    status: Literal["active", "archived"] | None = None
    custom_data: dict[str, int | str | None | dict | list] | None = None


class Business(BusinessBase):
    id: str
    import_meta: ImportMeta | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None


class BusinessQueryParams(BaseModel):
    # Return entities after the specified cursor. Used for working through paginated results.
    after: str | None = None
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


class BusinessResponse(PaddleResponse):
    data: Business


class BusinessesResponse(PaddleResponse):
    data: list[Business]


class BusinessRequest(BusinessBase):
    pass
