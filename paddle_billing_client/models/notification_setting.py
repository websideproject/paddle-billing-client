from __future__ import annotations

from typing import List, Literal, Optional

from paddle_billing_client.models import LazyBaseModel as BaseModel
from paddle_billing_client.models import PaddleResponse


class SubscribedEvent(BaseModel):
    name: str
    description: str
    group: str
    available_versions: list[int]


class NotificationSettingBase(BaseModel):
    description: str
    destination: str
    subscribed_events: list[SubscribedEvent]
    type: Literal["email", "url"] | None = None
    active: bool
    api_version: int
    include_sensitive_fields: bool


class NotificationSetting(NotificationSettingBase):
    id: str
    endpoint_secret_key: str


class NotificationSettingResponse(PaddleResponse):
    data: NotificationSetting


class NotificationSettingsResponse(PaddleResponse):
    data: list[NotificationSetting]


class NotificationSettingRequest(NotificationSettingBase):
    subscribed_events: list[str]
