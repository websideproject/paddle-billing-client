import os
from datetime import datetime

import deepdiff
import pytest
from apiclient import HeaderAuthentication

from paddle_billing_client.models.address import Address
from paddle_billing_client.models.common import BillingPeriod
from paddle_billing_client.models.customer import Customer
from paddle_billing_client.models.price import BillingCycle, Price, UnitPrice
from paddle_billing_client.models.product import Product
from paddle_billing_client.models.subscription import (
    Item,
    ScheduledChange,
    Subscription,
    SubscriptionQueryParams,
    SubscriptionRequest,
    SubscriptionResponse,
    SubscriptionsResponse,
)
from paddle_billing_client.models.transaction import (
    AdjustedTotals,
    LineItem,
    LineItemProration,
    LineItemTotals,
    LineItemUnitTotals,
    TaxRatesTotals,
    TaxRatesUsed,
    Totals,
    Transaction,
    TransactionDetails,
    TransactionResponse,
)


class TestSubscription:
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
    def test_get_subscription(self):
        subscription = self.client.get_subscription(
            subscription_id="sub_01h7n3a88jwktex2tfjzahmn57"
        )
        expected_subscription = SubscriptionResponse(
            data=Subscription(
                id="sub_01h7n3a88jwktex2tfjzahmn57",
                status="active",
                customer_id="ctm_01h7mrr5j8rnawwzh9nschgp1v",
                address_id="add_01h7mrzwtwthvqqy7vq90f0kd7",
                business_id=None,
                currency_code="USD",
                created_at="2023-08-12T14:44:57.746086Z",
                updated_at="2023-08-12T14:44:57.746086Z",
                started_at="2023-08-12T14:44:57.746081Z",
                first_billed_at="2023-08-12T14:44:57.746081Z",
                next_billed_at="2023-09-12T14:44:57.746081Z",
                paused_at=None,
                canceled_at=None,
                collection_mode="manual",
                billing_details=dict(
                    enable_checkout=True,
                    purchase_order_number="",
                    additional_information="",
                    payment_terms=dict(frequency=2, interval="week"),
                ),
                current_billing_period=dict(
                    starts_at="2023-08-12T14:44:57.746081Z",
                    ends_at="2023-09-12T14:44:57.746081Z",
                ),
                billing_cycle=dict(frequency=1, interval="month"),
                scheduled_change=None,
                items=[
                    {
                        "status": "active",
                        "quantity": 1,
                        "recurring": True,
                        "created_at": "2023-08-12T14:44:57.746087Z",
                        "updated_at": "2023-08-12T14:44:57.746087Z",
                        "previously_billed_at": "2023-08-12T14:44:57.746081Z",
                        "next_billed_at": "2023-09-12T14:44:57.746081Z",
                        "trial_dates": None,
                        "price": {
                            "id": "pri_01h7mrnc315chey77qhrd32vfs",
                            "product_id": "pro_01h7mrm9f0xvrvvwvkg1b7q8e3",
                            "description": "asd",
                            "tax_mode": "account_setting",
                            "billing_cycle": {"frequency": 1, "interval": "month"},
                            "trial_period": None,
                            "unit_price": {"amount": "1270", "currency_code": "USD"},
                        },
                    },
                ],
                custom_data=dict(user_id="123"),
                management_urls={
                    "update_payment_method": None,
                    "cancel": "https://sandbox-buyer-portal.paddle.com/subscriptions/sub_01h7n3a88jwktex2tfjzahmn57/cancel?token=pga_eyJhbGciOiJSUzI1NiIsImtpZCI6IjUwMWI4NGRhNWExYmIyODU2NDcyM2EzNDFkZGY5NTcyZDQwNDAwNDI4OTg3NzQyNjgzZWUyOWYyYTdmYjc0NDkiLCJ0eXAiOiJKV1QifQ.eyJpZCI6InBnYV8wMWg5Zm1lM2I0ZGI3bTduNnNtZTR2eWV5dyIsInNlbGxlci1pZCI6Ijg5MzkiLCJ0eXBlIjoic3RhbmRhcmQiLCJ2ZXJzaW9uIjoiMSIsInVzYWdlIjoibWFuYWdlbWVudF91cmwiLCJzY29wZSI6ImN1c3RvbWVyLnN1YnNjcmlwdGlvbi1wYXltZW50LnVwZGF0ZSBjdXN0b21lci5zdWJzY3JpcHRpb24tcGF5bWVudC5yZWFkIGN1c3RvbWVyLnN1YnNjcmlwdGlvbi1jYW5jZWwuY3JlYXRlIGN1c3RvbWVyLnN1YnNjcmlwdGlvbi5yZWFkIiwiaXNzIjoiZ3Vlc3RhY2Nlc3Mtc2VydmljZSIsInN1YiI6ImN0bV8wMWg3bXJyNWo4cm5hd3d6aDluc2NoZ3AxdiIsImlhdCI6MTY5MzgxNTYwNiwiZXhwIjoxNzI1NDM4MDA2fQ.EoPDg2jcSwZJ_Gu3-e0EwA6gNQW3qF6Tegh-Z0GC1RT4oO6phSSYR2Q6p7GXImaoqzw6ohS88x2bV2DaHXmagbmcvrv80vAq-UKRSfZfTPzvYhR5pN6RNeR95gxUmxZJrJ-IFehXsbHtwqiJNe7pkd8pY7tnmbw4rEHf5b6cPmXjfrJFI8N9IynJ_k6WJamA7rVjV81mtwxVUfWrW2a49bpaboyhM08eVAZL5ziQNBJynhsCm8wKVJTjiWm7t2iU3-sQ1yQh-JWQLYgck_EVTqbDZHySRgvUzWWcl9XMCaEn1_W-Zl8_GKfMs0sqyc88wgbi9RcjZG-6pzAOYWU6XA",
                },
                discount=None,
            ),
            meta=dict(request_id="0f7e095c-b6b9-49e8-bc43-7037aa40e91d"),
        )

        assert (
            deepdiff.DeepDiff(
                subscription,
                expected_subscription,
                ignore_order=True,
            )
            == {}
        )

    @pytest.mark.vcr
    def test_list_subscriptions(self):
        subscriptions = self.client.list_subscriptions(
            query_params=SubscriptionQueryParams(
                status="active",
                customer_id="ctm_01h7mrr5j8rnawwzh9nschgp1v",
            )
        )
        expected_subscriptions = SubscriptionsResponse(
            data=[
                Subscription(
                    id="sub_01h7n3a88jwktex2tfjzahmn57",
                    status="active",
                    customer_id="ctm_01h7mrr5j8rnawwzh9nschgp1v",
                    address_id="add_01h7mrzwtwthvqqy7vq90f0kd7",
                    business_id=None,
                    currency_code="USD",
                    created_at="2023-08-12T14:44:57.746086Z",
                    updated_at="2023-08-12T14:44:57.746086Z",
                    started_at="2023-08-12T14:44:57.746081Z",
                    first_billed_at="2023-08-12T14:44:57.746081Z",
                    next_billed_at="2023-09-12T14:44:57.746081Z",
                    paused_at=None,
                    canceled_at=None,
                    collection_mode="manual",
                    billing_details=dict(
                        enable_checkout=True,
                        purchase_order_number="",
                        additional_information="",
                        payment_terms=dict(frequency=2, interval="week"),
                    ),
                    current_billing_period=dict(
                        starts_at="2023-08-12T14:44:57.746081Z",
                        ends_at="2023-09-12T14:44:57.746081Z",
                    ),
                    billing_cycle=dict(frequency=1, interval="month"),
                    scheduled_change=None,
                    items=[
                        {
                            "status": "active",
                            "quantity": 1,
                            "recurring": True,
                            "created_at": "2023-08-12T14:44:57.746087Z",
                            "updated_at": "2023-08-12T14:44:57.746087Z",
                            "previously_billed_at": "2023-08-12T14:44:57.746081Z",
                            "next_billed_at": "2023-09-12T14:44:57.746081Z",
                            "trial_dates": None,
                            "price": {
                                "id": "pri_01h7mrnc315chey77qhrd32vfs",
                                "product_id": "pro_01h7mrm9f0xvrvvwvkg1b7q8e3",
                                "description": "asd",
                                "tax_mode": "account_setting",
                                "billing_cycle": {"frequency": 1, "interval": "month"},
                                "trial_period": None,
                                "unit_price": {
                                    "amount": "1270",
                                    "currency_code": "USD",
                                },
                            },
                        },
                    ],
                    custom_data=dict(user_id="123"),
                    management_urls={
                        "update_payment_method": None,
                        "cancel": "https://sandbox-buyer-portal.paddle.com/subscriptions/sub_01h7n3a88jwktex2tfjzahmn57/cancel?token=pga_eyJhbGciOiJSUzI1NiIsImtpZCI6IjUwMWI4NGRhNWExYmIyODU2NDcyM2EzNDFkZGY5NTcyZDQwNDAwNDI4OTg3NzQyNjgzZWUyOWYyYTdmYjc0NDkiLCJ0eXAiOiJKV1QifQ.eyJpZCI6InBnYV8wMWg5Zm40M3c4ano2NWI2Mzk4Y3piNHRyNyIsInNlbGxlci1pZCI6Ijg5MzkiLCJ0eXBlIjoic3RhbmRhcmQiLCJ2ZXJzaW9uIjoiMSIsInVzYWdlIjoibWFuYWdlbWVudF91cmwiLCJzY29wZSI6ImN1c3RvbWVyLnN1YnNjcmlwdGlvbi1wYXltZW50LnVwZGF0ZSBjdXN0b21lci5zdWJzY3JpcHRpb24tcGF5bWVudC5yZWFkIGN1c3RvbWVyLnN1YnNjcmlwdGlvbi1jYW5jZWwuY3JlYXRlIGN1c3RvbWVyLnN1YnNjcmlwdGlvbi5yZWFkIiwiaXNzIjoiZ3Vlc3RhY2Nlc3Mtc2VydmljZSIsInN1YiI6ImN0bV8wMWg3bXJyNWo4cm5hd3d6aDluc2NoZ3AxdiIsImlhdCI6MTY5MzgxNjMyOCwiZXhwIjoxNzI1NDM4NzI4fQ.FoEUlAbdo8PRhmDXkqHa0GIpRheyfk7m8rSD4ZzXlggzdLU7HXtIiJz68YYfGFAE_xwNRVFL0_DjqIrhAtQo2NTh858pwJ0z32jWA0nA6AOlo6XYiA7LQqNrR05Y6KNGBUvoB2eJMtC9hAVySzA7-OynDXK4-M4cdK7KJ9Wx6os1RQpUlDbQaSoW7za2ZVKYs7NKlcgx6P9xV9v9cIEJ9lVRlSbf1MP5Laaf2RWXEIagVLbHW0Cb9fOwRAOdI_bkMXCKrd5enxdX0gQf6ncf-rjR9iUSd3owaPwoSC1N4_Uxdj-6GXVujegegcbC71u4qkh1qiel7-zfPQkSpi5X-g",
                    },
                    discount=None,
                )
            ],
            meta=dict(
                request_id="f9e7978a-8623-43ff-873f-8462ad9c29a0",
                pagination=dict(
                    per_page=50,
                    next="https://sandbox-api.paddle.com/subscriptions?after=sub_01h7n3a88jwktex2tfjzahmn57&customer_id=ctm_01h7mrr5j8rnawwzh9nschgp1v&status=active",
                    has_more=False,
                    estimated_total=1,
                ),
            ),
        )

        assert (
            deepdiff.DeepDiff(
                subscriptions,
                expected_subscriptions,
                ignore_order=True,
            )
            == {}
        )

    @pytest.mark.vcr
    def test_preview_update_subscription(self):
        subscription = self.client.preview_update_subscription(
            subscription_id="sub_01h7n3a88jwktex2tfjzahmn57",
            data=SubscriptionRequest(
                items=[
                    {"price_id": "pri_01h7mrnc315chey77qhrd32vfs", "quantity": 2},
                ],
                proration_billing_mode="prorated_immediately",
            ),
        )
        expected_subscription = SubscriptionResponse(
            data=Subscription(
                status="active",
                customer_id="ctm_01h7mrr5j8rnawwzh9nschgp1v",
                address_id="add_01h7mrzwtwthvqqy7vq90f0kd7",
                business_id=None,
                currency_code="USD",
                created_at="2023-08-12T14:44:57.746086Z",
                updated_at="2023-09-04T08:44:52.9Z",
                started_at="2023-08-12T14:44:57.746081Z",
                first_billed_at="2023-08-12T14:44:57.746081Z",
                next_billed_at="2023-09-12T14:44:57.746081Z",
                paused_at=None,
                canceled_at=None,
                collection_mode="manual",
                billing_details=dict(
                    enable_checkout=True,
                    purchase_order_number="",
                    additional_information="",
                    payment_terms=dict(frequency=2, interval="week"),
                ),
                current_billing_period=dict(
                    starts_at="2023-08-12T14:44:57.746081Z",
                    ends_at="2023-09-12T14:44:57.746081Z",
                ),
                billing_cycle=dict(frequency=1, interval="month"),
                recurring_transaction_details=dict(
                    tax_rates_used=[
                        {
                            "tax_rate": "0.27",
                            "totals": {
                                "subtotal": "2000",
                                "discount": "0",
                                "tax": "540",
                                "total": "2540",
                            },
                        }
                    ],
                    totals={
                        "subtotal": "2000",
                        "tax": "540",
                        "discount": "0",
                        "total": "2540",
                        "fee": None,
                        "credit": "0",
                        "balance": "2540",
                        "grand_total": "2540",
                        "earnings": None,
                        "currency_code": "USD",
                        "exchange_rate": "1",
                    },
                    line_items=[
                        {
                            "price_id": "pri_01h7mrnc315chey77qhrd32vfs",
                            "quantity": 2,
                            "totals": {
                                "subtotal": "2000",
                                "tax": "540",
                                "discount": "0",
                                "total": "2540",
                            },
                            "product": {
                                "id": "pro_01h7mrm9f0xvrvvwvkg1b7q8e3",
                                "name": "Sample new product",
                                "description": "",
                                "tax_category": "standard",
                                "image_url": "",
                                "status": "active",
                            },
                            "tax_rate": "0.27",
                            "unit_totals": {
                                "subtotal": "1000",
                                "discount": "0",
                                "tax": "270",
                                "total": "1270",
                            },
                        }
                    ],
                ),
                next_transaction=Transaction(
                    billing_period=dict(
                        starts_at="2023-09-12T14:44:57.746081Z",
                        ends_at="2023-10-12T14:44:57.746081Z",
                    ),
                    details=dict(
                        tax_rates_used=[
                            {
                                "tax_rate": "0.27",
                                "totals": {
                                    "subtotal": "2000",
                                    "discount": "0",
                                    "tax": "540",
                                    "total": "2540",
                                },
                            }
                        ],
                        totals={
                            "subtotal": "2000",
                            "tax": "540",
                            "discount": "0",
                            "total": "2540",
                            "fee": None,
                            "credit": "0",
                            "balance": "2540",
                            "grand_total": "2540",
                            "earnings": None,
                            "currency_code": "USD",
                            "exchange_rate": "1",
                        },
                        line_items=[
                            {
                                "price_id": "pri_01h7mrnc315chey77qhrd32vfs",
                                "quantity": 2,
                                "totals": {
                                    "subtotal": "2000",
                                    "tax": "540",
                                    "discount": "0",
                                    "total": "2540",
                                },
                                "product": {
                                    "id": "pro_01h7mrm9f0xvrvvwvkg1b7q8e3",
                                    "name": "Sample new product",
                                    "description": "",
                                    "tax_category": "standard",
                                    "image_url": "",
                                    "status": "active",
                                },
                                "tax_rate": "0.27",
                                "unit_totals": {
                                    "subtotal": "1000",
                                    "discount": "0",
                                    "tax": "270",
                                    "total": "1270",
                                },
                            }
                        ],
                    ),
                    adjustments=[],
                ),
                immediate_transaction=Transaction(
                    billing_period=dict(
                        starts_at="2023-09-04T08:44:53.197Z",
                        ends_at="2023-09-12T14:44:57.746081Z",
                    ),
                    details={
                        "tax_rates_used": [
                            {
                                "tax_rate": "0.27",
                                "totals": {
                                    "subtotal": "532",
                                    "discount": "0",
                                    "tax": "144",
                                    "total": "676",
                                },
                            }
                        ],
                        "totals": {
                            "subtotal": "532",
                            "tax": "144",
                            "discount": "0",
                            "total": "676",
                            "fee": None,
                            "credit": "338",
                            "balance": "338",
                            "grand_total": "338",
                            "earnings": None,
                            "currency_code": "USD",
                            "exchange_rate": "1",
                        },
                        "line_items": [
                            {
                                "price_id": "pri_01h7mrnc315chey77qhrd32vfs",
                                "quantity": 2,
                                "totals": {
                                    "subtotal": "532",
                                    "tax": "144",
                                    "discount": "0",
                                    "total": "676",
                                },
                                "product": {
                                    "id": "pro_01h7mrm9f0xvrvvwvkg1b7q8e3",
                                    "name": "Sample new product",
                                    "description": "",
                                    "tax_category": "standard",
                                    "image_url": "",
                                    "status": "active",
                                },
                                "tax_rate": "0.27",
                                "unit_totals": {
                                    "subtotal": "266",
                                    "discount": "0",
                                    "tax": "72",
                                    "total": "338",
                                },
                                "proration": {
                                    "rate": "0.26613",
                                    "billing_period": {
                                        "starts_at": "2023-09-04T08:44:52.899Z",
                                        "ends_at": "2023-09-12T14:44:57.746081Z",
                                    },
                                },
                            }
                        ],
                    },
                    adjustments=[
                        {
                            "transaction_id": "txn_01h7n3a7g7h0qr49zt9ckgketd",
                            "items": [
                                {
                                    "item_id": "txnitm_01h7n3a7jefxzqhpaw6hdc523q",
                                    "type": "proration",
                                    "amount": "338",
                                    "proration": {
                                        "rate": "0.26613",
                                        "billing_period": {
                                            "starts_at": "2023-09-04T08:44:52.898Z",
                                            "ends_at": "2023-09-12T14:44:57.746081Z",
                                        },
                                    },
                                    "totals": {
                                        "subtotal": "266",
                                        "tax": "72",
                                        "total": "338",
                                    },
                                }
                            ],
                            "totals": {
                                "subtotal": "266",
                                "tax": "72",
                                "total": "338",
                                "fee": "12",
                                "earnings": "254",
                                "currency_code": "USD",
                            },
                        }
                    ],
                ),
                scheduled_change=None,
                items=[
                    {
                        "status": "active",
                        "quantity": 2,
                        "recurring": True,
                        "created_at": "2023-08-12T14:44:57.746087Z",
                        "updated_at": "2023-09-04T08:44:52.886Z",
                        "previously_billed_at": "2023-08-12T14:44:57.746081Z",
                        "next_billed_at": "2023-09-12T14:44:57.746081Z",
                        "trial_dates": None,
                        "price": {
                            "id": "pri_01h7mrnc315chey77qhrd32vfs",
                            "product_id": "pro_01h7mrm9f0xvrvvwvkg1b7q8e3",
                            "description": "asd",
                            "tax_mode": "account_setting",
                            "billing_cycle": {"frequency": 1, "interval": "month"},
                            "trial_period": None,
                            "unit_price": {"amount": "1270", "currency_code": "USD"},
                        },
                    }
                ],
                custom_data=dict(user_id="123"),
                management_urls={
                    "update_payment_method": None,
                    "cancel": "https://sandbox-buyer-portal.paddle.com/subscriptions/sub_01h7n3a88jwktex2tfjzahmn57/cancel?token=pga_eyJhbGciOiJSUzI1NiIsImtpZCI6IjUwMWI4NGRhNWExYmIyODU2NDcyM2EzNDFkZGY5NTcyZDQwNDAwNDI4OTg3NzQyNjgzZWUyOWYyYTdmYjc0NDkiLCJ0eXAiOiJKV1QifQ.eyJpZCI6InBnYV8wMWg5Zm52ZjI5ZTJyNmY0bjM0cjgxMGZ6cSIsInNlbGxlci1pZCI6Ijg5MzkiLCJ0eXBlIjoic3RhbmRhcmQiLCJ2ZXJzaW9uIjoiMSIsInVzYWdlIjoibWFuYWdlbWVudF91cmwiLCJzY29wZSI6ImN1c3RvbWVyLnN1YnNjcmlwdGlvbi1wYXltZW50LnVwZGF0ZSBjdXN0b21lci5zdWJzY3JpcHRpb24tcGF5bWVudC5yZWFkIGN1c3RvbWVyLnN1YnNjcmlwdGlvbi1jYW5jZWwuY3JlYXRlIGN1c3RvbWVyLnN1YnNjcmlwdGlvbi5yZWFkIiwiaXNzIjoiZ3Vlc3RhY2Nlc3Mtc2VydmljZSIsInN1YiI6ImN0bV8wMWg3bXJyNWo4cm5hd3d6aDluc2NoZ3AxdiIsImlhdCI6MTY5MzgxNzA5MywiZXhwIjoxNzI1NDM5NDkzfQ.gPlOSJDNyaGlasaUL9XZddFRefttT5A1I4GCximQvHyCNbbu6AdjkDhKPtmsUd_CLdtkzz44399PwUxrLX2_JwF1aRMvrPQGbku_DpAAhfsruKagdL4zn33n9wLFj0Ie75We_hnp87pBB8NnfWxOKBb_cVOJSqbNVMrvmkqrS6XzsDN-ovdcb6vY54FrCbnuA1ItBgTk-Fw-OsX-hFJ2rCmSKyyHKClFUgvkMfbAL5_SsRcntY5gkSj-NN1ChmfiXsqZ6jZiun475tORQSc_bm9WU03ntjB8riXkVUs9R3VF1APZL8Y9OpldImXfnSq4MSKDabsqQ-sapptlM1Px1Q",
                },
                discount=None,
                update_summary=dict(
                    credit=dict(amount="338", currency_code="USD"),
                    charge=dict(amount="676", currency_code="USD"),
                    result=dict(action="charge", amount="338", currency_code="USD"),
                ),
            ),
            meta=dict(request_id="a21f92c6-e1a7-49d2-b32f-9fc4d445b865"),
        )

        assert (
            deepdiff.DeepDiff(
                subscription,
                expected_subscription,
                ignore_order=True,
            )
            == {}
        )

        assert isinstance(subscription.data, Subscription)
        assert isinstance(subscription.data.next_transaction, Transaction)
        assert isinstance(subscription.data.immediate_transaction, Transaction)

    @pytest.mark.vcr
    def test_update_subscription(self):
        subscription = self.client.update_subscription(
            subscription_id="sub_01h7n3a88jwktex2tfjzahmn57",
            data=SubscriptionRequest(
                items=[
                    {"price_id": "pri_01h7mrnc315chey77qhrd32vfs", "quantity": 2},
                ],
                proration_billing_mode="prorated_next_billing_period",
            ),
        )
        expected_subscription = SubscriptionResponse(
            data=Subscription(
                id="sub_01h7n3a88jwktex2tfjzahmn57",
                status="active",
                customer_id="ctm_01h7mrr5j8rnawwzh9nschgp1v",
                address_id="add_01h7mrzwtwthvqqy7vq90f0kd7",
                business_id=None,
                currency_code="USD",
                created_at="2023-08-12T14:44:57.746086Z",
                updated_at="2023-09-04T09:11:33.105Z",
                started_at="2023-08-12T14:44:57.746081Z",
                first_billed_at="2023-08-12T14:44:57.746081Z",
                next_billed_at="2023-09-12T14:44:57.746081Z",
                paused_at=None,
                canceled_at=None,
                collection_mode="manual",
                billing_details=dict(
                    enable_checkout=True,
                    purchase_order_number="",
                    additional_information="",
                    payment_terms=dict(frequency=2, interval="week"),
                ),
                current_billing_period=dict(
                    starts_at="2023-08-12T14:44:57.746081Z",
                    ends_at="2023-09-12T14:44:57.746081Z",
                ),
                billing_cycle=dict(frequency=1, interval="month"),
                recurring_transaction_details=None,
                next_transaction=None,
                immediate_transaction=None,
                scheduled_change=None,
                items=[
                    {
                        "status": "active",
                        "quantity": 2,
                        "recurring": True,
                        "created_at": "2023-08-12T14:44:57.746087Z",
                        "updated_at": "2023-09-04T09:11:33.096Z",
                        "previously_billed_at": "2023-08-12T14:44:57.746081Z",
                        "next_billed_at": "2023-09-12T14:44:57.746081Z",
                        "trial_dates": None,
                        "price": {
                            "id": "pri_01h7mrnc315chey77qhrd32vfs",
                            "product_id": "pro_01h7mrm9f0xvrvvwvkg1b7q8e3",
                            "description": "asd",
                            "tax_mode": "account_setting",
                            "billing_cycle": {"frequency": 1, "interval": "month"},
                            "trial_period": None,
                            "unit_price": {"amount": "1270", "currency_code": "USD"},
                        },
                    }
                ],
                custom_data=dict(user_id="123"),
                management_urls={
                    "update_payment_method": None,
                    "cancel": "https://sandbox-buyer-portal.paddle.com/subscriptions/sub_01h7n3a88jwktex2tfjzahmn57/cancel?token=pga_eyJhbGciOiJSUzI1NiIsImtpZCI6IjUwMWI4NGRhNWExYmIyODU2NDcyM2EzNDFkZGY5NTcyZDQwNDAwNDI4OTg3NzQyNjgzZWUyOWYyYTdmYjc0NDkiLCJ0eXAiOiJKV1QifQ.eyJpZCI6InBnYV8wMWg5ZnFjOWZ2dHl6OTI2eGdiYWNwODY2cyIsInNlbGxlci1pZCI6Ijg5MzkiLCJ0eXBlIjoic3RhbmRhcmQiLCJ2ZXJzaW9uIjoiMSIsInVzYWdlIjoibWFuYWdlbWVudF91cmwiLCJzY29wZSI6ImN1c3RvbWVyLnN1YnNjcmlwdGlvbi1wYXltZW50LnVwZGF0ZSBjdXN0b21lci5zdWJzY3JpcHRpb24tcGF5bWVudC5yZWFkIGN1c3RvbWVyLnN1YnNjcmlwdGlvbi1jYW5jZWwuY3JlYXRlIGN1c3RvbWVyLnN1YnNjcmlwdGlvbi5yZWFkIiwiaXNzIjoiZ3Vlc3RhY2Nlc3Mtc2VydmljZSIsInN1YiI6ImN0bV8wMWg3bXJyNWo4cm5hd3d6aDluc2NoZ3AxdiIsImlhdCI6MTY5MzgxODY5MywiZXhwIjoxNzI1NDQxMDkzfQ.GGulLq0v9PfluJv1U4BSTVemQ__GimrAZ1mO7KwJpYFIx_KBrtQjM_-jQvbnx933Q9jfRUPV3v6o_XITDtj8Zvntm6I2hKLErEUlyxW9y_SZurJpTtgvdtYfnw3WDPo5pNa4eL2X4hu92PQSQJbS8iN3C40siKa4NciniUwbgUgWsSjqLee1VIefrXDI1FbGSTtDNUz-Sp39DHgNTjUkxz-L_WUr9K4m2x6-NaA6VNW7zArAWzY4s_LBK-Woc8IV-ygRGUlXrg3qJTE9PeFS-nPxXyXZ-BdmIS4Sy0YwKsgdAF2iH-kgP4S-xalJYNs6uPEVxC2i3Y9fkqhqeOe3qg",
                },
                discount=None,
            ),
            meta=dict(request_id="50006f21-6095-4a04-ad34-ed87f437c78f"),
        )

        assert (
            deepdiff.DeepDiff(
                subscription,
                expected_subscription,
                ignore_order=True,
            )
            == {}
        )

    @pytest.mark.vcr
    def test_get_transaction_to_update_payment_method(self):
        transaction = self.client.get_transaction_to_update_payment_method(
            subscription_id="sub_01h9fs0mgwkhtdan4qd4r7qq77",
        )
        expected_transaction = TransactionResponse(
            data=Transaction(
                items=[
                    {
                        "price": {
                            "id": "pri_01h7mrnc315chey77qhrd32vfs",
                            "description": "asd",
                            "product_id": "pro_01h7mrm9f0xvrvvwvkg1b7q8e3",
                            "billing_cycle": {"interval": "month", "frequency": 1},
                            "trial_period": None,
                            "tax_mode": "account_setting",
                            "unit_price": {"amount": "1000", "currency_code": "USD"},
                            "unit_price_overrides": [],
                            "quantity": {"minimum": 1, "maximum": 100},
                            "status": "active",
                        },
                        "quantity": 1,
                        "proration": {
                            "rate": "0",
                            "billing_period": {
                                "starts_at": "2023-09-04T09:40:06.415402Z",
                                "ends_at": "2023-10-04T09:40:06.415402Z",
                            },
                        },
                    }
                ],
                status="ready",
                customer_id="ctm_01h9fryr8y9k8r4k0fjgkhem6p",
                address_id="add_01h9fryr9ftp2er4g1sxjhqg8w",
                business_id=None,
                discount_id=None,
                custom_data=None,
                collection_mode="automatic",
                billing_details=None,
                billing_period=BillingPeriod(
                    ends_at="2023-09-04T09:40:06.415402Z",
                    starts_at="2023-09-04T09:40:06.415402Z",
                ),
                currency_code="USD",
                customer_ip_address=None,
                ignore_trials=None,
                address=Address(
                    description="",
                    first_line="",
                    second_line="",
                    city="",
                    postal_code="",
                    region="",
                    country_code="HU",
                    status="active",
                    id="add_01h9fryr9ftp2er4g1sxjhqg8w",
                    created_at=None,
                    updated_at=None,
                    is_sanctioned=False,
                    suitable_for=["automatic"],
                ),
                id="txn_01h9fs2d1n49jdh2we7aqb08m0",
                customer=Customer(
                    email="asd1@asd.com",
                    name="",
                    locale="en",
                    id="ctm_01h9fryr8y9k8r4k0fjgkhem6p",
                    marketing_consent=True,
                    created_at=None,
                    updated_at=None,
                    imported_at=None,
                    source=None,
                    status="active",
                    is_sanctioned=False,
                    tax_exemptions=[],
                    suitable_for=["automatic"],
                ),
                business=None,
                discount=None,
                seller=None,
                adjustments_totals=None,
                origin="subscription_payment_method_change",
                subscription_id="sub_01h9fs0mgwkhtdan4qd4r7qq77",
                invoice_id=None,
                invoice_number=None,
                created_at="2023-09-04T09:41:06.283577437Z",
                updated_at="2023-09-04T09:41:06.283577437Z",
                billed_at=None,
                details=TransactionDetails(
                    tax_rates_used=[
                        TaxRatesUsed(
                            tax_rate="0.27",
                            totals=TaxRatesTotals(
                                subtotal="0", discount="0", tax="0", total="0"
                            ),
                        )
                    ],
                    totals=Totals(
                        subtotal="0",
                        discount="0",
                        tax="0",
                        total="0",
                        credit="0",
                        balance="0",
                        grand_total="0",
                        fee=None,
                        earnings=None,
                        currency_code="USD",
                        exchange_rate="1",
                    ),
                    adjusted_totals=AdjustedTotals(
                        subtotal="0",
                        tax="0",
                        total="0",
                        grand_total="0",
                        fee="0",
                        earnings="0",
                        currency_code="USD",
                    ),
                    payout_totals=None,
                    adjusted_payout_totals=None,
                    line_items=[
                        LineItem(
                            id="txnitm_01h9fs2d32f35beymbjzs776aw",
                            price_id="pri_01h7mrnc315chey77qhrd32vfs",
                            quantity=1,
                            proration=LineItemProration(
                                rate="0",
                                billing_period=BillingPeriod(
                                    ends_at="2023-10-04T09:40:06.415402Z",
                                    starts_at="2023-09-04T09:40:06.415402Z",
                                ),
                            ),
                            tax_rate="0.27",
                            unit_totals=LineItemUnitTotals(
                                subtotal="0", discount="0", tax="0", total="0"
                            ),
                            totals=LineItemTotals(
                                subtotal="0", discount="0", tax="0", total="0"
                            ),
                            product=Product(
                                name="Sample new product",
                                tax_category="standard",
                                description="",
                                image_url="",
                                custom_data=None,
                                status="active",
                                id="pro_01h7mrm9f0xvrvvwvkg1b7q8e3",
                                created_at=None,
                                prices=None,
                            ),
                        )
                    ],
                ),
                payments=[],
                checkout={
                    "url": "https://webstormit.com?_ptxn=txn_01h9fs2d1n49jdh2we7aqb08m0"
                },
                ledger_id=41846,
                tax_details={"entity": "GB", "registration_number": "EU372017215"},
            ),
            meta=dict(request_id="600d122f-212a-4136-81ef-759d3d367a0d"),
        )

        assert (
            deepdiff.DeepDiff(
                transaction,
                expected_transaction,
                ignore_order=True,
            )
            == {}
        )
        assert isinstance(transaction.data, Transaction)
        assert isinstance(transaction.data.details, TransactionDetails)
        assert isinstance(transaction.data.details.line_items[0], LineItem)
        assert isinstance(transaction.data.details.line_items[0].product, Product)
        assert isinstance(
            transaction.data.details.line_items[0].proration, LineItemProration
        )
        assert isinstance(
            transaction.data.details.line_items[0].unit_totals, LineItemUnitTotals
        )
        assert isinstance(transaction.data.details.line_items[0].totals, LineItemTotals)
        assert isinstance(transaction.data.details.totals, Totals)
        assert isinstance(transaction.data.details.adjusted_totals, AdjustedTotals)

    @pytest.mark.vcr
    def test_preview_one_time_charge(self):
        subscription = self.client.preview_one_time_charge(
            subscription_id="sub_01h9fs0mgwkhtdan4qd4r7qq77",
            data=SubscriptionRequest(
                items=[
                    {"price_id": "pri_01h9fwyrg7wtge506jpqjdfekr", "quantity": 1},
                ],
                effective_from="immediately",
            ),
        )
        expected_subscription = SubscriptionResponse(
            data=Subscription(
                status="active",
                customer_id="ctm_01h9fryr8y9k8r4k0fjgkhem6p",
                address_id="add_01h9fryr9ftp2er4g1sxjhqg8w",
                business_id=None,
                currency_code="USD",
                created_at="2023-09-04T09:40:08.348Z",
                updated_at="2023-09-04T10:49:22.612Z",
                started_at="2023-09-04T09:40:06.415402Z",
                first_billed_at="2023-09-04T09:40:06.415402Z",
                next_billed_at="2023-10-04T09:40:06.415402Z",
                paused_at=None,
                canceled_at=None,
                collection_mode="automatic",
                billing_details=None,
                current_billing_period=BillingPeriod(
                    ends_at="2023-10-04T09:40:06.415402Z",
                    starts_at="2023-09-04T09:40:06.415402Z",
                ),
                billing_cycle=BillingCycle(interval="month", frequency=1),
                recurring_transaction_details={
                    "tax_rates_used": [
                        {
                            "tax_rate": "0.27",
                            "totals": {
                                "subtotal": "1000",
                                "discount": "0",
                                "tax": "270",
                                "total": "1270",
                            },
                        }
                    ],
                    "totals": {
                        "subtotal": "1000",
                        "tax": "270",
                        "discount": "0",
                        "total": "1270",
                        "fee": None,
                        "credit": "0",
                        "balance": "1270",
                        "grand_total": "1270",
                        "earnings": None,
                        "currency_code": "USD",
                        "exchange_rate": "1",
                    },
                    "line_items": [
                        {
                            "price_id": "pri_01h7mrnc315chey77qhrd32vfs",
                            "quantity": 1,
                            "totals": {
                                "subtotal": "1000",
                                "tax": "270",
                                "discount": "0",
                                "total": "1270",
                            },
                            "product": {
                                "id": "pro_01h7mrm9f0xvrvvwvkg1b7q8e3",
                                "name": "Sample new product",
                                "description": "",
                                "tax_category": "standard",
                                "image_url": "",
                                "status": "active",
                            },
                            "tax_rate": "0.27",
                            "unit_totals": {
                                "subtotal": "1000",
                                "discount": "0",
                                "tax": "270",
                                "total": "1270",
                            },
                        }
                    ],
                },
                scheduled_change=None,
                items=[
                    Item(
                        price=Price(
                            description="asd",
                            product_id="pro_01h7mrm9f0xvrvvwvkg1b7q8e3",
                            billing_cycle=BillingCycle(interval="month", frequency=1),
                            trial_period=None,
                            tax_mode="account_setting",
                            unit_price_overrides=None,
                            quantity=None,
                            custom_data=None,
                            id="pri_01h7mrnc315chey77qhrd32vfs",
                            unit_price=UnitPrice(amount="1270", currency_code="USD"),
                            status=None,
                        ),
                        price_id=None,
                        status="active",
                        quantity=1,
                        recurring=True,
                        created_at="2023-09-04T09:40:08.348Z",
                        updated_at="2023-09-04T09:40:08.348Z",
                        next_billed_at="2023-10-04T09:40:06.415402Z",
                        previously_billed_at="2023-09-04T09:40:06.415402Z",
                        trial_dates=None,
                    )
                ],
                custom_data=None,
                management_urls={
                    "update_payment_method": "https://sandbox-buyer-portal.paddle.com/subscriptions/sub_01h9fs0mgwkhtdan4qd4r7qq77/update-payment-method?token=pga_eyJhbGciOiJSUzI1NiIsImtpZCI6IjUwMWI4NGRhNWExYmIyODU2NDcyM2EzNDFkZGY5NTcyZDQwNDAwNDI4OTg3NzQyNjgzZWUyOWYyYTdmYjc0NDkiLCJ0eXAiOiJKV1QifQ.eyJpZCI6InBnYV8wMWg5Znd6ZHM0c3p4cTd2YTdxd2djc215YyIsInNlbGxlci1pZCI6Ijg5MzkiLCJ0eXBlIjoic3RhbmRhcmQiLCJ2ZXJzaW9uIjoiMSIsInVzYWdlIjoibWFuYWdlbWVudF91cmwiLCJzY29wZSI6ImN1c3RvbWVyLnN1YnNjcmlwdGlvbi1wYXltZW50LnVwZGF0ZSBjdXN0b21lci5zdWJzY3JpcHRpb24tcGF5bWVudC5yZWFkIGN1c3RvbWVyLnN1YnNjcmlwdGlvbi1jYW5jZWwuY3JlYXRlIGN1c3RvbWVyLnN1YnNjcmlwdGlvbi5yZWFkIiwiaXNzIjoiZ3Vlc3RhY2Nlc3Mtc2VydmljZSIsInN1YiI6ImN0bV8wMWg5ZnJ5cjh5OWs4cjRrMGZqZ2toZW02cCIsImlhdCI6MTY5MzgyNDU2MiwiZXhwIjoxNzI1NDQ2OTYyfQ.X2OOsHYgnG_8iKUXD9XIs5ojoLrQp-5_uL9XSMPLKFMaWoWXcTRtqds7DWVPqXulH--6WkMh5N0mbkNILVFg6cRKbP-LQSTuB0ZoB7H77cFD94s1VzBU4t3rosxgkRB9zZRm6XLTAYlj_5glIpH45vUigu8r3VE1PeLp6w84Qe8iaHuV_xbEXVWw860j1Sd3ro2tKFnGC5bLN2KRRKTzmPVwiT0UVz7q78GQiZi9Rj84bFxGOmiB0fDGrDRfvpBeCWF4ww1SlxAZeefoZCtgtcF2uoJk35tGo2J5_aFNxUJtvouEnLUbbsCr24mHJtj-S_YuRvUQaLqy4XtowyiwMQ",
                    "cancel": "https://sandbox-buyer-portal.paddle.com/subscriptions/sub_01h9fs0mgwkhtdan4qd4r7qq77/cancel?token=pga_eyJhbGciOiJSUzI1NiIsImtpZCI6IjUwMWI4NGRhNWExYmIyODU2NDcyM2EzNDFkZGY5NTcyZDQwNDAwNDI4OTg3NzQyNjgzZWUyOWYyYTdmYjc0NDkiLCJ0eXAiOiJKV1QifQ.eyJpZCI6InBnYV8wMWg5Znd6ZHM0c3p4cTd2YTdxd2djc215YyIsInNlbGxlci1pZCI6Ijg5MzkiLCJ0eXBlIjoic3RhbmRhcmQiLCJ2ZXJzaW9uIjoiMSIsInVzYWdlIjoibWFuYWdlbWVudF91cmwiLCJzY29wZSI6ImN1c3RvbWVyLnN1YnNjcmlwdGlvbi1wYXltZW50LnVwZGF0ZSBjdXN0b21lci5zdWJzY3JpcHRpb24tcGF5bWVudC5yZWFkIGN1c3RvbWVyLnN1YnNjcmlwdGlvbi1jYW5jZWwuY3JlYXRlIGN1c3RvbWVyLnN1YnNjcmlwdGlvbi5yZWFkIiwiaXNzIjoiZ3Vlc3RhY2Nlc3Mtc2VydmljZSIsInN1YiI6ImN0bV8wMWg5ZnJ5cjh5OWs4cjRrMGZqZ2toZW02cCIsImlhdCI6MTY5MzgyNDU2MiwiZXhwIjoxNzI1NDQ2OTYyfQ.X2OOsHYgnG_8iKUXD9XIs5ojoLrQp-5_uL9XSMPLKFMaWoWXcTRtqds7DWVPqXulH--6WkMh5N0mbkNILVFg6cRKbP-LQSTuB0ZoB7H77cFD94s1VzBU4t3rosxgkRB9zZRm6XLTAYlj_5glIpH45vUigu8r3VE1PeLp6w84Qe8iaHuV_xbEXVWw860j1Sd3ro2tKFnGC5bLN2KRRKTzmPVwiT0UVz7q78GQiZi9Rj84bFxGOmiB0fDGrDRfvpBeCWF4ww1SlxAZeefoZCtgtcF2uoJk35tGo2J5_aFNxUJtvouEnLUbbsCr24mHJtj-S_YuRvUQaLqy4XtowyiwMQ",
                },
                id=None,
                next_transaction=Transaction(
                    items=None,
                    status=None,
                    customer_id=None,
                    address_id=None,
                    business_id=None,
                    discount_id=None,
                    custom_data=None,
                    collection_mode=None,
                    billing_details=None,
                    billing_period=BillingPeriod(
                        ends_at="2023-11-04T09:40:06.415402Z",
                        starts_at="2023-10-04T09:40:06.415402Z",
                    ),
                    currency_code=None,
                    customer_ip_address=None,
                    ignore_trials=None,
                    address=None,
                    id=None,
                    customer=None,
                    business=None,
                    discount=None,
                    seller=None,
                    adjustments_totals=None,
                    origin=None,
                    subscription_id=None,
                    invoice_id=None,
                    invoice_number=None,
                    created_at=None,
                    updated_at=None,
                    billed_at=None,
                    details=TransactionDetails(
                        tax_rates_used=[
                            TaxRatesUsed(
                                tax_rate="0.27",
                                totals=TaxRatesTotals(
                                    subtotal="1000",
                                    discount="0",
                                    tax="270",
                                    total="1270",
                                ),
                            )
                        ],
                        totals=Totals(
                            subtotal="1000",
                            discount="0",
                            tax="270",
                            total="1270",
                            credit="0",
                            balance="1270",
                            grand_total="1270",
                            fee=None,
                            earnings=None,
                            currency_code="USD",
                            exchange_rate="1",
                        ),
                        adjusted_totals=None,
                        payout_totals=None,
                        adjusted_payout_totals=None,
                        line_items=[
                            LineItem(
                                id=None,
                                price_id="pri_01h7mrnc315chey77qhrd32vfs",
                                quantity=1,
                                proration=None,
                                tax_rate="0.27",
                                unit_totals=LineItemUnitTotals(
                                    subtotal="1000",
                                    discount="0",
                                    tax="270",
                                    total="1270",
                                ),
                                totals=LineItemTotals(
                                    subtotal="1000",
                                    discount="0",
                                    tax="270",
                                    total="1270",
                                ),
                                product=Product(
                                    name="Sample new product",
                                    tax_category="standard",
                                    description="",
                                    image_url="",
                                    custom_data=None,
                                    status="active",
                                    id="pro_01h7mrm9f0xvrvvwvkg1b7q8e3",
                                    created_at=None,
                                    prices=None,
                                ),
                            )
                        ],
                    ),
                    payments=None,
                    checkout=None,
                    adjustments=[],
                ),
                immediate_transaction=Transaction(
                    items=None,
                    status=None,
                    customer_id=None,
                    address_id=None,
                    business_id=None,
                    discount_id=None,
                    custom_data=None,
                    collection_mode=None,
                    billing_details=None,
                    billing_period=BillingPeriod(
                        ends_at="2023-10-04T09:40:06.415402Z",
                        starts_at="2023-09-04T10:49:22.985Z",
                    ),
                    currency_code=None,
                    customer_ip_address=None,
                    ignore_trials=None,
                    address=None,
                    id=None,
                    customer=None,
                    business=None,
                    discount=None,
                    seller=None,
                    adjustments_totals=None,
                    origin=None,
                    subscription_id=None,
                    invoice_id=None,
                    invoice_number=None,
                    created_at=None,
                    updated_at=None,
                    billed_at=None,
                    details=TransactionDetails(
                        tax_rates_used=[
                            TaxRatesUsed(
                                tax_rate="0.27",
                                totals=TaxRatesTotals(
                                    subtotal="10000",
                                    discount="0",
                                    tax="2700",
                                    total="12700",
                                ),
                            )
                        ],
                        totals=Totals(
                            subtotal="10000",
                            discount="0",
                            tax="2700",
                            total="12700",
                            credit="0",
                            balance="12700",
                            grand_total="12700",
                            fee=None,
                            earnings=None,
                            currency_code="USD",
                            exchange_rate="1",
                        ),
                        adjusted_totals=None,
                        payout_totals=None,
                        adjusted_payout_totals=None,
                        line_items=[
                            LineItem(
                                id=None,
                                price_id="pri_01h9fwyrg7wtge506jpqjdfekr",
                                quantity=1,
                                proration=None,
                                tax_rate="0.27",
                                unit_totals=LineItemUnitTotals(
                                    subtotal="10000",
                                    discount="0",
                                    tax="2700",
                                    total="12700",
                                ),
                                totals=LineItemTotals(
                                    subtotal="10000",
                                    discount="0",
                                    tax="2700",
                                    total="12700",
                                ),
                                product=Product(
                                    name="Test Product New 2",
                                    tax_category="standard",
                                    description="Test Product Description",
                                    image_url="https://example.com/image.png",
                                    custom_data=None,
                                    status="active",
                                    id="pro_01h89b2j66qq82x6vn5d39c4av",
                                    created_at=None,
                                    prices=None,
                                ),
                            )
                        ],
                    ),
                    payments=None,
                    checkout=None,
                    adjustments=[],
                ),
                discount=None,
                update_summary={
                    "credit": {"amount": "0", "currency_code": "USD"},
                    "charge": {"amount": "12700", "currency_code": "USD"},
                    "result": {
                        "action": "charge",
                        "amount": "12700",
                        "currency_code": "USD",
                    },
                },
            ),
            meta=dict(request_id="93b5164c-50c9-41f6-99fe-9a17c88a71cf"),
        )

        assert (
            deepdiff.DeepDiff(
                subscription,
                expected_subscription,
                ignore_order=True,
            )
            == {}
        )

        assert isinstance(subscription.data, Subscription)
        assert isinstance(subscription.data.next_transaction, Transaction)
        assert isinstance(subscription.data.immediate_transaction, Transaction)

    @pytest.mark.vcr
    def test_create_one_time_charge(self):
        subscription = self.client.create_one_time_charge(
            subscription_id="sub_01h9fs0mgwkhtdan4qd4r7qq77",
            data=SubscriptionRequest(
                items=[
                    {"price_id": "pri_01h9fwyrg7wtge506jpqjdfekr", "quantity": 1},
                ],
                effective_from="immediately",
            ),
        )
        expected_subscription = SubscriptionResponse(
            data=Subscription(
                status="active",
                customer_id="ctm_01h9fryr8y9k8r4k0fjgkhem6p",
                address_id="add_01h9fryr9ftp2er4g1sxjhqg8w",
                business_id=None,
                currency_code="USD",
                created_at="2023-09-04T09:40:08.348Z",
                updated_at="2023-09-04T10:59:04.165Z",
                started_at="2023-09-04T09:40:06.415402Z",
                first_billed_at="2023-09-04T09:40:06.415402Z",
                next_billed_at="2023-10-04T09:40:06.415402Z",
                paused_at=None,
                canceled_at=None,
                collection_mode="automatic",
                billing_details=None,
                current_billing_period=BillingPeriod(
                    ends_at="2023-10-04T09:40:06.415402Z",
                    starts_at="2023-09-04T09:40:06.415402Z",
                ),
                billing_cycle=BillingCycle(interval="month", frequency=1),
                recurring_transaction_details=None,
                scheduled_change=None,
                items=[
                    Item(
                        price=Price(
                            description="asd",
                            product_id="pro_01h7mrm9f0xvrvvwvkg1b7q8e3",
                            billing_cycle=BillingCycle(interval="month", frequency=1),
                            trial_period=None,
                            tax_mode="account_setting",
                            unit_price_overrides=None,
                            quantity=None,
                            custom_data=None,
                            id="pri_01h7mrnc315chey77qhrd32vfs",
                            unit_price=UnitPrice(amount="1270", currency_code="USD"),
                            status=None,
                        ),
                        price_id=None,
                        status="active",
                        quantity=1,
                        recurring=True,
                        created_at="2023-09-04T09:40:08.348Z",
                        updated_at="2023-09-04T09:40:08.348Z",
                        next_billed_at="2023-10-04T09:40:06.415402Z",
                        previously_billed_at="2023-09-04T09:40:06.415402Z",
                        trial_dates=None,
                    )
                ],
                custom_data=None,
                management_urls={
                    "update_payment_method": "https://sandbox-buyer-portal.paddle.com/subscriptions/sub_01h9fs0mgwkhtdan4qd4r7qq77/update-payment-method?token=pga_eyJhbGciOiJSUzI1NiIsImtpZCI6IjUwMWI4NGRhNWExYmIyODU2NDcyM2EzNDFkZGY5NTcyZDQwNDAwNDI4OTg3NzQyNjgzZWUyOWYyYTdmYjc0NDkiLCJ0eXAiOiJKV1QifQ.eyJpZCI6InBnYV8wMWg5ZnhoODA4Ynp6eG5uem1reXY2cWNjMCIsInNlbGxlci1pZCI6Ijg5MzkiLCJ0eXBlIjoic3RhbmRhcmQiLCJ2ZXJzaW9uIjoiMSIsInVzYWdlIjoibWFuYWdlbWVudF91cmwiLCJzY29wZSI6ImN1c3RvbWVyLnN1YnNjcmlwdGlvbi1wYXltZW50LnVwZGF0ZSBjdXN0b21lci5zdWJzY3JpcHRpb24tcGF5bWVudC5yZWFkIGN1c3RvbWVyLnN1YnNjcmlwdGlvbi1jYW5jZWwuY3JlYXRlIGN1c3RvbWVyLnN1YnNjcmlwdGlvbi5yZWFkIiwiaXNzIjoiZ3Vlc3RhY2Nlc3Mtc2VydmljZSIsInN1YiI6ImN0bV8wMWg5ZnJ5cjh5OWs4cjRrMGZqZ2toZW02cCIsImlhdCI6MTY5MzgyNTE0NiwiZXhwIjoxNzI1NDQ3NTQ2fQ.AUOOoOyHcy48KOPJ94RB0sKWmd7O8gdxagtwQlNBMqyWOK7ugZrawDgTzY4x8EaR171Minx1o3IoV1E4zAdwMlmK0VKMx_1e1bsjUh1VA9P8T1T3OKiBCwW74j2WVj0utCSu2p9HhgKhTLa9FGhcJy-7SRghwiVwKMejydFLJTY40Uirihn3bC-DE-QRkWrj-gnUR8wl-0X8rKaTSG5LjESw7ZLT_3gIo-gjePgeNKe8Oe6TIsorKOo9DHxdpyzaOKbHRoU9C01u5KtBeyuWc5Zis-3m9opMGtOVKD3K_cnTjjAeegui3Av-2UZadc1nDWXyaC2B7q-D8ejiK5EbZw",
                    "cancel": "https://sandbox-buyer-portal.paddle.com/subscriptions/sub_01h9fs0mgwkhtdan4qd4r7qq77/cancel?token=pga_eyJhbGciOiJSUzI1NiIsImtpZCI6IjUwMWI4NGRhNWExYmIyODU2NDcyM2EzNDFkZGY5NTcyZDQwNDAwNDI4OTg3NzQyNjgzZWUyOWYyYTdmYjc0NDkiLCJ0eXAiOiJKV1QifQ.eyJpZCI6InBnYV8wMWg5ZnhoODA4Ynp6eG5uem1reXY2cWNjMCIsInNlbGxlci1pZCI6Ijg5MzkiLCJ0eXBlIjoic3RhbmRhcmQiLCJ2ZXJzaW9uIjoiMSIsInVzYWdlIjoibWFuYWdlbWVudF91cmwiLCJzY29wZSI6ImN1c3RvbWVyLnN1YnNjcmlwdGlvbi1wYXltZW50LnVwZGF0ZSBjdXN0b21lci5zdWJzY3JpcHRpb24tcGF5bWVudC5yZWFkIGN1c3RvbWVyLnN1YnNjcmlwdGlvbi1jYW5jZWwuY3JlYXRlIGN1c3RvbWVyLnN1YnNjcmlwdGlvbi5yZWFkIiwiaXNzIjoiZ3Vlc3RhY2Nlc3Mtc2VydmljZSIsInN1YiI6ImN0bV8wMWg5ZnJ5cjh5OWs4cjRrMGZqZ2toZW02cCIsImlhdCI6MTY5MzgyNTE0NiwiZXhwIjoxNzI1NDQ3NTQ2fQ.AUOOoOyHcy48KOPJ94RB0sKWmd7O8gdxagtwQlNBMqyWOK7ugZrawDgTzY4x8EaR171Minx1o3IoV1E4zAdwMlmK0VKMx_1e1bsjUh1VA9P8T1T3OKiBCwW74j2WVj0utCSu2p9HhgKhTLa9FGhcJy-7SRghwiVwKMejydFLJTY40Uirihn3bC-DE-QRkWrj-gnUR8wl-0X8rKaTSG5LjESw7ZLT_3gIo-gjePgeNKe8Oe6TIsorKOo9DHxdpyzaOKbHRoU9C01u5KtBeyuWc5Zis-3m9opMGtOVKD3K_cnTjjAeegui3Av-2UZadc1nDWXyaC2B7q-D8ejiK5EbZw",
                },
                id="sub_01h9fs0mgwkhtdan4qd4r7qq77",
                next_transaction=None,
                immediate_transaction=None,
                discount=None,
            ),
            meta=dict(request_id="e2c3502a-c73f-4d5a-a6dc-476a6ff0774e"),
        )

        assert (
            deepdiff.DeepDiff(
                subscription,
                expected_subscription,
                ignore_order=True,
            )
            == {}
        )

        assert isinstance(subscription.data, Subscription)

    @pytest.mark.vcr
    def test_pause_subscription(self):
        subscription = self.client.pause_subscription(
            subscription_id="sub_01h9fs0mgwkhtdan4qd4r7qq77",
            data=SubscriptionRequest(
                effective_from="next_billing_period",
            ),
        )
        expected_subscription = SubscriptionResponse(
            data=Subscription(
                status="active",
                customer_id="ctm_01h9fryr8y9k8r4k0fjgkhem6p",
                address_id="add_01h9fryr9ftp2er4g1sxjhqg8w",
                business_id=None,
                currency_code="USD",
                created_at="2023-09-04T09:40:08.348Z",
                updated_at="2023-09-04T11:10:45.159Z",
                started_at="2023-09-04T09:40:06.415402Z",
                first_billed_at="2023-09-04T09:40:06.415402Z",
                next_billed_at=None,
                paused_at=None,
                canceled_at=None,
                collection_mode="automatic",
                billing_details=None,
                current_billing_period=BillingPeriod(
                    ends_at="2023-10-04T09:40:06.415402Z",
                    starts_at="2023-09-04T09:40:06.415402Z",
                ),
                billing_cycle=BillingCycle(interval="month", frequency=1),
                recurring_transaction_details=None,
                scheduled_change=ScheduledChange(
                    action="pause",
                    effective_at="2023-10-04T09:40:06.415402Z",
                    resume_at=None,
                ),
                items=[
                    Item(
                        price=Price(
                            description="asd",
                            product_id="pro_01h7mrm9f0xvrvvwvkg1b7q8e3",
                            billing_cycle=BillingCycle(interval="month", frequency=1),
                            trial_period=None,
                            tax_mode="account_setting",
                            unit_price_overrides=None,
                            quantity=None,
                            custom_data=None,
                            id="pri_01h7mrnc315chey77qhrd32vfs",
                            unit_price=UnitPrice(amount="1270", currency_code="USD"),
                            status=None,
                        ),
                        price_id=None,
                        status="active",
                        quantity=1,
                        recurring=True,
                        created_at="2023-09-04T09:40:08.348Z",
                        updated_at="2023-09-04T09:40:08.348Z",
                        next_billed_at=None,
                        previously_billed_at="2023-09-04T09:40:06.415402Z",
                        trial_dates=None,
                    )
                ],
                custom_data=None,
                management_urls={
                    "update_payment_method": "https://sandbox-buyer-portal.paddle.com/subscriptions/sub_01h9fs0mgwkhtdan4qd4r7qq77/update-payment-method?token=pga_eyJhbGciOiJSUzI1NiIsImtpZCI6IjUwMWI4NGRhNWExYmIyODU2NDcyM2EzNDFkZGY5NTcyZDQwNDAwNDI4OTg3NzQyNjgzZWUyOWYyYTdmYjc0NDkiLCJ0eXAiOiJKV1QifQ.eyJpZCI6InBnYV8wMWg5Znk2aHhjZjdjZzdkNTExbXl3a2RybiIsInNlbGxlci1pZCI6Ijg5MzkiLCJ0eXBlIjoic3RhbmRhcmQiLCJ2ZXJzaW9uIjoiMSIsInVzYWdlIjoibWFuYWdlbWVudF91cmwiLCJzY29wZSI6ImN1c3RvbWVyLnN1YnNjcmlwdGlvbi1wYXltZW50LnVwZGF0ZSBjdXN0b21lci5zdWJzY3JpcHRpb24tcGF5bWVudC5yZWFkIGN1c3RvbWVyLnN1YnNjcmlwdGlvbi1jYW5jZWwuY3JlYXRlIGN1c3RvbWVyLnN1YnNjcmlwdGlvbi5yZWFkIiwiaXNzIjoiZ3Vlc3RhY2Nlc3Mtc2VydmljZSIsInN1YiI6ImN0bV8wMWg5ZnJ5cjh5OWs4cjRrMGZqZ2toZW02cCIsImlhdCI6MTY5MzgyNTg0NSwiZXhwIjoxNzI1NDQ4MjQ1fQ.ERuDWELZu8vlTtbwHsY7x6q1zHEZYUE7KrZKGsQ4yTFov9_Wk0IXd6uQ1mX6gtZxLeBdAsxEIhAg_id3VmQFUllp3giWSY7kDUYH5LhtyyStztpmBXIYtXoFJoEHxamXf4DJXU6AxaZiF-MXWOFNjpDT8PBs2glcSMGbVo9iJAxGcoFSJiQh0lyEipUItb7ZUONxktAwtnsaX5edX61rbx0Aj-oMO_0EI-g4ZUleYMRIWQSiv5_5wfbiZvNmFrGZSWBsYkYcwcOpxzMFkIEyI4KARFOQ1BhiCDD-EA2m51jslVZqPx3_YXMCEs1KBoNhUDE8oYlyQsv8HAWa3O-rAw",
                    "cancel": "https://sandbox-buyer-portal.paddle.com/subscriptions/sub_01h9fs0mgwkhtdan4qd4r7qq77/cancel?token=pga_eyJhbGciOiJSUzI1NiIsImtpZCI6IjUwMWI4NGRhNWExYmIyODU2NDcyM2EzNDFkZGY5NTcyZDQwNDAwNDI4OTg3NzQyNjgzZWUyOWYyYTdmYjc0NDkiLCJ0eXAiOiJKV1QifQ.eyJpZCI6InBnYV8wMWg5Znk2aHhjZjdjZzdkNTExbXl3a2RybiIsInNlbGxlci1pZCI6Ijg5MzkiLCJ0eXBlIjoic3RhbmRhcmQiLCJ2ZXJzaW9uIjoiMSIsInVzYWdlIjoibWFuYWdlbWVudF91cmwiLCJzY29wZSI6ImN1c3RvbWVyLnN1YnNjcmlwdGlvbi1wYXltZW50LnVwZGF0ZSBjdXN0b21lci5zdWJzY3JpcHRpb24tcGF5bWVudC5yZWFkIGN1c3RvbWVyLnN1YnNjcmlwdGlvbi1jYW5jZWwuY3JlYXRlIGN1c3RvbWVyLnN1YnNjcmlwdGlvbi5yZWFkIiwiaXNzIjoiZ3Vlc3RhY2Nlc3Mtc2VydmljZSIsInN1YiI6ImN0bV8wMWg5ZnJ5cjh5OWs4cjRrMGZqZ2toZW02cCIsImlhdCI6MTY5MzgyNTg0NSwiZXhwIjoxNzI1NDQ4MjQ1fQ.ERuDWELZu8vlTtbwHsY7x6q1zHEZYUE7KrZKGsQ4yTFov9_Wk0IXd6uQ1mX6gtZxLeBdAsxEIhAg_id3VmQFUllp3giWSY7kDUYH5LhtyyStztpmBXIYtXoFJoEHxamXf4DJXU6AxaZiF-MXWOFNjpDT8PBs2glcSMGbVo9iJAxGcoFSJiQh0lyEipUItb7ZUONxktAwtnsaX5edX61rbx0Aj-oMO_0EI-g4ZUleYMRIWQSiv5_5wfbiZvNmFrGZSWBsYkYcwcOpxzMFkIEyI4KARFOQ1BhiCDD-EA2m51jslVZqPx3_YXMCEs1KBoNhUDE8oYlyQsv8HAWa3O-rAw",
                },
                id="sub_01h9fs0mgwkhtdan4qd4r7qq77",
                next_transaction=None,
                immediate_transaction=None,
                discount=None,
            ),
            meta=dict(request_id="78e160f2-0448-4d4e-9784-bd30586719c1"),
        )

        assert (
            deepdiff.DeepDiff(
                subscription,
                expected_subscription,
                ignore_order=True,
            )
            == {}
        )

        assert isinstance(subscription.data, Subscription)
        assert isinstance(subscription.data.scheduled_change, ScheduledChange)

    # @pytest.mark.vcr
    # def test_resume_subscription(self):
    #     subscription = self.client.resume_subscription(
    #         subscription_id="sub_01h9fs0mgwkhtdan4qd4r7qq77",
    #         data=SubscriptionRequest(
    #             effective_from="next_billing_period",
    #         ),
    #     )
    #     print(subscription)
    #     # TODO: Finish this request. Blocking issue: Internal server error - waiting for Paddle to fix
    #
    #     assert False

    @pytest.mark.vcr
    def test_cancel_subscription(self):
        subscription = self.client.cancel_subscription(
            subscription_id="sub_01h9fja8n8w8f9he3gbgy518mt",
            data=SubscriptionRequest(
                effective_from="next_billing_period",
            ),
        )
        expected_subscription = SubscriptionResponse(
            data=Subscription(
                status="active",
                customer_id="ctm_01h8w66qa8djqjhmdkth2fnebk",
                address_id="add_01h9fj8v8ej6cqs7v9jrabrjp5",
                business_id="biz_01h8xg9dgqkehwp72x067vems9",
                currency_code="USD",
                created_at="2023-09-04T07:43:03.848Z",
                updated_at="2023-09-04T11:53:28.992Z",
                started_at="2023-09-04T07:43:03.848Z",
                first_billed_at="2023-09-04T07:43:03.848Z",
                next_billed_at=None,
                paused_at=None,
                canceled_at=None,
                collection_mode="manual",
                billing_details={
                    "enable_checkout": True,
                    "purchase_order_number": "",
                    "additional_information": "",
                    "payment_terms": {"frequency": 2, "interval": "week"},
                },
                current_billing_period=BillingPeriod(
                    ends_at="2023-10-04T07:43:03.848Z",
                    starts_at="2023-09-04T07:43:03.848Z",
                ),
                billing_cycle=BillingCycle(interval="month", frequency=1),
                recurring_transaction_details=None,
                scheduled_change=ScheduledChange(
                    action="cancel",
                    effective_at="2023-10-04T07:43:03.848Z",
                    resume_at=None,
                ),
                items=[
                    Item(
                        price=Price(
                            description="Test Price Description 2",
                            product_id="pro_01h81jnhdrz5wfde6cn8wg9y1y",
                            billing_cycle=BillingCycle(interval="month", frequency=1),
                            trial_period=None,
                            tax_mode="account_setting",
                            unit_price_overrides=None,
                            quantity=None,
                            custom_data=None,
                            id="pri_01h81k4xtxq5atfyjdfadsavd8",
                            unit_price=UnitPrice(amount="1525", currency_code="USD"),
                            status=None,
                        ),
                        price_id=None,
                        status="active",
                        quantity=1,
                        recurring=True,
                        created_at="2023-09-04T07:43:03.848Z",
                        updated_at="2023-09-04T07:43:03.848Z",
                        next_billed_at=None,
                        previously_billed_at="2023-09-04T07:43:03.848Z",
                        trial_dates=None,
                    )
                ],
                custom_data=None,
                management_urls={
                    "update_payment_method": None,
                    "cancel": "https://sandbox-buyer-portal.paddle.com/subscriptions/sub_01h9fja8n8w8f9he3gbgy518mt/cancel?token=pga_eyJhbGciOiJSUzI1NiIsImtpZCI6IjUwMWI4NGRhNWExYmIyODU2NDcyM2EzNDFkZGY5NTcyZDQwNDAwNDI4OTg3NzQyNjgzZWUyOWYyYTdmYjc0NDkiLCJ0eXAiOiJKV1QifQ.eyJpZCI6InBnYV8wMWg5ZzBtc240MWJ5YTh2cncyNDR0c25udCIsInNlbGxlci1pZCI6Ijg5MzkiLCJ0eXBlIjoic3RhbmRhcmQiLCJ2ZXJzaW9uIjoiMSIsInVzYWdlIjoibWFuYWdlbWVudF91cmwiLCJzY29wZSI6ImN1c3RvbWVyLnN1YnNjcmlwdGlvbi1wYXltZW50LnVwZGF0ZSBjdXN0b21lci5zdWJzY3JpcHRpb24tcGF5bWVudC5yZWFkIGN1c3RvbWVyLnN1YnNjcmlwdGlvbi1jYW5jZWwuY3JlYXRlIGN1c3RvbWVyLnN1YnNjcmlwdGlvbi5yZWFkIiwiaXNzIjoiZ3Vlc3RhY2Nlc3Mtc2VydmljZSIsInN1YiI6ImN0bV8wMWg4dzY2cWE4ZGpxamhtZGt0aDJmbmViayIsImlhdCI6MTY5MzgyODQwOCwiZXhwIjoxNzI1NDUwODA4fQ.pBHJqyYJJxWlsmXhVUIvn1PWFKWs4ylNHvDy5kKBBPK2FoAyf5erhlWUmSjfOlCP4PSsMOYHxpQ2Sv75ExfceLCcoCgp8GkrzCapPeVf-x74YVTvd_z_QCoerp6GkmoMAPe7UNsVzQTALLeBVeIGT_FJMsQP_4rsHCJLxAme7xwwNUaVrnQ4v-jO18MMa6yXinXyyV5WFlKbWfQjrfR-jCidt64JXTV_8SLRrHAqkw2e4Ejnj_LOi5PCY8Dc2caPNaQxX-mGb74nWQ28_UdK_SR5xBZt_--djCa4vUiQ5ZFMyzo_wPRk1SGDaRknODI5ILV2dCtctvYJbExe6TmeXQ",
                },
                id="sub_01h9fja8n8w8f9he3gbgy518mt",
                next_transaction=None,
                immediate_transaction=None,
                discount=None,
            ),
            meta=dict(request_id="60dd009b-c9b5-44f5-9daf-a8e665764599"),
        )

        assert (
            deepdiff.DeepDiff(
                subscription,
                expected_subscription,
                ignore_order=True,
            )
            == {}
        )

        assert isinstance(subscription.data, Subscription)
        assert isinstance(subscription.data.scheduled_change, ScheduledChange)
