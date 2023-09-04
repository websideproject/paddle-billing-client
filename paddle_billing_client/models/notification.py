from __future__ import annotations

from typing import List, Literal, Optional

from datetime import datetime

from pydantic import Field, root_validator, validator

from paddle_billing_client.models import LazyBaseModel as BaseModel
from paddle_billing_client.models import PaddleResponse
from paddle_billing_client.utils import parse_event_to_model


class NotificationIdPathParams(BaseModel):
    notificationId: str


class NotificationPayload(BaseModel):
    notification_id: str
    event_id: str
    event_type: str
    data: dict
    occurred_at: datetime

    @root_validator(pre=False, allow_reuse=True)
    def select_data(cls, values):  # pragma: no cover
        values["data"] = parse_event_to_model(values["event_type"], values["data"])
        return values


class Notification(BaseModel):
    id: str
    type: str
    status: str
    payload: NotificationPayload
    occurred_at: datetime
    delivered_at: datetime
    replayed_at: str | None
    origin: str
    last_attempt_at: datetime
    retry_at: str | None
    times_attempted: int
    notification_setting_id: str


class NotificationQueryParams(BaseModel):
    # Return entities after the specified cursor. Used for working through paginated results.
    after: str | None = None
    # Return entities related to the specified notification destination.
    # Use a comma separated list to specify multiple notification destination IDs.
    notification_setting_id: str | None = None
    # Order returned entities by the specified field and direction ([ASC] or [DESC]).
    order_by: Literal["[ASC]", "[DESC]"] | None = None
    # Set how many entities are returned per page. Default: 50
    per_page: int | None = None
    # Return entities that match a search query. Searches id and type fields.
    search: str | None = None
    # Return entities that match the specified status. Use a comma separated list to specify multiple status values.
    status: str | None = None
    # Return entities that contain the Paddle ID specified. Pass a transaction, customer, or subscription ID.
    filter: str | None = None
    # Return entities up to a specific time.
    to: str | None = None
    # Return entities from a specific time.
    from_field: str | None = Field(None, alias="from")

    @validator("status", allow_reuse=True)
    def check_status(cls, v: str) -> str:  # pragma: no cover
        valid_statuses = ["delivered", "failed", "needs_retry", "not_attempted"]
        if not all([s in valid_statuses for s in v.split(",")]):
            raise ValueError(
                f"Query param invalid status: {v}, allowed values: {valid_statuses}"
            )
        return v


class NotificationResponse(PaddleResponse):
    data: Notification


class NotificationsResponse(PaddleResponse):
    data: list[Notification]


class NotificationReplay(BaseModel):
    event_id: str | None


class NotificationReplayResponse(PaddleResponse):
    data: NotificationReplay
