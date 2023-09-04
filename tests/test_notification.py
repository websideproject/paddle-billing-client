import datetime
import os

import deepdiff
import pytest
from apiclient import HeaderAuthentication

from paddle_billing_client.models.common import BillingPeriod
from paddle_billing_client.models.notification import (
    Notification,
    NotificationPayload,
    NotificationReplay,
    NotificationReplayResponse,
    NotificationResponse,
    NotificationsResponse,
)
from paddle_billing_client.models.price import BillingCycle, Price, UnitPrice
from paddle_billing_client.models.product import Product
from paddle_billing_client.models.subscription import (
    Item,
    ScheduledChange,
    Subscription,
)
from paddle_billing_client.models.transaction import (
    AdjustedTotals,
    LineItem,
    LineItemTotals,
    LineItemUnitTotals,
    TaxRatesTotals,
    TaxRatesUsed,
    Totals,
    Transaction,
    TransactionDetails,
)


class TestNotification:
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
    def test_get_notification(self):
        notification = self.client.get_notification(
            notification_id="ntf_01h9g0mtsp2mae24351z8nfsg1"
        )
        expected_notification = NotificationResponse(
            data=Notification(
                id="ntf_01h9g0mtsp2mae24351z8nfsg1",
                type="subscription.updated",
                status="delivered",
                payload=NotificationPayload(
                    notification_id="ntf_01h9g0mtsp2mae24351z8nfsg1",
                    event_id="evt_01h9g0mtq3fkpsb6cdftgb0an0",
                    event_type="subscription.updated",
                    data=Subscription(
                        status="active",
                        customer_id="ctm_01h8w66qa8djqjhmdkth2fnebk",
                        address_id="add_01h9fj8v8ej6cqs7v9jrabrjp5",
                        business_id="biz_01h8xg9dgqkehwp72x067vems9",
                        currency_code="USD",
                        created_at=datetime.datetime(
                            2023, 9, 4, 7, 43, 3, 848000, tzinfo=datetime.timezone.utc
                        ),
                        updated_at=datetime.datetime(
                            2023, 9, 4, 11, 53, 28, 992000, tzinfo=datetime.timezone.utc
                        ),
                        started_at=datetime.datetime(
                            2023, 9, 4, 7, 43, 3, 848000, tzinfo=datetime.timezone.utc
                        ),
                        first_billed_at=datetime.datetime(
                            2023, 9, 4, 7, 43, 3, 848000, tzinfo=datetime.timezone.utc
                        ),
                        next_billed_at=None,
                        paused_at=None,
                        canceled_at=None,
                        collection_mode="manual",
                        billing_details={
                            "payment_terms": {"interval": "week", "frequency": 2},
                            "enable_checkout": True,
                            "purchase_order_number": None,
                            "additional_information": None,
                        },
                        current_billing_period=BillingPeriod(
                            ends_at="2023-10-04T07:43:03.848Z",
                            starts_at="2023-09-04T07:43:03.848Z",
                        ),
                        billing_cycle=BillingCycle(interval="month", frequency=1),
                        recurring_transaction_details=None,
                        scheduled_change=ScheduledChange(
                            action="cancel",
                            effective_at=datetime.datetime(
                                2023,
                                10,
                                4,
                                7,
                                43,
                                3,
                                848000,
                                tzinfo=datetime.timezone.utc,
                            ),
                            resume_at=None,
                        ),
                        items=[
                            Item(
                                price=Price(
                                    description="Test Price Description 2",
                                    product_id="pro_01h81jnhdrz5wfde6cn8wg9y1y",
                                    billing_cycle=BillingCycle(
                                        interval="month", frequency=1
                                    ),
                                    trial_period=None,
                                    tax_mode="account_setting",
                                    unit_price_overrides=None,
                                    quantity=None,
                                    custom_data=None,
                                    id="pri_01h81k4xtxq5atfyjdfadsavd8",
                                    unit_price=UnitPrice(
                                        amount="1525", currency_code="USD"
                                    ),
                                    status=None,
                                ),
                                price_id=None,
                                status="active",
                                quantity=1,
                                recurring=True,
                                created_at=datetime.datetime(
                                    2023,
                                    9,
                                    4,
                                    7,
                                    43,
                                    3,
                                    848000,
                                    tzinfo=datetime.timezone.utc,
                                ),
                                updated_at=datetime.datetime(
                                    2023,
                                    9,
                                    4,
                                    7,
                                    43,
                                    3,
                                    848000,
                                    tzinfo=datetime.timezone.utc,
                                ),
                                next_billed_at=None,
                                previously_billed_at=datetime.datetime(
                                    2023,
                                    9,
                                    4,
                                    7,
                                    43,
                                    3,
                                    848000,
                                    tzinfo=datetime.timezone.utc,
                                ),
                                trial_dates=None,
                            )
                        ],
                        custom_data=None,
                        management_urls=None,
                        id="sub_01h9fja8n8w8f9he3gbgy518mt",
                        next_transaction=None,
                        immediate_transaction=None,
                        discount=None,
                    ),
                    occurred_at=datetime.datetime(
                        2023, 9, 4, 11, 53, 30, 83681, tzinfo=datetime.timezone.utc
                    ),
                ),
                occurred_at=datetime.datetime(
                    2023, 9, 4, 11, 53, 30, 83681, tzinfo=datetime.timezone.utc
                ),
                delivered_at=datetime.datetime(
                    2023, 9, 4, 11, 53, 30, 467385, tzinfo=datetime.timezone.utc
                ),
                replayed_at=None,
                origin="event",
                last_attempt_at=datetime.datetime(
                    2023, 9, 4, 11, 53, 30, 205837, tzinfo=datetime.timezone.utc
                ),
                retry_at=None,
                times_attempted=1,
                notification_setting_id="ntfset_01h7mt960x2r58dp0wrevgzk41",
            ),
            meta=dict(request_id="ef69ce41-4f63-401f-8d2f-71541ecc5cdd"),
        )

        assert (
            deepdiff.DeepDiff(
                notification.dict(), expected_notification.dict(), ignore_order=True
            )
            == {}
        )

    @pytest.mark.vcr
    def test_list_notifications(self):
        notifications = self.client.list_notifications()
        expected_notifications = NotificationsResponse(
            data=[
                Notification(
                    id="ntf_01h9g0mtsp2mae24351z8nfsg1",
                    type="subscription.updated",
                    status="delivered",
                    payload=NotificationPayload(
                        notification_id="ntf_01h9g0mtsp2mae24351z8nfsg1",
                        event_id="evt_01h9g0mtq3fkpsb6cdftgb0an0",
                        event_type="subscription.updated",
                        data=Subscription(
                            status="active",
                            customer_id="ctm_01h8w66qa8djqjhmdkth2fnebk",
                            address_id="add_01h9fj8v8ej6cqs7v9jrabrjp5",
                            business_id="biz_01h8xg9dgqkehwp72x067vems9",
                            currency_code="USD",
                            created_at=datetime.datetime(
                                2023,
                                9,
                                4,
                                7,
                                43,
                                3,
                                848000,
                                tzinfo=datetime.timezone.utc,
                            ),
                            updated_at=datetime.datetime(
                                2023,
                                9,
                                4,
                                11,
                                53,
                                28,
                                992000,
                                tzinfo=datetime.timezone.utc,
                            ),
                            started_at=datetime.datetime(
                                2023,
                                9,
                                4,
                                7,
                                43,
                                3,
                                848000,
                                tzinfo=datetime.timezone.utc,
                            ),
                            first_billed_at=datetime.datetime(
                                2023,
                                9,
                                4,
                                7,
                                43,
                                3,
                                848000,
                                tzinfo=datetime.timezone.utc,
                            ),
                            next_billed_at=None,
                            paused_at=None,
                            canceled_at=None,
                            collection_mode="manual",
                            billing_details={
                                "payment_terms": {"interval": "week", "frequency": 2},
                                "enable_checkout": True,
                                "purchase_order_number": None,
                                "additional_information": None,
                            },
                            current_billing_period=BillingPeriod(
                                ends_at="2023-10-04T07:43:03.848Z",
                                starts_at="2023-09-04T07:43:03.848Z",
                            ),
                            billing_cycle=BillingCycle(interval="month", frequency=1),
                            recurring_transaction_details=None,
                            scheduled_change=ScheduledChange(
                                action="cancel",
                                effective_at=datetime.datetime(
                                    2023,
                                    10,
                                    4,
                                    7,
                                    43,
                                    3,
                                    848000,
                                    tzinfo=datetime.timezone.utc,
                                ),
                                resume_at=None,
                            ),
                            items=[
                                Item(
                                    price=Price(
                                        description="Test Price Description 2",
                                        product_id="pro_01h81jnhdrz5wfde6cn8wg9y1y",
                                        billing_cycle=BillingCycle(
                                            interval="month", frequency=1
                                        ),
                                        trial_period=None,
                                        tax_mode="account_setting",
                                        unit_price_overrides=None,
                                        quantity=None,
                                        custom_data=None,
                                        id="pri_01h81k4xtxq5atfyjdfadsavd8",
                                        unit_price=UnitPrice(
                                            amount="1525", currency_code="USD"
                                        ),
                                        status=None,
                                    ),
                                    price_id=None,
                                    status="active",
                                    quantity=1,
                                    recurring=True,
                                    created_at=datetime.datetime(
                                        2023,
                                        9,
                                        4,
                                        7,
                                        43,
                                        3,
                                        848000,
                                        tzinfo=datetime.timezone.utc,
                                    ),
                                    updated_at=datetime.datetime(
                                        2023,
                                        9,
                                        4,
                                        7,
                                        43,
                                        3,
                                        848000,
                                        tzinfo=datetime.timezone.utc,
                                    ),
                                    next_billed_at=None,
                                    previously_billed_at=datetime.datetime(
                                        2023,
                                        9,
                                        4,
                                        7,
                                        43,
                                        3,
                                        848000,
                                        tzinfo=datetime.timezone.utc,
                                    ),
                                    trial_dates=None,
                                )
                            ],
                            custom_data=None,
                            management_urls=None,
                            id="sub_01h9fja8n8w8f9he3gbgy518mt",
                            next_transaction=None,
                            immediate_transaction=None,
                            discount=None,
                        ),
                        occurred_at=datetime.datetime(
                            2023, 9, 4, 11, 53, 30, 83681, tzinfo=datetime.timezone.utc
                        ),
                    ),
                    occurred_at=datetime.datetime(
                        2023, 9, 4, 11, 53, 30, 83681, tzinfo=datetime.timezone.utc
                    ),
                    delivered_at=datetime.datetime(
                        2023, 9, 4, 11, 53, 30, 467385, tzinfo=datetime.timezone.utc
                    ),
                    replayed_at=None,
                    origin="event",
                    last_attempt_at=datetime.datetime(
                        2023, 9, 4, 11, 53, 30, 205837, tzinfo=datetime.timezone.utc
                    ),
                    retry_at=None,
                    times_attempted=1,
                    notification_setting_id="ntfset_01h7mt960x2r58dp0wrevgzk41",
                ),
                Notification(
                    id="ntf_01h9fy6jw3dnqwzhsdwd1t3p4q",
                    type="subscription.updated",
                    status="delivered",
                    payload=NotificationPayload(
                        notification_id="ntf_01h9fy6jw3dnqwzhsdwd1t3p4q",
                        event_id="evt_01h9fy6js58ny2hg9e5ee0m7td",
                        event_type="subscription.updated",
                        data=Subscription(
                            status="active",
                            customer_id="ctm_01h9fryr8y9k8r4k0fjgkhem6p",
                            address_id="add_01h9fryr9ftp2er4g1sxjhqg8w",
                            business_id=None,
                            currency_code="USD",
                            created_at=datetime.datetime(
                                2023,
                                9,
                                4,
                                9,
                                40,
                                8,
                                348000,
                                tzinfo=datetime.timezone.utc,
                            ),
                            updated_at=datetime.datetime(
                                2023,
                                9,
                                4,
                                11,
                                10,
                                45,
                                159000,
                                tzinfo=datetime.timezone.utc,
                            ),
                            started_at=datetime.datetime(
                                2023,
                                9,
                                4,
                                9,
                                40,
                                6,
                                415402,
                                tzinfo=datetime.timezone.utc,
                            ),
                            first_billed_at=datetime.datetime(
                                2023,
                                9,
                                4,
                                9,
                                40,
                                6,
                                415402,
                                tzinfo=datetime.timezone.utc,
                            ),
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
                                effective_at=datetime.datetime(
                                    2023,
                                    10,
                                    4,
                                    9,
                                    40,
                                    6,
                                    415402,
                                    tzinfo=datetime.timezone.utc,
                                ),
                                resume_at=None,
                            ),
                            items=[
                                Item(
                                    price=Price(
                                        description="asd",
                                        product_id="pro_01h7mrm9f0xvrvvwvkg1b7q8e3",
                                        billing_cycle=BillingCycle(
                                            interval="month", frequency=1
                                        ),
                                        trial_period=None,
                                        tax_mode="account_setting",
                                        unit_price_overrides=None,
                                        quantity=None,
                                        custom_data=None,
                                        id="pri_01h7mrnc315chey77qhrd32vfs",
                                        unit_price=UnitPrice(
                                            amount="1270", currency_code="USD"
                                        ),
                                        status=None,
                                    ),
                                    price_id=None,
                                    status="active",
                                    quantity=1,
                                    recurring=True,
                                    created_at=datetime.datetime(
                                        2023,
                                        9,
                                        4,
                                        9,
                                        40,
                                        8,
                                        348000,
                                        tzinfo=datetime.timezone.utc,
                                    ),
                                    updated_at=datetime.datetime(
                                        2023,
                                        9,
                                        4,
                                        9,
                                        40,
                                        8,
                                        348000,
                                        tzinfo=datetime.timezone.utc,
                                    ),
                                    next_billed_at=None,
                                    previously_billed_at=datetime.datetime(
                                        2023,
                                        9,
                                        4,
                                        9,
                                        40,
                                        6,
                                        415402,
                                        tzinfo=datetime.timezone.utc,
                                    ),
                                    trial_dates=None,
                                )
                            ],
                            custom_data=None,
                            management_urls=None,
                            id="sub_01h9fs0mgwkhtdan4qd4r7qq77",
                            next_transaction=None,
                            immediate_transaction=None,
                            discount=None,
                        ),
                        occurred_at=datetime.datetime(
                            2023, 9, 4, 11, 10, 46, 53471, tzinfo=datetime.timezone.utc
                        ),
                    ),
                    occurred_at=datetime.datetime(
                        2023, 9, 4, 11, 10, 46, 53471, tzinfo=datetime.timezone.utc
                    ),
                    delivered_at=datetime.datetime(
                        2023, 9, 4, 11, 10, 46, 422260, tzinfo=datetime.timezone.utc
                    ),
                    replayed_at=None,
                    origin="event",
                    last_attempt_at=datetime.datetime(
                        2023, 9, 4, 11, 10, 46, 173869, tzinfo=datetime.timezone.utc
                    ),
                    retry_at=None,
                    times_attempted=1,
                    notification_setting_id="ntfset_01h7mt960x2r58dp0wrevgzk41",
                ),
                Notification(
                    id="ntf_01h9fxhe651pdwk7m35e4svdah",
                    type="transaction.updated",
                    status="delivered",
                    payload=NotificationPayload(
                        notification_id="ntf_01h9fxhe651pdwk7m35e4svdah",
                        event_id="evt_01h9fxhe42nttzszaxmhvd23h5",
                        event_type="transaction.updated",
                        data=Transaction(
                            items=[
                                {
                                    "price": {
                                        "id": "pri_01h9fwyrg7wtge506jpqjdfekr",
                                        "status": "active",
                                        "quantity": {"maximum": 1, "minimum": 1},
                                        "tax_mode": "account_setting",
                                        "product_id": "pro_01h89b2j66qq82x6vn5d39c4av",
                                        "unit_price": {
                                            "amount": "10000",
                                            "currency_code": "USD",
                                        },
                                        "description": "One time purchase",
                                        "trial_period": None,
                                        "billing_cycle": None,
                                        "unit_price_overrides": [],
                                    },
                                    "quantity": 1,
                                }
                            ],
                            status="completed",
                            customer_id="ctm_01h9fryr8y9k8r4k0fjgkhem6p",
                            address_id="add_01h9fryr9ftp2er4g1sxjhqg8w",
                            business_id=None,
                            discount_id=None,
                            custom_data=None,
                            collection_mode="automatic",
                            billing_details=None,
                            billing_period=BillingPeriod(
                                ends_at="2023-10-04T09:40:06.415402Z",
                                starts_at="2023-09-04T09:40:06.415402Z",
                            ),
                            currency_code="USD",
                            customer_ip_address=None,
                            ignore_trials=None,
                            address=None,
                            id="txn_01h9fxh5ch237z4rnrxb87rqr2",
                            customer=None,
                            business=None,
                            discount=None,
                            seller=None,
                            adjustments_totals=None,
                            origin="subscription_charge",
                            subscription_id="sub_01h9fs0mgwkhtdan4qd4r7qq77",
                            invoice_id="inv_01h9fxh9zw9q2hk2k0f78mra5q",
                            invoice_number="3789-10004",
                            created_at=datetime.datetime(
                                2023,
                                9,
                                4,
                                10,
                                59,
                                4,
                                283136,
                                tzinfo=datetime.timezone.utc,
                            ),
                            updated_at=datetime.datetime(
                                2023,
                                9,
                                4,
                                10,
                                59,
                                12,
                                889595,
                                tzinfo=datetime.timezone.utc,
                            ),
                            billed_at="2023-09-04T10:59:04.209753Z",
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
                                    balance="0",
                                    grand_total="12700",
                                    fee=None,
                                    earnings=None,
                                    currency_code="USD",
                                    exchange_rate="1",
                                ),
                                adjusted_totals=AdjustedTotals(
                                    subtotal="10000",
                                    tax="2700",
                                    total="12700",
                                    grand_total="12700",
                                    fee="0",
                                    earnings="0",
                                    currency_code="USD",
                                ),
                                payout_totals=None,
                                adjusted_payout_totals=None,
                                line_items=[
                                    LineItem(
                                        id="txnitm_01h9fxh5e9gkab3abgn9yvtvdz",
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
                            payments=[
                                {
                                    "amount": "12700",
                                    "status": "captured",
                                    "created_at": "2023-09-04T10:59:04.483431Z",
                                    "error_code": None,
                                    "captured_at": "2023-09-04T10:59:06.850433Z",
                                    "method_details": {
                                        "card": {
                                            "type": "visa",
                                            "last4": "5556",
                                            "expiry_year": 2024,
                                            "expiry_month": 1,
                                        },
                                        "type": "card",
                                    },
                                    "payment_attempt_id": "f237591a-d3a7-4990-b654-c1135347e8ec",
                                    "stored_payment_method_id": "ef9df7ea-5f85-4a64-ad48-c13753540e28",
                                }
                            ],
                            checkout={
                                "url": "https://webstormit.com?_ptxn=txn_01h9fxh5ch237z4rnrxb87rqr2"
                            },
                        ),
                        occurred_at=datetime.datetime(
                            2023, 9, 4, 10, 59, 13, 155048, tzinfo=datetime.timezone.utc
                        ),
                    ),
                    occurred_at=datetime.datetime(
                        2023, 9, 4, 10, 59, 13, 155048, tzinfo=datetime.timezone.utc
                    ),
                    delivered_at=datetime.datetime(
                        2023, 9, 4, 10, 59, 13, 499271, tzinfo=datetime.timezone.utc
                    ),
                    replayed_at=None,
                    origin="event",
                    last_attempt_at=datetime.datetime(
                        2023, 9, 4, 10, 59, 13, 251145, tzinfo=datetime.timezone.utc
                    ),
                    retry_at=None,
                    times_attempted=1,
                    notification_setting_id="ntfset_01h7mt960x2r58dp0wrevgzk41",
                ),
            ],
            meta=dict(
                request_id="dce2a16b-4248-4625-af2e-aba9cb2839e1",
                pagination=dict(
                    per_page=50,
                    estimated_total=2,
                    next="http://sandbox-api.paddle.com/notifications?after=ntf_01h9fxhe651pdwk7m35e4svdah",
                    has_more=True,
                ),
            ),
        )

        assert (
            deepdiff.DeepDiff(notifications, expected_notifications, ignore_order=True)
            == {}
        )

    @pytest.mark.vcr
    def test_replay_notification(self):
        replay_response = self.client.replay_notification(
            notification_id="ntf_01h9g0mtsp2mae24351z8nfsg1"
        )
        expected_response = NotificationReplayResponse(
            data=NotificationReplay(
                event_id=None, notification_id="ntf_01h9gekx4926y70b8n799p93e9"
            ),
            meta=dict(request_id="441af6da-9e20-413e-90e6-5e043a8f8caf"),
        )

        assert (
            deepdiff.DeepDiff(
                replay_response.dict(), expected_response.dict(), ignore_order=True
            )
            == {}
        )
