from __future__ import annotations

from typing import Literal

from datetime import datetime

from pydantic import ConfigDict, Field, model_validator

from paddle_billing_client.models import LazyBaseModel as BaseModel
from paddle_billing_client.models import PaddleResponse
from paddle_billing_client.utils import parse_event_to_model


class NotificationIdPathParams(BaseModel):
    notificationId: str


class NotificationPayload(BaseModel):
    notification_id: str
    event_id: str
    event_type: str
    data: dict | BaseModel
    occurred_at: datetime

    @model_validator(mode="after")
    def check_status(self):
        self.data = parse_event_to_model(self.event_type, self.data)
        return self


class Notification(BaseModel):
    id: str
    type: str
    status: str
    payload: NotificationPayload
    occurred_at: datetime
    delivered_at: datetime | None = None
    replayed_at: str | None = None
    origin: str
    last_attempt_at: datetime | None = None
    retry_at: str | None = None
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

    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="after")
    def check_status(self):
        valid_statuses = ["delivered", "failed", "needs_retry", "not_attempted"]
        if self.status and not all(
            [s in valid_statuses for s in self.status.split(",")]
        ):
            raise ValueError(
                f"Query param invalid status: {self.status}, allowed values: {valid_statuses}"
            )
        return self


class NotificationResponse(PaddleResponse):
    data: Notification


class NotificationsResponse(PaddleResponse):
    data: list[Notification]


class NotificationReplay(BaseModel):
    event_id: str | None = None


class NotificationReplayResponse(PaddleResponse):
    data: NotificationReplay
