from __future__ import annotations

from typing import Any, Dict, List, Literal, Optional

from datetime import datetime

from pydantic import Extra, validator
from pydantic.types import Enum

from paddle_billing_client.models.base import LazyBaseModel as BaseModel
from paddle_billing_client.models.base import PaddleResponse
from paddle_billing_client.models.common import BillingPeriod


class AdjustmentAction(str, Enum):
    refund = "refund"
    credit = "credit"
    chargeback = "chargeback"
    chargeback_warning = "chargeback_warning"


class AdjustmentStatus(str, Enum):
    pending_approval = "pending_approval"
    approved = "approved"
    rejected = "rejected"


class AdjustmentItemProration(BaseModel):
    rate: str
    billing_period: BillingPeriod | None


class AdjustmentItem(BaseModel):
    id: str | None
    item_id: str
    type: str
    amount: str
    proration: AdjustmentItemProration | None
    totals: dict | None


class AdjustmentBase(BaseModel):
    # How this adjustment impacts the related transaction.
    # 'refund' adjustments must be approved by Paddle, and are created with the status 'pending_approval'.
    # 'chargeback' and 'chargeback_warning' adjustments are created automatically by Paddle.
    action: AdjustmentAction
    transaction_id: str
    reason: str | None
    items: list[AdjustmentItem]


class Adjustment(AdjustmentBase):
    id: str
    subscription_id: str | None
    customer_id: str
    currency_code: str
    # Status of this adjustment. Set automatically by Paddle.
    # 'refund' adjustments must be approved by Paddle,
    # and are created with the status 'pending_approval' until they move to 'approved' or 'rejected' on review.
    # 'credit' adjustments are created with the status 'approved'.
    status: AdjustmentStatus
    totals: dict
    payout_totals: dict | None
    created_at: datetime
    updated_at: datetime


class AdjustmentQueryParams(BaseModel):
    # Return entities for the specified action.
    action: AdjustmentAction | None
    # Return entities after the specified cursor. Used for working through paginated results.
    after: str | None = None
    # Return entities related to the specified customer. Use a comma separated list to specify multiple customer IDs.
    customer_id: str | None
    # Order returned entities by the specified field and direction ([ASC] or [DESC]).
    order_by: Literal["[ASC]", "[DESC]"] | None = None
    # Set how many entities are returned per page. Default: 50
    per_page: int | None = None
    # Return entities that match the specified status. Use a comma separated list to specify multiple status values.
    status: str | None = None
    # Return entities related to the specified subscription.
    # Use a comma separated list to specify multiple subscription IDs.
    subscription_id: str | None
    # Return entities related to the specified transaction.
    # Use a comma separated list to specify multiple transaction IDs.
    transaction_id: str | None
    # Return only the IDs specified.
    # Use a comma separated list to get multiple entities.
    id: str | None = None

    class Config:
        extra = Extra.forbid

    @validator("status", allow_reuse=True)
    def check_status(cls, v: str) -> str:  # pragma: no cover
        valid_statuses = ["approved", "pending_approval", "rejected", "reversed"]
        if not all([s in valid_statuses for s in v.split(",")]):
            raise ValueError(
                f"Query param invalid status: {v}, allowed values: {valid_statuses}"
            )
        return v


class AdjustmentResponse(PaddleResponse):
    data: Adjustment


class AdjustmentsResponse(PaddleResponse):
    data: list[Adjustment]


class AdjustmentRequest(AdjustmentBase):
    pass
