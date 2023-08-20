from typing import Dict, List, Literal, Optional

from datetime import datetime

from pydantic import validator

from paddle_billing_client.models import LazyBaseModel as BaseModel
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
    description: Optional[str]
    image_url: Optional[str]
    custom_data: Optional[Dict[str, str]]
    status: Optional[Literal["active", "archived"]]


class Product(ProductBase):
    id: str
    created_at: Optional[datetime]
    prices: Optional[List[Price]]


class ProductQueryParams(BaseModel):
    # Return entities after the specified cursor. Used for working through paginated results.
    after: Optional[str] = None
    # Return only the IDs specified. Use a comma separated list to get multiple entities.
    id: Optional[str] = None
    # Include related entities in the response.
    include: Optional[Literal["prices"]] = None
    # Order returned entities by the specified field and direction ([ASC] or [DESC]).
    order_by: Optional[Literal["[ASC]", "[DESC]"]] = None
    # Set how many entities are returned per page. Default: 50
    per_page: Optional[int] = None
    # Return entities that match the specified status. Use a comma separated list to specify multiple status values.
    status: Optional[str] = None
    # Return entities that match the specified tax category.
    tax_category: Optional[
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
    ] = None

    @validator("status", allow_reuse=True)
    def check_status(cls, v: str) -> str:  # pragma: no cover
        valid_statuses = ["active", "archived"]
        if not all([s in valid_statuses for s in v.split(",")]):
            raise ValueError(
                f"Query param invalid status: {v}, allowed values: {valid_statuses}"
            )
        return v


class ProductResponse(BaseModel):
    data: Product


class ProductsResponse(BaseModel):
    data: List[Product]


class ProductRequest(ProductBase):
    pass
