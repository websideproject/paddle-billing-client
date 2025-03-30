from __future__ import annotations

from typing import Literal

from datetime import datetime

from pydantic import ConfigDict, model_validator

from paddle_billing_client.models import LazyBaseModel as BaseModel
from paddle_billing_client.models import PaddleResponse
from paddle_billing_client.models.common import ImportMeta
from paddle_billing_client.models.price import Price


class ProductBase(BaseModel):
    name: str
    tax_category: Literal[
        "digital-goods",
        "ebooks",
        "implementation-services",
        "professional-services",
        "saas",
        "software-programming-services",
        "standard",
        "training-services",
        "website-hosting",
    ]
    description: str | None = None
    image_url: str | None = None
    custom_data: dict[str, int | str | None | dict | list] | None = None
    status: Literal["active", "archived"] | None = None
    type: Literal["custom", "standard"] | None = None


class Product(ProductBase):
    id: str
    created_at: datetime | None = None
    prices: list[Price] | None = None
    import_meta: ImportMeta | None = None


class ProductQueryParams(BaseModel):
    # Return entities after the specified cursor. Used for working through paginated results.
    after: str | None = None
    # Return only the IDs specified. Use a comma separated list to get multiple entities.
    id: str | None = None
    # Include related entities in the response.
    include: Literal["prices"] | None = None
    # Order returned entities by the specified field and direction ([ASC] or [DESC]).
    order_by: Literal["[ASC]", "[DESC]"] | None = None
    # Set how many entities are returned per page. Default: 50
    per_page: int | None = None
    # Return entities that match the specified status. Use a comma separated list to specify multiple status values.
    status: str | None = None
    # Return entities that match the specified tax category.
    tax_category: None | (
        Literal[
            "digital-goods",
            "ebooks",
            "implementation-services",
            "professional-services",
            "saas",
            "software-programming-services",
            "standard",
            "training-services",
            "website-hosting",
        ]
    ) = None

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


class ProductResponse(PaddleResponse):
    data: Product


class ProductsResponse(PaddleResponse):
    data: list[Product]


class ProductRequest(ProductBase):
    pass
