import os

import deepdiff
import pytest
from apiclient import HeaderAuthentication

from paddle_billing_client.models.notification_setting import (
    NotificationSetting,
    NotificationSettingRequest,
    NotificationSettingResponse,
    NotificationSettingsResponse,
    SubscribedEvent,
)


class TestNotificationSetting:
    def setup_class(self):
        from paddle_billing_client.client import PaddleApiClient  # pragma: no cover

        self.client = PaddleApiClient(
            authentication_method=HeaderAuthentication(
                token=os.getenv(
                    "PADDLE_SANDBOX_AUTH_TOKEN",
                )
            ),
        )

    """
    create_notification_setting: str = "notification-settings"
    get_notification_setting: str = "notification-settings/{notification_setting_id}"
    list_notification_settings: str = "notification-settings"
    update_notification_setting: str = "notification-settings/{notification_setting_id}"
    delete_notification_setting: str = "notification-settings/{notification_setting_id}"
    """

    @pytest.mark.vcr
    def test_create_notification_setting(self):
        notification_setting = self.client.create_notification_setting(
            data=NotificationSettingRequest(
                description="Test Notification Setting",
                destination="https://webhook.site/8b4f9b9f-1b0e-4b3c-8d7f-4d3f0e0a6b3b",
                api_version=1,
                include_sensitive_fields=False,
                active=True,
                type="url",
                subscribed_events=[
                    "transaction.billed",
                    "transaction.canceled",
                    "transaction.completed",
                    "transaction.created",
                    "transaction.payment_failed",
                    "transaction.ready",
                    "transaction.updated",
                    "subscription.activated",
                    "subscription.created",
                    "subscription.past_due",
                    "subscription.paused",
                    "subscription.resumed",
                    "subscription.trialing",
                    "subscription.updated",
                ],
            )
        )
        expected_notification_setting = NotificationSettingResponse(
            data=NotificationSetting(
                description="Test Notification Setting",
                destination="https://webhook.site/8b4f9b9f-1b0e-4b3c-8d7f-4d3f0e0a6b3b",
                subscribed_events=[
                    SubscribedEvent(
                        name="transaction.billed",
                        description="Occurs when a transaction is billed. Its status field changes to billed and billed_at is populated.",
                        group="Transaction",
                        available_versions=[1],
                    ),
                    SubscribedEvent(
                        name="transaction.canceled",
                        description="Occurs when a transaction is canceled. Its status field changes to canceled.",
                        group="Transaction",
                        available_versions=[1],
                    ),
                    SubscribedEvent(
                        name="transaction.completed",
                        description="Occurs when a transaction is completed. Its status field changes to completed.",
                        group="Transaction",
                        available_versions=[1],
                    ),
                    SubscribedEvent(
                        name="transaction.created",
                        description="Occurs when a transaction is created.",
                        group="Transaction",
                        available_versions=[1],
                    ),
                    SubscribedEvent(
                        name="transaction.payment_failed",
                        description="Occurs when a payment fails for a transaction. The payments array is updated with details of the payment attempt.",
                        group="Transaction",
                        available_versions=[1],
                    ),
                    SubscribedEvent(
                        name="transaction.ready",
                        description="Occurs when a transaction is ready to be billed. Its status field changes to ready.",
                        group="Transaction",
                        available_versions=[1],
                    ),
                    SubscribedEvent(
                        name="transaction.updated",
                        description="Occurs when a transaction is updated.",
                        group="Transaction",
                        available_versions=[1],
                    ),
                    SubscribedEvent(
                        name="subscription.activated",
                        description="Occurs when a subscription becomes active. Its status field changes to active. This means any trial period has elapsed and Paddle has successfully billed the customer.",
                        group="Subscription",
                        available_versions=[1],
                    ),
                    SubscribedEvent(
                        name="subscription.created",
                        description="Occurs when a subscription is created. subscription.trialing or subscription.activated typically follow.",
                        group="Subscription",
                        available_versions=[1],
                    ),
                    SubscribedEvent(
                        name="subscription.past_due",
                        description="Occurs when a subscription has an unpaid transaction. Its status changes to past_due.",
                        group="Subscription",
                        available_versions=[1],
                    ),
                    SubscribedEvent(
                        name="subscription.paused",
                        description="Occurs when a subscription is paused. Its status field changes to paused.",
                        group="Subscription",
                        available_versions=[1],
                    ),
                    SubscribedEvent(
                        name="subscription.resumed",
                        description="Occurs when a subscription is resumed after being paused. Its status field changes to active.",
                        group="Subscription",
                        available_versions=[1],
                    ),
                    SubscribedEvent(
                        name="subscription.trialing",
                        description="Occurs when a subscription enters trial period.",
                        group="Subscription",
                        available_versions=[1],
                    ),
                    SubscribedEvent(
                        name="subscription.updated",
                        description="Occurs when a subscription is updated.",
                        group="Subscription",
                        available_versions=[1],
                    ),
                ],
                type="url",
                active=True,
                api_version=1,
                include_sensitive_fields=False,
                id="ntfset_01h9gb2gj5grek32ptb024ygke",
                endpoint_secret_key="pdl_ntfset_01h9gb2gj5grek32ptb024ygke_+ahXo6Zd7+PnDE/9f7BPSMOlqIY+9YRl",
            ),
            meta=dict(request_id="55ba1328-e1d5-4ef6-b586-9cb10537833b"),
        )

        assert (
            deepdiff.DeepDiff(
                notification_setting, expected_notification_setting, ignore_order=True
            )
            == {}
        )

        assert isinstance(notification_setting, NotificationSettingResponse)
        assert isinstance(notification_setting.data, NotificationSetting)
        assert notification_setting.data.description == "Test Notification Setting"

    @pytest.mark.vcr
    def test_get_notification_setting(self):
        notification_setting = self.client.get_notification_setting(
            notification_setting_id="ntfset_01h9gb2gj5grek32ptb024ygke",
        )
        expected_notification_setting = NotificationSettingResponse(
            data=NotificationSetting(
                description="Test Notification Setting",
                destination="https://webhook.site/8b4f9b9f-1b0e-4b3c-8d7f-4d3f0e0a6b3b",
                subscribed_events=[
                    SubscribedEvent(
                        name="transaction.billed",
                        description="Occurs when a transaction is billed. Its status field changes to billed and billed_at is populated.",
                        group="Transaction",
                        available_versions=[1],
                    ),
                    SubscribedEvent(
                        name="transaction.canceled",
                        description="Occurs when a transaction is canceled. Its status field changes to canceled.",
                        group="Transaction",
                        available_versions=[1],
                    ),
                    SubscribedEvent(
                        name="transaction.completed",
                        description="Occurs when a transaction is completed. Its status field changes to completed.",
                        group="Transaction",
                        available_versions=[1],
                    ),
                    SubscribedEvent(
                        name="transaction.created",
                        description="Occurs when a transaction is created.",
                        group="Transaction",
                        available_versions=[1],
                    ),
                    SubscribedEvent(
                        name="transaction.payment_failed",
                        description="Occurs when a payment fails for a transaction. The payments array is updated with details of the payment attempt.",
                        group="Transaction",
                        available_versions=[1],
                    ),
                    SubscribedEvent(
                        name="transaction.ready",
                        description="Occurs when a transaction is ready to be billed. Its status field changes to ready.",
                        group="Transaction",
                        available_versions=[1],
                    ),
                    SubscribedEvent(
                        name="transaction.updated",
                        description="Occurs when a transaction is updated.",
                        group="Transaction",
                        available_versions=[1],
                    ),
                    SubscribedEvent(
                        name="subscription.activated",
                        description="Occurs when a subscription becomes active. Its status field changes to active. This means any trial period has elapsed and Paddle has successfully billed the customer.",
                        group="Subscription",
                        available_versions=[1],
                    ),
                    SubscribedEvent(
                        name="subscription.created",
                        description="Occurs when a subscription is created. subscription.trialing or subscription.activated typically follow.",
                        group="Subscription",
                        available_versions=[1],
                    ),
                    SubscribedEvent(
                        name="subscription.past_due",
                        description="Occurs when a subscription has an unpaid transaction. Its status changes to past_due.",
                        group="Subscription",
                        available_versions=[1],
                    ),
                    SubscribedEvent(
                        name="subscription.paused",
                        description="Occurs when a subscription is paused. Its status field changes to paused.",
                        group="Subscription",
                        available_versions=[1],
                    ),
                    SubscribedEvent(
                        name="subscription.resumed",
                        description="Occurs when a subscription is resumed after being paused. Its status field changes to active.",
                        group="Subscription",
                        available_versions=[1],
                    ),
                    SubscribedEvent(
                        name="subscription.trialing",
                        description="Occurs when a subscription enters trial period.",
                        group="Subscription",
                        available_versions=[1],
                    ),
                    SubscribedEvent(
                        name="subscription.updated",
                        description="Occurs when a subscription is updated.",
                        group="Subscription",
                        available_versions=[1],
                    ),
                ],
                type="url",
                active=True,
                api_version=1,
                include_sensitive_fields=False,
                id="ntfset_01h9gb2gj5grek32ptb024ygke",
                endpoint_secret_key="pdl_ntfset_01h9gb2gj5grek32ptb024ygke_+ahXo6Zd7+PnDE/9f7BPSMOlqIY+9YRl",
            ),
            meta=dict(request_id="9fdbcd42-c03d-4871-8275-aa7cc163b13e"),
        )

        assert (
            deepdiff.DeepDiff(
                notification_setting, expected_notification_setting, ignore_order=True
            )
            == {}
        )

        assert isinstance(notification_setting, NotificationSettingResponse)
        assert isinstance(notification_setting.data, NotificationSetting)
        assert notification_setting.data.description == "Test Notification Setting"

    @pytest.mark.vcr
    def test_list_notification_settings(self):
        notification_settings = self.client.list_notification_settings()
        expected_notification_settings = NotificationSettingsResponse(
            data=[
                NotificationSetting(
                    description="Test Notification Setting",
                    destination="https://webhook.site/8b4f9b9f-1b0e-4b3c-8d7f-4d3f0e0a6b3b",
                    subscribed_events=[
                        SubscribedEvent(
                            name="transaction.billed",
                            description="Occurs when a transaction is billed. Its status field changes to billed and billed_at is populated.",
                            group="Transaction",
                            available_versions=[1],
                        ),
                        SubscribedEvent(
                            name="transaction.canceled",
                            description="Occurs when a transaction is canceled. Its status field changes to canceled.",
                            group="Transaction",
                            available_versions=[1],
                        ),
                        SubscribedEvent(
                            name="transaction.completed",
                            description="Occurs when a transaction is completed. Its status field changes to completed.",
                            group="Transaction",
                            available_versions=[1],
                        ),
                        SubscribedEvent(
                            name="transaction.created",
                            description="Occurs when a transaction is created.",
                            group="Transaction",
                            available_versions=[1],
                        ),
                        SubscribedEvent(
                            name="transaction.payment_failed",
                            description="Occurs when a payment fails for a transaction. The payments array is updated with details of the payment attempt.",
                            group="Transaction",
                            available_versions=[1],
                        ),
                        SubscribedEvent(
                            name="transaction.ready",
                            description="Occurs when a transaction is ready to be billed. Its status field changes to ready.",
                            group="Transaction",
                            available_versions=[1],
                        ),
                        SubscribedEvent(
                            name="transaction.updated",
                            description="Occurs when a transaction is updated.",
                            group="Transaction",
                            available_versions=[1],
                        ),
                        SubscribedEvent(
                            name="subscription.activated",
                            description="Occurs when a subscription becomes active. Its status field changes to active. This means any trial period has elapsed and Paddle has successfully billed the customer.",
                            group="Subscription",
                            available_versions=[1],
                        ),
                        SubscribedEvent(
                            name="subscription.created",
                            description="Occurs when a subscription is created. subscription.trialing or subscription.activated typically follow.",
                            group="Subscription",
                            available_versions=[1],
                        ),
                        SubscribedEvent(
                            name="subscription.past_due",
                            description="Occurs when a subscription has an unpaid transaction. Its status changes to past_due.",
                            group="Subscription",
                            available_versions=[1],
                        ),
                        SubscribedEvent(
                            name="subscription.paused",
                            description="Occurs when a subscription is paused. Its status field changes to paused.",
                            group="Subscription",
                            available_versions=[1],
                        ),
                        SubscribedEvent(
                            name="subscription.resumed",
                            description="Occurs when a subscription is resumed after being paused. Its status field changes to active.",
                            group="Subscription",
                            available_versions=[1],
                        ),
                        SubscribedEvent(
                            name="subscription.trialing",
                            description="Occurs when a subscription enters trial period.",
                            group="Subscription",
                            available_versions=[1],
                        ),
                        SubscribedEvent(
                            name="subscription.updated",
                            description="Occurs when a subscription is updated.",
                            group="Subscription",
                            available_versions=[1],
                        ),
                    ],
                    type="url",
                    active=True,
                    api_version=1,
                    include_sensitive_fields=False,
                    id="ntfset_01h9gb2gj5grek32ptb024ygke",
                    endpoint_secret_key="pdl_ntfset_01h9gb2gj5grek32ptb024ygke_+ahXo6Zd7+PnDE/9f7BPSMOlqIY+9YRl",
                ),
            ],
            meta=dict(
                request_id="24754b48-ed40-40de-bf30-ea696f0f9426",
            ),
        )

        assert (
            deepdiff.DeepDiff(
                notification_settings, expected_notification_settings, ignore_order=True
            )
            == {}
        )

        assert isinstance(notification_settings, NotificationSettingsResponse)
        assert isinstance(notification_settings.data, list)
        assert isinstance(notification_settings.data[0], NotificationSetting)
        assert notification_settings.data[0].description == "Test Notification Setting"

    @pytest.mark.vcr
    def test_update_notification_setting(self):
        notification_setting = self.client.update_notification_setting(
            notification_setting_id="ntfset_01h9gb2gj5grek32ptb024ygke",
            data=NotificationSettingRequest(
                description="Test Notification Setting 2",
                destination="https://webhook.site/8b4f9b9f-1b0e-4b3c-8d7f-4d3f0e0a6b3b",
                api_version=1,
                include_sensitive_fields=False,
                active=False,
                type="url",
                subscribed_events=[
                    "transaction.billed",
                    "transaction.canceled",
                    "transaction.completed",
                    "transaction.created",
                    "transaction.payment_failed",
                    "transaction.ready",
                    "transaction.updated",
                ],
            ),
        )
        expected_notification_setting = NotificationSettingResponse(
            data=NotificationSetting(
                description="Test Notification Setting 2",
                destination="https://webhook.site/8b4f9b9f-1b0e-4b3c-8d7f-4d3f0e0a6b3b",
                subscribed_events=[
                    SubscribedEvent(
                        name="transaction.billed",
                        description="Occurs when a transaction is billed. Its status field changes to billed and billed_at is populated.",
                        group="Transaction",
                        available_versions=[1],
                    ),
                    SubscribedEvent(
                        name="transaction.canceled",
                        description="Occurs when a transaction is canceled. Its status field changes to canceled.",
                        group="Transaction",
                        available_versions=[1],
                    ),
                    SubscribedEvent(
                        name="transaction.completed",
                        description="Occurs when a transaction is completed. Its status field changes to completed.",
                        group="Transaction",
                        available_versions=[1],
                    ),
                    SubscribedEvent(
                        name="transaction.created",
                        description="Occurs when a transaction is created.",
                        group="Transaction",
                        available_versions=[1],
                    ),
                    SubscribedEvent(
                        name="transaction.payment_failed",
                        description="Occurs when a payment fails for a transaction. The payments array is updated with details of the payment attempt.",
                        group="Transaction",
                        available_versions=[1],
                    ),
                    SubscribedEvent(
                        name="transaction.ready",
                        description="Occurs when a transaction is ready to be billed. Its status field changes to ready.",
                        group="Transaction",
                        available_versions=[1],
                    ),
                    SubscribedEvent(
                        name="transaction.updated",
                        description="Occurs when a transaction is updated.",
                        group="Transaction",
                        available_versions=[1],
                    ),
                ],
                type="url",
                active=False,
                api_version=1,
                include_sensitive_fields=False,
                id="ntfset_01h9gb2gj5grek32ptb024ygke",
                endpoint_secret_key="pdl_ntfset_01h9gb2gj5grek32ptb024ygke_+ahXo6Zd7+PnDE/9f7BPSMOlqIY+9YRl",
            ),
            meta=dict(request_id="6592c87a-7e37-4764-96ad-e43c04be8f7c"),
        )

        assert (
            deepdiff.DeepDiff(
                notification_setting, expected_notification_setting, ignore_order=True
            )
            == {}
        )

        assert isinstance(notification_setting, NotificationSettingResponse)
        assert isinstance(notification_setting.data, NotificationSetting)
        assert notification_setting.data.description == "Test Notification Setting 2"
        assert notification_setting.data.active is False

    @pytest.mark.vcr
    def test_delete_notification_setting(self):
        response = self.client.delete_notification_setting(
            notification_setting_id="ntfset_01h9gb2gj5grek32ptb024ygke",
        )

        assert response is None
