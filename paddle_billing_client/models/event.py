from __future__ import annotations

from typing import List, Literal, Optional

from datetime import datetime

from pydantic import root_validator

from paddle_billing_client.models import LazyBaseModel as BaseModel
from paddle_billing_client.models import PaddleResponse
from paddle_billing_client.utils import parse_event_to_model


class EventType(BaseModel):
    name: str
    description: str
    group: str
    available_versions: list[int]


class EventTypesResponse(PaddleResponse):
    data: list[EventType]


class EventQueryParams(BaseModel):
    # Return entities after the specified cursor. Used for working through paginated results.
    after: str | None = None
    # Order returned entities by the specified field and direction ([ASC] or [DESC]).
    order_by: Literal["[ASC]", "[DESC]"] | None = None
    # Set how many entities are returned per page. Default: 50
    per_page: int | None = None


class Event(BaseModel):
    notification_id: str | None
    event_id: str
    event_type: str
    data: dict
    occurred_at: datetime

    @root_validator(pre=False, allow_reuse=True)
    def select_data(cls, values):  # pragma: no cover
        values["data"] = parse_event_to_model(values["event_type"], values["data"])
        return values


class EventsResponse(PaddleResponse):
    data: list[Event]
