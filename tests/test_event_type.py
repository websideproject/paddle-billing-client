import os

import deepdiff
import pytest
from apiclient.authentication_methods import HeaderAuthentication

from paddle_billing_client.models.event import EventType, EventTypesResponse


class TestEventType:
    def setup_class(self):
        from paddle_billing_client.client import PaddleApiClient  # pragma: no cover

        self.client = PaddleApiClient(
            authentication_method=HeaderAuthentication(
                token=os.getenv(
                    "PADDLE_SANDBOX_AUTH_TOKEN",
                )
            ),
        )

    @pytest.mark.vcr
    def test_list_event_types(self):
        event_types = self.client.list_event_types()
        expected_event_types = EventTypesResponse(
            data=[
                EventType(
                    name="transaction.billed",
                    description="Occurs when a transaction is billed. Its status field changes to billed and billed_at is populated.",
                    group="Transaction",
                    available_versions=[1],
                ),
                EventType(
                    name="transaction.canceled",
                    description="Occurs when a transaction is canceled. Its status field changes to canceled.",
                    group="Transaction",
                    available_versions=[1],
                ),
                EventType(
                    name="transaction.completed",
                    description="Occurs when a transaction is completed. Its status field changes to completed.",
                    group="Transaction",
                    available_versions=[1],
                ),
                EventType(
                    name="transaction.created",
                    description="Occurs when a transaction is created.",
                    group="Transaction",
                    available_versions=[1],
                ),
                EventType(
                    name="transaction.past_due",
                    description="Occurs when a transaction becomes past due. Its status field changes to past_due.",
                    group="Transaction",
                    available_versions=[1],
                ),
                EventType(
                    name="transaction.payment_failed",
                    description="Occurs when a payment fails for a transaction. The payments array is updated with details of the payment attempt.",
                    group="Transaction",
                    available_versions=[1],
                ),
                EventType(
                    name="transaction.ready",
                    description="Occurs when a transaction is ready to be billed. Its status field changes to ready.",
                    group="Transaction",
                    available_versions=[1],
                ),
                EventType(
                    name="transaction.updated",
                    description="Occurs when a transaction is updated.",
                    group="Transaction",
                    available_versions=[1],
                ),
                EventType(
                    name="subscription.activated",
                    description="Occurs when a subscription becomes active. Its status field changes to active. This means any trial period has elapsed and Paddle has successfully billed the customer.",
                    group="Subscription",
                    available_versions=[1],
                ),
                EventType(
                    name="subscription.canceled",
                    description="Occurs when a subscription is canceled. Its status field changes to canceled.",
                    group="Subscription",
                    available_versions=[1],
                ),
                EventType(
                    name="subscription.created",
                    description="Occurs when a subscription is created. subscription.trialing or subscription.activated typically follow.",
                    group="Subscription",
                    available_versions=[1],
                ),
                EventType(
                    name="subscription.imported",
                    description="Occurs when a subscription is imported.",
                    group="Subscription",
                    available_versions=[1],
                ),
                EventType(
                    name="subscription.past_due",
                    description="Occurs when a subscription has an unpaid transaction. Its status changes to past_due.",
                    group="Subscription",
                    available_versions=[1],
                ),
                EventType(
                    name="subscription.paused",
                    description="Occurs when a subscription is paused. Its status field changes to paused.",
                    group="Subscription",
                    available_versions=[1],
                ),
                EventType(
                    name="subscription.resumed",
                    description="Occurs when a subscription is resumed after being paused. Its status field changes to active.",
                    group="Subscription",
                    available_versions=[1],
                ),
                EventType(
                    name="subscription.trialing",
                    description="Occurs when a subscription enters trial period.",
                    group="Subscription",
                    available_versions=[1],
                ),
                EventType(
                    name="subscription.updated",
                    description="Occurs when a subscription is updated.",
                    group="Subscription",
                    available_versions=[1],
                ),
                EventType(
                    name="product.created",
                    description="Occurs when a product is created.",
                    group="Product",
                    available_versions=[1],
                ),
                EventType(
                    name="product.updated",
                    description="Occurs when a product is updated.",
                    group="Product",
                    available_versions=[1],
                ),
                EventType(
                    name="price.created",
                    description="Occurs when a price is created.",
                    group="Price",
                    available_versions=[1],
                ),
                EventType(
                    name="price.updated",
                    description="Occurs when a price is updated.",
                    group="Price",
                    available_versions=[1],
                ),
                EventType(
                    name="customer.created",
                    description="Occurs when a customer is created.",
                    group="Customer",
                    available_versions=[1],
                ),
                EventType(
                    name="customer.updated",
                    description="Occurs when a customer is updated.",
                    group="Customer",
                    available_versions=[1],
                ),
                EventType(
                    name="address.created",
                    description="Occurs when an address is created.",
                    group="Address",
                    available_versions=[1],
                ),
                EventType(
                    name="address.updated",
                    description="Occurs when an address is updated.",
                    group="Address",
                    available_versions=[1],
                ),
                EventType(
                    name="business.created",
                    description="Occurs when a business is created.",
                    group="Business",
                    available_versions=[1],
                ),
                EventType(
                    name="business.updated",
                    description="Occurs when a business is updated.",
                    group="Business",
                    available_versions=[1],
                ),
                EventType(
                    name="adjustment.created",
                    description="Occurs when an adjustment is created.",
                    group="Adjustment",
                    available_versions=[1],
                ),
                EventType(
                    name="adjustment.updated",
                    description="Occurs when an adjustment is updated, the only time an adjustment will be updated is when the status changes from pending to approved or from pending to rejected.",
                    group="Adjustment",
                    available_versions=[1],
                ),
                EventType(
                    name="payout.created",
                    description="Occurs when a payout is created.",
                    group="Payout",
                    available_versions=[1],
                ),
                EventType(
                    name="payout.paid",
                    description="Occurs when a payout is paid.",
                    group="Payout",
                    available_versions=[1],
                ),
            ],
            meta=dict(request_id="ae438f57-5db5-458e-8b72-f39f07c7434c"),
        )

        assert (
            deepdiff.DeepDiff(event_types, expected_event_types, ignore_order=True)
            == {}
        )
