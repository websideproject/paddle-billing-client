import datetime
import os

import deepdiff
import pytest
from apiclient import HeaderAuthentication

from paddle_billing_client.models.address import Address
from paddle_billing_client.models.adjustment import Adjustment, AdjustmentItem
from paddle_billing_client.models.business import Business, Contact
from paddle_billing_client.models.common import BillingPeriod
from paddle_billing_client.models.customer import Customer
from paddle_billing_client.models.event import Event, EventsResponse
from paddle_billing_client.models.price import BillingCycle, Price, Quantity, UnitPrice
from paddle_billing_client.models.product import Product
from paddle_billing_client.models.subscription import (
    Item,
    ScheduledChange,
    Subscription,
)
from paddle_billing_client.models.transaction import (
    AdjustedPayoutTotals,
    AdjustedTotals,
    BillingDetails,
    ChargebackFee,
    LineItem,
    LineItemProration,
    LineItemTotals,
    LineItemUnitTotals,
    PayoutTotals,
    TaxRatesTotals,
    TaxRatesUsed,
    Totals,
    Transaction,
    TransactionDetails,
)


class TestEvents:
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
    def test_list_events(self):
        events = self.client.list_events()
        expected_events = EventsResponse(
            data=[
                Event(
                    notification_id=None,
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
                Event(
                    notification_id=None,
                    event_id="evt_01h9fy6js58ny2hg9e5ee0m7td",
                    event_type="subscription.updated",
                    data=Subscription(
                        status="active",
                        customer_id="ctm_01h9fryr8y9k8r4k0fjgkhem6p",
                        address_id="add_01h9fryr9ftp2er4g1sxjhqg8w",
                        business_id=None,
                        currency_code="USD",
                        created_at=datetime.datetime(
                            2023, 9, 4, 9, 40, 8, 348000, tzinfo=datetime.timezone.utc
                        ),
                        updated_at=datetime.datetime(
                            2023, 9, 4, 11, 10, 45, 159000, tzinfo=datetime.timezone.utc
                        ),
                        started_at=datetime.datetime(
                            2023, 9, 4, 9, 40, 6, 415402, tzinfo=datetime.timezone.utc
                        ),
                        first_billed_at=datetime.datetime(
                            2023, 9, 4, 9, 40, 6, 415402, tzinfo=datetime.timezone.utc
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
                Event(
                    notification_id=None,
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
                            2023, 9, 4, 10, 59, 4, 283136, tzinfo=datetime.timezone.utc
                        ),
                        updated_at=datetime.datetime(
                            2023, 9, 4, 10, 59, 12, 889595, tzinfo=datetime.timezone.utc
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
                Event(
                    notification_id=None,
                    event_id="evt_01h9fxhah0bv7gpt9b1219ca71",
                    event_type="transaction.completed",
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
                        invoice_id=None,
                        invoice_number=None,
                        created_at=datetime.datetime(
                            2023, 9, 4, 10, 59, 4, 283136, tzinfo=datetime.timezone.utc
                        ),
                        updated_at=datetime.datetime(
                            2023, 9, 4, 10, 59, 7, 707834, tzinfo=datetime.timezone.utc
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
                                fee="685",
                                earnings="9315",
                                currency_code="USD",
                                exchange_rate="1",
                            ),
                            adjusted_totals=AdjustedTotals(
                                subtotal="10000",
                                tax="2700",
                                total="12700",
                                grand_total="12700",
                                fee="685",
                                earnings="9315",
                                currency_code="USD",
                            ),
                            payout_totals=PayoutTotals(
                                subtotal="10000",
                                discount="0",
                                tax="2700",
                                total="12700",
                                credit="0",
                                balance="0",
                                grand_total="12700",
                                fee="685",
                                earnings="9315",
                                currency_code="USD",
                                fee_rate="0.05",
                                exchange_rate="1",
                            ),
                            adjusted_payout_totals=AdjustedPayoutTotals(
                                subtotal="10000",
                                tax="2700",
                                total="12700",
                                fee="685",
                                chargeback_fee=ChargebackFee(amount="0", original=None),
                                earnings="9315",
                                currency_code="USD",
                                exchange_rate="1",
                            ),
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
                        2023, 9, 4, 10, 59, 9, 472592, tzinfo=datetime.timezone.utc
                    ),
                ),
                Event(
                    notification_id=None,
                    event_id="evt_01h9fxh93bfqqax355za7k79c4",
                    event_type="subscription.updated",
                    data=Subscription(
                        status="active",
                        customer_id="ctm_01h9fryr8y9k8r4k0fjgkhem6p",
                        address_id="add_01h9fryr9ftp2er4g1sxjhqg8w",
                        business_id=None,
                        currency_code="USD",
                        created_at=datetime.datetime(
                            2023, 9, 4, 9, 40, 8, 348000, tzinfo=datetime.timezone.utc
                        ),
                        updated_at=datetime.datetime(
                            2023, 9, 4, 10, 59, 4, 165000, tzinfo=datetime.timezone.utc
                        ),
                        started_at=datetime.datetime(
                            2023, 9, 4, 9, 40, 6, 415402, tzinfo=datetime.timezone.utc
                        ),
                        first_billed_at=datetime.datetime(
                            2023, 9, 4, 9, 40, 6, 415402, tzinfo=datetime.timezone.utc
                        ),
                        next_billed_at=datetime.datetime(
                            2023, 10, 4, 9, 40, 6, 415402, tzinfo=datetime.timezone.utc
                        ),
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
                                next_billed_at=datetime.datetime(
                                    2023,
                                    10,
                                    4,
                                    9,
                                    40,
                                    6,
                                    415402,
                                    tzinfo=datetime.timezone.utc,
                                ),
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
                        2023, 9, 4, 10, 59, 8, 11811, tzinfo=datetime.timezone.utc
                    ),
                ),
                Event(
                    notification_id=None,
                    event_id="evt_01h9fxh63wpbbbr8r1s759bvc3",
                    event_type="transaction.billed",
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
                                "price_id": "pri_01h9fwyrg7wtge506jpqjdfekr",
                                "quantity": 1,
                                "proration": None,
                            }
                        ],
                        status="billed",
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
                        invoice_id=None,
                        invoice_number=None,
                        created_at=datetime.datetime(
                            2023, 9, 4, 10, 59, 4, 283136, tzinfo=datetime.timezone.utc
                        ),
                        updated_at=datetime.datetime(
                            2023, 9, 4, 10, 59, 4, 283136, tzinfo=datetime.timezone.utc
                        ),
                        billed_at="2023-09-04T10:59:04.2097533Z",
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
                            ),
                            adjusted_totals=None,
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
                        payments=[],
                        checkout={
                            "url": "https://webstormit.com?_ptxn=txn_01h9fxh5ch237z4rnrxb87rqr2"
                        },
                    ),
                    occurred_at=datetime.datetime(
                        2023, 9, 4, 10, 59, 4, 956753, tzinfo=datetime.timezone.utc
                    ),
                ),
                Event(
                    notification_id=None,
                    event_id="evt_01h9fxh63wnzea8nkkbmexdnw7",
                    event_type="transaction.created",
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
                                "price_id": "pri_01h9fwyrg7wtge506jpqjdfekr",
                                "quantity": 1,
                                "proration": None,
                            }
                        ],
                        status="billed",
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
                        invoice_id=None,
                        invoice_number=None,
                        created_at=datetime.datetime(
                            2023, 9, 4, 10, 59, 4, 283136, tzinfo=datetime.timezone.utc
                        ),
                        updated_at=datetime.datetime(
                            2023, 9, 4, 10, 59, 4, 283136, tzinfo=datetime.timezone.utc
                        ),
                        billed_at="2023-09-04T10:59:04.2097533Z",
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
                            ),
                            adjusted_totals=None,
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
                        payments=[],
                        checkout={
                            "url": "https://webstormit.com?_ptxn=txn_01h9fxh5ch237z4rnrxb87rqr2"
                        },
                    ),
                    occurred_at=datetime.datetime(
                        2023, 9, 4, 10, 59, 4, 956753, tzinfo=datetime.timezone.utc
                    ),
                ),
                Event(
                    notification_id=None,
                    event_id="evt_01h9fwyrypzzy63jy7y9yz1gg4",
                    event_type="price.created",
                    data=Price(
                        description="One time purchase",
                        product_id="pro_01h89b2j66qq82x6vn5d39c4av",
                        billing_cycle=None,
                        trial_period=None,
                        tax_mode="account_setting",
                        unit_price_overrides=[],
                        quantity=Quantity(minimum=1, maximum=1),
                        custom_data=None,
                        id="pri_01h9fwyrg7wtge506jpqjdfekr",
                        unit_price=UnitPrice(amount="10000", currency_code="USD"),
                        status="active",
                    ),
                    occurred_at=datetime.datetime(
                        2023, 9, 4, 10, 49, 1, 654763, tzinfo=datetime.timezone.utc
                    ),
                ),
                Event(
                    notification_id=None,
                    event_id="evt_01h9fs2dsmnrkp8dcfgrtjav2a",
                    event_type="transaction.created",
                    data=Transaction(
                        items=[
                            {
                                "price": {
                                    "id": "pri_01h7mrnc315chey77qhrd32vfs",
                                    "status": "active",
                                    "quantity": {"maximum": 100, "minimum": 1},
                                    "tax_mode": "account_setting",
                                    "product_id": "pro_01h7mrm9f0xvrvvwvkg1b7q8e3",
                                    "unit_price": {
                                        "amount": "1000",
                                        "currency_code": "USD",
                                    },
                                    "description": "asd",
                                    "trial_period": None,
                                    "billing_cycle": {
                                        "interval": "month",
                                        "frequency": 1,
                                    },
                                    "unit_price_overrides": [],
                                },
                                "price_id": "pri_01h7mrnc315chey77qhrd32vfs",
                                "quantity": 1,
                                "proration": {
                                    "rate": "0",
                                    "billing_period": {
                                        "ends_at": "2023-10-04T09:40:06.415402Z",
                                        "starts_at": "2023-09-04T09:40:06.415402Z",
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
                        address=None,
                        id="txn_01h9fs2d1n49jdh2we7aqb08m0",
                        customer=None,
                        business=None,
                        discount=None,
                        seller=None,
                        adjustments_totals=None,
                        origin="subscription_payment_method_change",
                        subscription_id="sub_01h9fs0mgwkhtdan4qd4r7qq77",
                        invoice_id=None,
                        invoice_number=None,
                        created_at=datetime.datetime(
                            2023, 9, 4, 9, 41, 6, 283577, tzinfo=datetime.timezone.utc
                        ),
                        updated_at=datetime.datetime(
                            2023, 9, 4, 9, 41, 6, 283577, tzinfo=datetime.timezone.utc
                        ),
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
                            ),
                            adjusted_totals=None,
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
                                        description=None,
                                        image_url=None,
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
                    ),
                    occurred_at=datetime.datetime(
                        2023, 9, 4, 9, 41, 6, 996624, tzinfo=datetime.timezone.utc
                    ),
                ),
                Event(
                    notification_id=None,
                    event_id="evt_01h9fs2dsc7f9vj1np59s7nv60",
                    event_type="transaction.ready",
                    data=Transaction(
                        items=[
                            {
                                "price": {
                                    "id": "pri_01h7mrnc315chey77qhrd32vfs",
                                    "status": "active",
                                    "quantity": {"maximum": 100, "minimum": 1},
                                    "tax_mode": "account_setting",
                                    "product_id": "pro_01h7mrm9f0xvrvvwvkg1b7q8e3",
                                    "unit_price": {
                                        "amount": "1000",
                                        "currency_code": "USD",
                                    },
                                    "description": "asd",
                                    "trial_period": None,
                                    "billing_cycle": {
                                        "interval": "month",
                                        "frequency": 1,
                                    },
                                    "unit_price_overrides": [],
                                },
                                "price_id": "pri_01h7mrnc315chey77qhrd32vfs",
                                "quantity": 1,
                                "proration": {
                                    "rate": "0",
                                    "billing_period": {
                                        "ends_at": "2023-10-04T09:40:06.415402Z",
                                        "starts_at": "2023-09-04T09:40:06.415402Z",
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
                        address=None,
                        id="txn_01h9fs2d1n49jdh2we7aqb08m0",
                        customer=None,
                        business=None,
                        discount=None,
                        seller=None,
                        adjustments_totals=None,
                        origin="subscription_payment_method_change",
                        subscription_id="sub_01h9fs0mgwkhtdan4qd4r7qq77",
                        invoice_id=None,
                        invoice_number=None,
                        created_at=datetime.datetime(
                            2023, 9, 4, 9, 41, 6, 283577, tzinfo=datetime.timezone.utc
                        ),
                        updated_at=datetime.datetime(
                            2023, 9, 4, 9, 41, 6, 283577, tzinfo=datetime.timezone.utc
                        ),
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
                            ),
                            adjusted_totals=None,
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
                                        description=None,
                                        image_url=None,
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
                    ),
                    occurred_at=datetime.datetime(
                        2023, 9, 4, 9, 41, 6, 988841, tzinfo=datetime.timezone.utc
                    ),
                ),
                Event(
                    notification_id=None,
                    event_id="evt_01h9fs0s0ttfmrns1nahk8fa87",
                    event_type="transaction.updated",
                    data=Transaction(
                        items=[
                            {
                                "price": {
                                    "id": "pri_01h7mrnc315chey77qhrd32vfs",
                                    "status": "active",
                                    "quantity": {"maximum": 100, "minimum": 1},
                                    "tax_mode": "account_setting",
                                    "product_id": "pro_01h7mrm9f0xvrvvwvkg1b7q8e3",
                                    "unit_price": {
                                        "amount": "1000",
                                        "currency_code": "USD",
                                    },
                                    "description": "asd",
                                    "trial_period": None,
                                    "billing_cycle": {
                                        "interval": "month",
                                        "frequency": 1,
                                    },
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
                        id="txn_01h9fry5ra42drtnvwwp2a16dz",
                        customer=None,
                        business=None,
                        discount=None,
                        seller=None,
                        adjustments_totals=None,
                        origin="web",
                        subscription_id="sub_01h9fs0mgwkhtdan4qd4r7qq77",
                        invoice_id="inv_01h9fs0m3pj1kg91cvj2gkw9kw",
                        invoice_number="3789-10003",
                        created_at=datetime.datetime(
                            2023, 9, 4, 9, 38, 47, 770001, tzinfo=datetime.timezone.utc
                        ),
                        updated_at=datetime.datetime(
                            2023, 9, 4, 9, 40, 12, 644309, tzinfo=datetime.timezone.utc
                        ),
                        billed_at="2023-09-04T09:40:07.314875Z",
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
                                balance="0",
                                grand_total="1270",
                                fee=None,
                                earnings=None,
                                currency_code="USD",
                                exchange_rate="1",
                            ),
                            adjusted_totals=AdjustedTotals(
                                subtotal="1000",
                                tax="270",
                                total="1270",
                                grand_total="1270",
                                fee="0",
                                earnings="0",
                                currency_code="USD",
                            ),
                            payout_totals=None,
                            adjusted_payout_totals=None,
                            line_items=[
                                LineItem(
                                    id="txnitm_01h9fryrd4h20qj3dcr4npc5d2",
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
                                        description=None,
                                        image_url=None,
                                        custom_data=None,
                                        status="active",
                                        id="pro_01h7mrm9f0xvrvvwvkg1b7q8e3",
                                        created_at=None,
                                        prices=None,
                                    ),
                                )
                            ],
                        ),
                        payments=[
                            {
                                "amount": "1270",
                                "status": "captured",
                                "created_at": "2023-09-04T09:39:58.95295Z",
                                "error_code": None,
                                "captured_at": "2023-09-04T09:40:06.415402Z",
                                "method_details": {
                                    "card": {
                                        "type": "visa",
                                        "last4": "5556",
                                        "expiry_year": 2024,
                                        "expiry_month": 1,
                                    },
                                    "type": "card",
                                },
                                "payment_attempt_id": "56c7c504-909a-4196-ab2f-2d5c38cd4fdb",
                                "stored_payment_method_id": "ef9df7ea-5f85-4a64-ad48-c13753540e28",
                            }
                        ],
                        checkout={
                            "url": "https://webstormit.com?_ptxn=txn_01h9fry5ra42drtnvwwp2a16dz"
                        },
                    ),
                    occurred_at=datetime.datetime(
                        2023, 9, 4, 9, 40, 12, 954416, tzinfo=datetime.timezone.utc
                    ),
                ),
                Event(
                    notification_id=None,
                    event_id="evt_01h9fs0ngq0adgwq8cpy0stmej",
                    event_type="transaction.updated",
                    data=Transaction(
                        items=[
                            {
                                "price": {
                                    "id": "pri_01h7mrnc315chey77qhrd32vfs",
                                    "status": "active",
                                    "quantity": {"maximum": 100, "minimum": 1},
                                    "tax_mode": "account_setting",
                                    "product_id": "pro_01h7mrm9f0xvrvvwvkg1b7q8e3",
                                    "unit_price": {
                                        "amount": "1000",
                                        "currency_code": "USD",
                                    },
                                    "description": "asd",
                                    "trial_period": None,
                                    "billing_cycle": {
                                        "interval": "month",
                                        "frequency": 1,
                                    },
                                    "unit_price_overrides": [],
                                },
                                "quantity": 1,
                                "proration": {
                                    "rate": "0",
                                    "billing_period": {
                                        "ends_at": "0001-01-01T00:00:00Z",
                                        "starts_at": "0001-01-01T00:00:00Z",
                                    },
                                },
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
                        id="txn_01h9fry5ra42drtnvwwp2a16dz",
                        customer=None,
                        business=None,
                        discount=None,
                        seller=None,
                        adjustments_totals=None,
                        origin="web",
                        subscription_id="sub_01h9fs0mgwkhtdan4qd4r7qq77",
                        invoice_id=None,
                        invoice_number=None,
                        created_at=datetime.datetime(
                            2023, 9, 4, 9, 38, 47, 770001, tzinfo=datetime.timezone.utc
                        ),
                        updated_at=datetime.datetime(
                            2023, 9, 4, 9, 40, 9, 144366, tzinfo=datetime.timezone.utc
                        ),
                        billed_at="2023-09-04T09:40:07.314875Z",
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
                                balance="0",
                                grand_total="1270",
                                fee=None,
                                earnings=None,
                                currency_code="USD",
                                exchange_rate="1",
                            ),
                            adjusted_totals=AdjustedTotals(
                                subtotal="1000",
                                tax="270",
                                total="1270",
                                grand_total="1270",
                                fee="0",
                                earnings="0",
                                currency_code="USD",
                            ),
                            payout_totals=None,
                            adjusted_payout_totals=None,
                            line_items=[
                                LineItem(
                                    id="txnitm_01h9fryrd4h20qj3dcr4npc5d2",
                                    price_id="pri_01h7mrnc315chey77qhrd32vfs",
                                    quantity=1,
                                    proration=LineItemProration(
                                        rate="0",
                                        billing_period=BillingPeriod(
                                            ends_at="0001-01-01T00:00:00Z",
                                            starts_at="0001-01-01T00:00:00Z",
                                        ),
                                    ),
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
                                        description=None,
                                        image_url=None,
                                        custom_data=None,
                                        status="active",
                                        id="pro_01h7mrm9f0xvrvvwvkg1b7q8e3",
                                        created_at=None,
                                        prices=None,
                                    ),
                                )
                            ],
                        ),
                        payments=[
                            {
                                "amount": "1270",
                                "status": "captured",
                                "created_at": "2023-09-04T09:39:58.95295Z",
                                "error_code": None,
                                "captured_at": "2023-09-04T09:40:06.415402Z",
                                "method_details": {
                                    "card": {
                                        "type": "visa",
                                        "last4": "5556",
                                        "expiry_year": 2024,
                                        "expiry_month": 1,
                                    },
                                    "type": "card",
                                },
                                "payment_attempt_id": "56c7c504-909a-4196-ab2f-2d5c38cd4fdb",
                                "stored_payment_method_id": "ef9df7ea-5f85-4a64-ad48-c13753540e28",
                            }
                        ],
                        checkout={
                            "url": "https://webstormit.com?_ptxn=txn_01h9fry5ra42drtnvwwp2a16dz"
                        },
                    ),
                    occurred_at=datetime.datetime(
                        2023, 9, 4, 9, 40, 9, 367148, tzinfo=datetime.timezone.utc
                    ),
                ),
                Event(
                    notification_id=None,
                    event_id="evt_01h9fs0nadngthj7ekep98qnhf",
                    event_type="subscription.activated",
                    data=Subscription(
                        status="active",
                        customer_id="ctm_01h9fryr8y9k8r4k0fjgkhem6p",
                        address_id="add_01h9fryr9ftp2er4g1sxjhqg8w",
                        business_id=None,
                        currency_code="USD",
                        created_at=datetime.datetime(
                            2023, 9, 4, 9, 40, 8, 348000, tzinfo=datetime.timezone.utc
                        ),
                        updated_at=datetime.datetime(
                            2023, 9, 4, 9, 40, 8, 348000, tzinfo=datetime.timezone.utc
                        ),
                        started_at=datetime.datetime(
                            2023, 9, 4, 9, 40, 6, 415402, tzinfo=datetime.timezone.utc
                        ),
                        first_billed_at=datetime.datetime(
                            2023, 9, 4, 9, 40, 6, 415402, tzinfo=datetime.timezone.utc
                        ),
                        next_billed_at=datetime.datetime(
                            2023, 10, 4, 9, 40, 6, 415402, tzinfo=datetime.timezone.utc
                        ),
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
                                next_billed_at=datetime.datetime(
                                    2023,
                                    10,
                                    4,
                                    9,
                                    40,
                                    6,
                                    415402,
                                    tzinfo=datetime.timezone.utc,
                                ),
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
                        2023, 9, 4, 9, 40, 9, 166024, tzinfo=datetime.timezone.utc
                    ),
                ),
                Event(
                    notification_id=None,
                    event_id="evt_01h9fs0n9wvsk5sbce5tabnmca",
                    event_type="subscription.created",
                    data=Subscription(
                        status="active",
                        customer_id="ctm_01h9fryr8y9k8r4k0fjgkhem6p",
                        address_id="add_01h9fryr9ftp2er4g1sxjhqg8w",
                        business_id=None,
                        currency_code="USD",
                        created_at=datetime.datetime(
                            2023, 9, 4, 9, 40, 8, 348000, tzinfo=datetime.timezone.utc
                        ),
                        updated_at=datetime.datetime(
                            2023, 9, 4, 9, 40, 8, 348000, tzinfo=datetime.timezone.utc
                        ),
                        started_at=datetime.datetime(
                            2023, 9, 4, 9, 40, 6, 415402, tzinfo=datetime.timezone.utc
                        ),
                        first_billed_at=datetime.datetime(
                            2023, 9, 4, 9, 40, 6, 415402, tzinfo=datetime.timezone.utc
                        ),
                        next_billed_at=datetime.datetime(
                            2023, 10, 4, 9, 40, 6, 415402, tzinfo=datetime.timezone.utc
                        ),
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
                                next_billed_at=datetime.datetime(
                                    2023,
                                    10,
                                    4,
                                    9,
                                    40,
                                    6,
                                    415402,
                                    tzinfo=datetime.timezone.utc,
                                ),
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
                        transaction_id="txn_01h9fry5ra42drtnvwwp2a16dz",
                    ),
                    occurred_at=datetime.datetime(
                        2023, 9, 4, 9, 40, 9, 148441, tzinfo=datetime.timezone.utc
                    ),
                ),
                Event(
                    notification_id=None,
                    event_id="evt_01h9fs0mkwjyyn1hdktk2ekps2",
                    event_type="transaction.completed",
                    data=Transaction(
                        items=[
                            {
                                "price": {
                                    "id": "pri_01h7mrnc315chey77qhrd32vfs",
                                    "status": "active",
                                    "quantity": {"maximum": 100, "minimum": 1},
                                    "tax_mode": "account_setting",
                                    "product_id": "pro_01h7mrm9f0xvrvvwvkg1b7q8e3",
                                    "unit_price": {
                                        "amount": "1000",
                                        "currency_code": "USD",
                                    },
                                    "description": "asd",
                                    "trial_period": None,
                                    "billing_cycle": {
                                        "interval": "month",
                                        "frequency": 1,
                                    },
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
                        billing_period=None,
                        currency_code="USD",
                        customer_ip_address=None,
                        ignore_trials=None,
                        address=None,
                        id="txn_01h9fry5ra42drtnvwwp2a16dz",
                        customer=None,
                        business=None,
                        discount=None,
                        seller=None,
                        adjustments_totals=None,
                        origin="web",
                        subscription_id=None,
                        invoice_id=None,
                        invoice_number=None,
                        created_at=datetime.datetime(
                            2023, 9, 4, 9, 38, 47, 770001, tzinfo=datetime.timezone.utc
                        ),
                        updated_at=datetime.datetime(
                            2023, 9, 4, 9, 40, 7, 314878, tzinfo=datetime.timezone.utc
                        ),
                        billed_at="2023-09-04T09:40:07.314875Z",
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
                                balance="0",
                                grand_total="1270",
                                fee="114",
                                earnings="886",
                                currency_code="USD",
                                exchange_rate="1",
                            ),
                            adjusted_totals=AdjustedTotals(
                                subtotal="1000",
                                tax="270",
                                total="1270",
                                grand_total="1270",
                                fee="114",
                                earnings="886",
                                currency_code="USD",
                            ),
                            payout_totals=PayoutTotals(
                                subtotal="1000",
                                discount="0",
                                tax="270",
                                total="1270",
                                credit="0",
                                balance="0",
                                grand_total="1270",
                                fee="114",
                                earnings="886",
                                currency_code="USD",
                                fee_rate="0.05",
                                exchange_rate="1",
                            ),
                            adjusted_payout_totals=AdjustedPayoutTotals(
                                subtotal="1000",
                                tax="270",
                                total="1270",
                                fee="114",
                                chargeback_fee=ChargebackFee(amount="0", original=None),
                                earnings="886",
                                currency_code="USD",
                                exchange_rate="1",
                            ),
                            line_items=[
                                LineItem(
                                    id="txnitm_01h9fryrd4h20qj3dcr4npc5d2",
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
                                        description=None,
                                        image_url=None,
                                        custom_data=None,
                                        status="active",
                                        id="pro_01h7mrm9f0xvrvvwvkg1b7q8e3",
                                        created_at=None,
                                        prices=None,
                                    ),
                                )
                            ],
                        ),
                        payments=[
                            {
                                "amount": "1270",
                                "status": "captured",
                                "created_at": "2023-09-04T09:39:58.95295Z",
                                "error_code": None,
                                "captured_at": "2023-09-04T09:40:06.415402Z",
                                "method_details": {
                                    "card": {
                                        "type": "visa",
                                        "last4": "5556",
                                        "expiry_year": 2024,
                                        "expiry_month": 1,
                                    },
                                    "type": "card",
                                },
                                "payment_attempt_id": "56c7c504-909a-4196-ab2f-2d5c38cd4fdb",
                                "stored_payment_method_id": "ef9df7ea-5f85-4a64-ad48-c13753540e28",
                            }
                        ],
                        checkout={
                            "url": "https://webstormit.com?_ptxn=txn_01h9fry5ra42drtnvwwp2a16dz"
                        },
                    ),
                    occurred_at=datetime.datetime(
                        2023, 9, 4, 9, 40, 8, 444970, tzinfo=datetime.timezone.utc
                    ),
                ),
                Event(
                    notification_id=None,
                    event_id="evt_01h9fryrxydkskmjse59dvywgv",
                    event_type="address.created",
                    data=Address(
                        description=None,
                        first_line=None,
                        second_line=None,
                        city=None,
                        postal_code=None,
                        region=None,
                        country_code="HU",
                        status="active",
                        id="add_01h9fryr9ftp2er4g1sxjhqg8w",
                        created_at=datetime.datetime(
                            2023, 9, 4, 9, 39, 6, 671000, tzinfo=datetime.timezone.utc
                        ),
                        updated_at=datetime.datetime(
                            2023, 9, 4, 9, 39, 6, 671000, tzinfo=datetime.timezone.utc
                        ),
                    ),
                    occurred_at=datetime.datetime(
                        2023, 9, 4, 9, 39, 7, 326862, tzinfo=datetime.timezone.utc
                    ),
                ),
                Event(
                    notification_id=None,
                    event_id="evt_01h9fryrvat82dm82kqs6jpavm",
                    event_type="customer.created",
                    data=Customer(
                        email="asd1@asd.com",
                        name=None,
                        locale="en",
                        id="ctm_01h9fryr8y9k8r4k0fjgkhem6p",
                        marketing_consent=True,
                        created_at=datetime.datetime(
                            2023, 9, 4, 9, 39, 6, 654000, tzinfo=datetime.timezone.utc
                        ),
                        updated_at=datetime.datetime(
                            2023, 9, 4, 9, 39, 6, 654000, tzinfo=datetime.timezone.utc
                        ),
                        imported_at=None,
                        source=None,
                        status="active",
                        is_sanctioned=None,
                        tax_exemptions=None,
                    ),
                    occurred_at=datetime.datetime(
                        2023, 9, 4, 9, 39, 7, 242375, tzinfo=datetime.timezone.utc
                    ),
                ),
                Event(
                    notification_id=None,
                    event_id="evt_01h9fryrtc4xzw4hr2t5peq9ec",
                    event_type="transaction.ready",
                    data=Transaction(
                        items=[
                            {
                                "price": {
                                    "id": "pri_01h7mrnc315chey77qhrd32vfs",
                                    "status": "active",
                                    "quantity": {"maximum": 100, "minimum": 1},
                                    "tax_mode": "account_setting",
                                    "product_id": "pro_01h7mrm9f0xvrvvwvkg1b7q8e3",
                                    "unit_price": {
                                        "amount": "1000",
                                        "currency_code": "USD",
                                    },
                                    "description": "asd",
                                    "trial_period": None,
                                    "billing_cycle": {
                                        "interval": "month",
                                        "frequency": 1,
                                    },
                                    "unit_price_overrides": [],
                                },
                                "quantity": 1,
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
                        billing_period=None,
                        currency_code="USD",
                        customer_ip_address=None,
                        ignore_trials=None,
                        address=None,
                        id="txn_01h9fry5ra42drtnvwwp2a16dz",
                        customer=None,
                        business=None,
                        discount=None,
                        seller=None,
                        adjustments_totals=None,
                        origin="web",
                        subscription_id=None,
                        invoice_id=None,
                        invoice_number=None,
                        created_at=datetime.datetime(
                            2023, 9, 4, 9, 38, 47, 770001, tzinfo=datetime.timezone.utc
                        ),
                        updated_at=datetime.datetime(
                            2023, 9, 4, 9, 39, 6, 796378, tzinfo=datetime.timezone.utc
                        ),
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
                            adjusted_totals=AdjustedTotals(
                                subtotal="1000",
                                tax="270",
                                total="1270",
                                grand_total="1270",
                                fee="0",
                                earnings="0",
                                currency_code="USD",
                            ),
                            payout_totals=None,
                            adjusted_payout_totals=None,
                            line_items=[
                                LineItem(
                                    id="txnitm_01h9fryrd4h20qj3dcr4npc5d2",
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
                                        description=None,
                                        image_url=None,
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
                            "url": "https://webstormit.com?_ptxn=txn_01h9fry5ra42drtnvwwp2a16dz"
                        },
                    ),
                    occurred_at=datetime.datetime(
                        2023, 9, 4, 9, 39, 7, 212655, tzinfo=datetime.timezone.utc
                    ),
                ),
                Event(
                    notification_id=None,
                    event_id="evt_01h9fryrrf1arppa2csg1v3r1c",
                    event_type="transaction.updated",
                    data=Transaction(
                        items=[
                            {
                                "price": {
                                    "id": "pri_01h7mrnc315chey77qhrd32vfs",
                                    "status": "active",
                                    "quantity": {"maximum": 100, "minimum": 1},
                                    "tax_mode": "account_setting",
                                    "product_id": "pro_01h7mrm9f0xvrvvwvkg1b7q8e3",
                                    "unit_price": {
                                        "amount": "1000",
                                        "currency_code": "USD",
                                    },
                                    "description": "asd",
                                    "trial_period": None,
                                    "billing_cycle": {
                                        "interval": "month",
                                        "frequency": 1,
                                    },
                                    "unit_price_overrides": [],
                                },
                                "quantity": 1,
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
                        billing_period=None,
                        currency_code="USD",
                        customer_ip_address=None,
                        ignore_trials=None,
                        address=None,
                        id="txn_01h9fry5ra42drtnvwwp2a16dz",
                        customer=None,
                        business=None,
                        discount=None,
                        seller=None,
                        adjustments_totals=None,
                        origin="web",
                        subscription_id=None,
                        invoice_id=None,
                        invoice_number=None,
                        created_at=datetime.datetime(
                            2023, 9, 4, 9, 38, 47, 770001, tzinfo=datetime.timezone.utc
                        ),
                        updated_at=datetime.datetime(
                            2023, 9, 4, 9, 39, 6, 796378, tzinfo=datetime.timezone.utc
                        ),
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
                            adjusted_totals=AdjustedTotals(
                                subtotal="1000",
                                tax="270",
                                total="1270",
                                grand_total="1270",
                                fee="0",
                                earnings="0",
                                currency_code="USD",
                            ),
                            payout_totals=None,
                            adjusted_payout_totals=None,
                            line_items=[
                                LineItem(
                                    id="txnitm_01h9fryrd4h20qj3dcr4npc5d2",
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
                                        description=None,
                                        image_url=None,
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
                            "url": "https://webstormit.com?_ptxn=txn_01h9fry5ra42drtnvwwp2a16dz"
                        },
                    ),
                    occurred_at=datetime.datetime(
                        2023, 9, 4, 9, 39, 7, 151585, tzinfo=datetime.timezone.utc
                    ),
                ),
                Event(
                    notification_id=None,
                    event_id="evt_01h9fry6za208s8td0t0ym815c",
                    event_type="transaction.created",
                    data=Transaction(
                        items=[
                            {
                                "price": {
                                    "id": "pri_01h7mrnc315chey77qhrd32vfs",
                                    "status": "active",
                                    "quantity": {"maximum": 100, "minimum": 1},
                                    "tax_mode": "account_setting",
                                    "product_id": "pro_01h7mrm9f0xvrvvwvkg1b7q8e3",
                                    "unit_price": {
                                        "amount": "1000",
                                        "currency_code": "USD",
                                    },
                                    "description": "asd",
                                    "trial_period": None,
                                    "billing_cycle": {
                                        "interval": "month",
                                        "frequency": 1,
                                    },
                                    "unit_price_overrides": [],
                                },
                                "price_id": "pri_01h7mrnc315chey77qhrd32vfs",
                                "quantity": 1,
                                "proration": None,
                            }
                        ],
                        status="draft",
                        customer_id=None,
                        address_id=None,
                        business_id=None,
                        discount_id=None,
                        custom_data=None,
                        collection_mode="automatic",
                        billing_details=None,
                        billing_period=None,
                        currency_code="USD",
                        customer_ip_address=None,
                        ignore_trials=None,
                        address=None,
                        id="txn_01h9fry5ra42drtnvwwp2a16dz",
                        customer=None,
                        business=None,
                        discount=None,
                        seller=None,
                        adjustments_totals=None,
                        origin="web",
                        subscription_id=None,
                        invoice_id=None,
                        invoice_number=None,
                        created_at=datetime.datetime(
                            2023, 9, 4, 9, 38, 47, 770001, tzinfo=datetime.timezone.utc
                        ),
                        updated_at=datetime.datetime(
                            2023, 9, 4, 9, 38, 47, 770001, tzinfo=datetime.timezone.utc
                        ),
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
                            ),
                            adjusted_totals=None,
                            payout_totals=None,
                            adjusted_payout_totals=None,
                            line_items=[
                                LineItem(
                                    id="txnitm_01h9fry5sqvqymcgefwz5h2eym",
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
                                        description=None,
                                        image_url=None,
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
                            "url": "https://webstormit.com?_ptxn=txn_01h9fry5ra42drtnvwwp2a16dz"
                        },
                    ),
                    occurred_at=datetime.datetime(
                        2023, 9, 4, 9, 38, 48, 938907, tzinfo=datetime.timezone.utc
                    ),
                ),
                Event(
                    notification_id=None,
                    event_id="evt_01h9frxehahz646as6ggcy22de",
                    event_type="transaction.created",
                    data=Transaction(
                        items=[
                            {
                                "price": {
                                    "id": "pri_01h7mrnc315chey77qhrd32vfs",
                                    "status": "active",
                                    "quantity": {"maximum": 100, "minimum": 1},
                                    "tax_mode": "account_setting",
                                    "product_id": "pro_01h7mrm9f0xvrvvwvkg1b7q8e3",
                                    "unit_price": {
                                        "amount": "1000",
                                        "currency_code": "USD",
                                    },
                                    "description": "asd",
                                    "trial_period": None,
                                    "billing_cycle": {
                                        "interval": "month",
                                        "frequency": 1,
                                    },
                                    "unit_price_overrides": [],
                                },
                                "price_id": "pri_01h7mrnc315chey77qhrd32vfs",
                                "quantity": 1,
                                "proration": None,
                            }
                        ],
                        status="draft",
                        customer_id=None,
                        address_id=None,
                        business_id=None,
                        discount_id=None,
                        custom_data=None,
                        collection_mode="automatic",
                        billing_details=None,
                        billing_period=None,
                        currency_code="USD",
                        customer_ip_address=None,
                        ignore_trials=None,
                        address=None,
                        id="txn_01h9frxdtvwbrfy7aepjwe2sme",
                        customer=None,
                        business=None,
                        discount=None,
                        seller=None,
                        adjustments_totals=None,
                        origin="web",
                        subscription_id=None,
                        invoice_id=None,
                        invoice_number=None,
                        created_at=datetime.datetime(
                            2023, 9, 4, 9, 38, 23, 254764, tzinfo=datetime.timezone.utc
                        ),
                        updated_at=datetime.datetime(
                            2023, 9, 4, 9, 38, 23, 254764, tzinfo=datetime.timezone.utc
                        ),
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
                            ),
                            adjusted_totals=None,
                            payout_totals=None,
                            adjusted_payout_totals=None,
                            line_items=[
                                LineItem(
                                    id="txnitm_01h9frxdw6zv7r2kj8t9bnrvqs",
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
                                        description=None,
                                        image_url=None,
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
                            "url": "https://webstormit.com?_ptxn=txn_01h9frxdtvwbrfy7aepjwe2sme"
                        },
                    ),
                    occurred_at=datetime.datetime(
                        2023, 9, 4, 9, 38, 23, 914730, tzinfo=datetime.timezone.utc
                    ),
                ),
                Event(
                    notification_id=None,
                    event_id="evt_01h9fqcaarn5bym9t4v5dbh8g2",
                    event_type="subscription.updated",
                    data=Subscription(
                        status="active",
                        customer_id="ctm_01h7mrr5j8rnawwzh9nschgp1v",
                        address_id="add_01h7mrzwtwthvqqy7vq90f0kd7",
                        business_id=None,
                        currency_code="USD",
                        created_at=datetime.datetime(
                            2023,
                            8,
                            12,
                            14,
                            44,
                            57,
                            746086,
                            tzinfo=datetime.timezone.utc,
                        ),
                        updated_at=datetime.datetime(
                            2023, 9, 4, 9, 11, 33, 105000, tzinfo=datetime.timezone.utc
                        ),
                        started_at=datetime.datetime(
                            2023,
                            8,
                            12,
                            14,
                            44,
                            57,
                            746081,
                            tzinfo=datetime.timezone.utc,
                        ),
                        first_billed_at=datetime.datetime(
                            2023,
                            8,
                            12,
                            14,
                            44,
                            57,
                            746081,
                            tzinfo=datetime.timezone.utc,
                        ),
                        next_billed_at=datetime.datetime(
                            2023,
                            9,
                            12,
                            14,
                            44,
                            57,
                            746081,
                            tzinfo=datetime.timezone.utc,
                        ),
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
                            ends_at="2023-09-12T14:44:57.746081Z",
                            starts_at="2023-08-12T14:44:57.746081Z",
                        ),
                        billing_cycle=BillingCycle(interval="month", frequency=1),
                        recurring_transaction_details=None,
                        scheduled_change=None,
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
                                quantity=2,
                                recurring=True,
                                created_at=datetime.datetime(
                                    2023,
                                    8,
                                    12,
                                    14,
                                    44,
                                    57,
                                    746087,
                                    tzinfo=datetime.timezone.utc,
                                ),
                                updated_at=datetime.datetime(
                                    2023,
                                    9,
                                    4,
                                    9,
                                    11,
                                    33,
                                    96000,
                                    tzinfo=datetime.timezone.utc,
                                ),
                                next_billed_at=datetime.datetime(
                                    2023,
                                    9,
                                    12,
                                    14,
                                    44,
                                    57,
                                    746081,
                                    tzinfo=datetime.timezone.utc,
                                ),
                                previously_billed_at=datetime.datetime(
                                    2023,
                                    8,
                                    12,
                                    14,
                                    44,
                                    57,
                                    746081,
                                    tzinfo=datetime.timezone.utc,
                                ),
                                trial_dates=None,
                            )
                        ],
                        custom_data={"user_id": "123"},
                        management_urls=None,
                        id="sub_01h7n3a88jwktex2tfjzahmn57",
                        next_transaction=None,
                        immediate_transaction=None,
                        discount=None,
                    ),
                    occurred_at=datetime.datetime(
                        2023, 9, 4, 9, 11, 33, 976128, tzinfo=datetime.timezone.utc
                    ),
                ),
                Event(
                    notification_id=None,
                    event_id="evt_01h9fk7ye82vmwc361fqz5ww10",
                    event_type="adjustment.created",
                    data=Adjustment(
                        action="refund",
                        transaction_id="txn_01h7n3a7g7h0qr49zt9ckgketd",
                        reason="Test Adjustment Reason",
                        items=[
                            AdjustmentItem(
                                id="adjitm_01h9fk7y5yj1m9bcn2726rdepp",
                                item_id="txnitm_01h7n3a7jefxzqhpaw6hdc523q",
                                type="partial",
                                amount="100",
                                proration=None,
                                totals={"tax": "21", "total": "100", "subtotal": "79"},
                            )
                        ],
                        id="adj_01h9fk7y5yj1m9bcn270a6rs81",
                        subscription_id="sub_01h7n3a88jwktex2tfjzahmn57",
                        customer_id="ctm_01h7mrr5j8rnawwzh9nschgp1v",
                        currency_code="USD",
                        status="pending_approval",
                        totals={
                            "fee": "3",
                            "tax": "21",
                            "total": "100",
                            "earnings": "76",
                            "subtotal": "79",
                            "currency_code": "USD",
                        },
                        payout_totals={
                            "fee": "3",
                            "tax": "21",
                            "total": "100",
                            "earnings": "76",
                            "subtotal": "79",
                            "currency_code": "USD",
                        },
                        created_at=datetime.datetime(
                            2023, 9, 4, 7, 59, 16, 172081, tzinfo=datetime.timezone.utc
                        ),
                        updated_at=datetime.datetime(
                            1, 1, 1, 0, 0, tzinfo=datetime.timezone.utc
                        ),
                        credit_applied_to_balance=None,
                    ),
                    occurred_at=datetime.datetime(
                        2023, 9, 4, 7, 59, 16, 424976, tzinfo=datetime.timezone.utc
                    ),
                ),
                Event(
                    notification_id=None,
                    event_id="evt_01h9fk61zckx4zpc6tjbtab57v",
                    event_type="transaction.completed",
                    data=Transaction(
                        items=[
                            {
                                "price": {
                                    "id": "pri_01h7mrnc315chey77qhrd32vfs",
                                    "status": "active",
                                    "quantity": {"maximum": 100, "minimum": 1},
                                    "tax_mode": "account_setting",
                                    "product_id": "pro_01h7mrm9f0xvrvvwvkg1b7q8e3",
                                    "unit_price": {
                                        "amount": "1000",
                                        "currency_code": "USD",
                                    },
                                    "description": "asd",
                                    "trial_period": None,
                                    "billing_cycle": {
                                        "interval": "month",
                                        "frequency": 1,
                                    },
                                    "unit_price_overrides": [],
                                },
                                "quantity": 1,
                            }
                        ],
                        status="completed",
                        customer_id="ctm_01h7mrr5j8rnawwzh9nschgp1v",
                        address_id="add_01h7mrzwtwthvqqy7vq90f0kd7",
                        business_id=None,
                        discount_id=None,
                        custom_data={"user_id": "123"},
                        collection_mode="manual",
                        billing_details=BillingDetails(
                            enable_checkout=True,
                            payment_terms={"interval": "day", "frequency": 14},
                            purchase_order_number=None,
                            additional_information=None,
                        ),
                        billing_period=None,
                        currency_code="USD",
                        customer_ip_address=None,
                        ignore_trials=None,
                        address=None,
                        id="txn_01h7n3a7g7h0qr49zt9ckgketd",
                        customer=None,
                        business=None,
                        discount=None,
                        seller=None,
                        adjustments_totals=None,
                        origin="api",
                        subscription_id="sub_01h7n3a88jwktex2tfjzahmn57",
                        invoice_id="inv_01h7n3a8d44tngnq7cmka6w7hs",
                        invoice_number="3789-10001",
                        created_at=datetime.datetime(
                            2023, 8, 12, 14, 44, 57, 79835, tzinfo=datetime.timezone.utc
                        ),
                        updated_at=datetime.datetime(
                            2023, 9, 4, 7, 58, 13, 312698, tzinfo=datetime.timezone.utc
                        ),
                        billed_at="2023-08-12T14:44:56.967138Z",
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
                                balance="0",
                                grand_total="1270",
                                fee="44",
                                earnings="956",
                                currency_code="USD",
                                exchange_rate="1",
                            ),
                            adjusted_totals=AdjustedTotals(
                                subtotal="1000",
                                tax="270",
                                total="1270",
                                grand_total="1270",
                                fee="44",
                                earnings="956",
                                currency_code="USD",
                            ),
                            payout_totals=PayoutTotals(
                                subtotal="1000",
                                discount="0",
                                tax="270",
                                total="1270",
                                credit="0",
                                balance="0",
                                grand_total="1270",
                                fee="44",
                                earnings="956",
                                currency_code="USD",
                                fee_rate="0.035",
                                exchange_rate="1",
                            ),
                            adjusted_payout_totals=AdjustedPayoutTotals(
                                subtotal="1000",
                                tax="270",
                                total="1270",
                                fee="44",
                                chargeback_fee=ChargebackFee(amount="0", original=None),
                                earnings="956",
                                currency_code="USD",
                                exchange_rate="1",
                            ),
                            line_items=[
                                LineItem(
                                    id="txnitm_01h7n3a7jefxzqhpaw6hdc523q",
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
                                        description=None,
                                        image_url=None,
                                        custom_data=None,
                                        status="active",
                                        id="pro_01h7mrm9f0xvrvvwvkg1b7q8e3",
                                        created_at=None,
                                        prices=None,
                                    ),
                                )
                            ],
                        ),
                        payments=[
                            {
                                "amount": "1270",
                                "status": "captured",
                                "created_at": "2023-09-04T07:58:04.656788Z",
                                "error_code": None,
                                "captured_at": "2023-09-04T07:58:12.488669Z",
                                "method_details": {
                                    "card": {
                                        "type": "visa",
                                        "last4": "5556",
                                        "expiry_year": 2024,
                                        "expiry_month": 1,
                                    },
                                    "type": "card",
                                },
                                "payment_attempt_id": "a43943e1-b0b5-4f4b-86d1-e648c183ce41",
                                "stored_payment_method_id": "a009e197-f44f-4897-886a-c48607d002dd",
                            }
                        ],
                        checkout={
                            "url": "https://webstormit.com?_ptxn=txn_01h7n3a7g7h0qr49zt9ckgketd"
                        },
                    ),
                    occurred_at=datetime.datetime(
                        2023, 9, 4, 7, 58, 14, 508687, tzinfo=datetime.timezone.utc
                    ),
                ),
                Event(
                    notification_id=None,
                    event_id="evt_01h9fjac1y4qhthy4dvzsz9407",
                    event_type="transaction.updated",
                    data=Transaction(
                        items=[
                            {
                                "price": {
                                    "id": "pri_01h81k4xtxq5atfyjdfadsavd8",
                                    "status": "active",
                                    "quantity": {"maximum": 100, "minimum": 1},
                                    "tax_mode": "account_setting",
                                    "product_id": "pro_01h81jnhdrz5wfde6cn8wg9y1y",
                                    "unit_price": {
                                        "amount": "1201",
                                        "currency_code": "USD",
                                    },
                                    "description": "Test Price Description 2",
                                    "trial_period": None,
                                    "billing_cycle": {
                                        "interval": "month",
                                        "frequency": 1,
                                    },
                                    "unit_price_overrides": [],
                                },
                                "quantity": 1,
                            }
                        ],
                        status="billed",
                        customer_id="ctm_01h8w66qa8djqjhmdkth2fnebk",
                        address_id="add_01h9fj8v8ej6cqs7v9jrabrjp5",
                        business_id="biz_01h8xg9dgqkehwp72x067vems9",
                        discount_id=None,
                        custom_data=None,
                        collection_mode="manual",
                        billing_details=BillingDetails(
                            enable_checkout=True,
                            payment_terms={"interval": "day", "frequency": 14},
                            purchase_order_number=None,
                            additional_information=None,
                        ),
                        billing_period=BillingPeriod(
                            ends_at="2023-10-04T07:43:03.848Z",
                            starts_at="2023-09-04T07:43:03.848Z",
                        ),
                        currency_code="USD",
                        customer_ip_address=None,
                        ignore_trials=None,
                        address=None,
                        id="txn_01h9fja7hy8kc43wezhzkvkqen",
                        customer=None,
                        business=None,
                        discount=None,
                        seller=None,
                        adjustments_totals=None,
                        origin="api",
                        subscription_id="sub_01h9fja8n8w8f9he3gbgy518mt",
                        invoice_id="inv_01h9fja8pnfkc0e8vpsh79y9fj",
                        invoice_number="3789-10002",
                        created_at=datetime.datetime(
                            2023, 9, 4, 7, 43, 2, 794850, tzinfo=datetime.timezone.utc
                        ),
                        updated_at=datetime.datetime(
                            2023, 9, 4, 7, 43, 7, 74603, tzinfo=datetime.timezone.utc
                        ),
                        billed_at="2023-09-04T07:43:02.718183Z",
                        details=TransactionDetails(
                            tax_rates_used=[
                                TaxRatesUsed(
                                    tax_rate="0.27",
                                    totals=TaxRatesTotals(
                                        subtotal="1201",
                                        discount="0",
                                        tax="324",
                                        total="1525",
                                    ),
                                )
                            ],
                            totals=Totals(
                                subtotal="1201",
                                discount="0",
                                tax="324",
                                total="1525",
                                credit="0",
                                balance="1525",
                                grand_total="1525",
                                fee=None,
                                earnings=None,
                                currency_code="USD",
                                exchange_rate="1",
                            ),
                            adjusted_totals=AdjustedTotals(
                                subtotal="1201",
                                tax="324",
                                total="1525",
                                grand_total="1525",
                                fee="0",
                                earnings="0",
                                currency_code="USD",
                            ),
                            payout_totals=None,
                            adjusted_payout_totals=None,
                            line_items=[
                                LineItem(
                                    id="txnitm_01h9fja7kn51ze3d859p7s2eq6",
                                    price_id="pri_01h81k4xtxq5atfyjdfadsavd8",
                                    quantity=1,
                                    proration=None,
                                    tax_rate="0.27",
                                    unit_totals=LineItemUnitTotals(
                                        subtotal="1201",
                                        discount="0",
                                        tax="324",
                                        total="1525",
                                    ),
                                    totals=LineItemTotals(
                                        subtotal="1201",
                                        discount="0",
                                        tax="324",
                                        total="1525",
                                    ),
                                    product=Product(
                                        name="Test Product New",
                                        tax_category="standard",
                                        description="Test Product Description",
                                        image_url="https://example.com/image.png",
                                        custom_data=None,
                                        status="active",
                                        id="pro_01h81jnhdrz5wfde6cn8wg9y1y",
                                        created_at=None,
                                        prices=None,
                                    ),
                                )
                            ],
                        ),
                        payments=[],
                        checkout={
                            "url": "https://webstormit.com?_ptxn=txn_01h9fja7hy8kc43wezhzkvkqen"
                        },
                    ),
                    occurred_at=datetime.datetime(
                        2023, 9, 4, 7, 43, 7, 326868, tzinfo=datetime.timezone.utc
                    ),
                ),
                Event(
                    notification_id=None,
                    event_id="evt_01h9fjaa0fszfrswes05g9sk7d",
                    event_type="transaction.updated",
                    data=Transaction(
                        items=[
                            {
                                "price": {
                                    "id": "pri_01h81k4xtxq5atfyjdfadsavd8",
                                    "status": "active",
                                    "quantity": {"maximum": 100, "minimum": 1},
                                    "tax_mode": "account_setting",
                                    "product_id": "pro_01h81jnhdrz5wfde6cn8wg9y1y",
                                    "unit_price": {
                                        "amount": "1201",
                                        "currency_code": "USD",
                                    },
                                    "description": "Test Price Description 2",
                                    "trial_period": None,
                                    "billing_cycle": {
                                        "interval": "month",
                                        "frequency": 1,
                                    },
                                    "unit_price_overrides": [],
                                },
                                "quantity": 1,
                                "proration": {
                                    "rate": "0",
                                    "billing_period": {
                                        "ends_at": "0001-01-01T00:00:00Z",
                                        "starts_at": "0001-01-01T00:00:00Z",
                                    },
                                },
                            }
                        ],
                        status="billed",
                        customer_id="ctm_01h8w66qa8djqjhmdkth2fnebk",
                        address_id="add_01h9fj8v8ej6cqs7v9jrabrjp5",
                        business_id="biz_01h8xg9dgqkehwp72x067vems9",
                        discount_id=None,
                        custom_data=None,
                        collection_mode="manual",
                        billing_details=BillingDetails(
                            enable_checkout=True,
                            payment_terms={"interval": "day", "frequency": 14},
                            purchase_order_number=None,
                            additional_information=None,
                        ),
                        billing_period=BillingPeriod(
                            ends_at="2023-10-04T07:43:03.848Z",
                            starts_at="2023-09-04T07:43:03.848Z",
                        ),
                        currency_code="USD",
                        customer_ip_address=None,
                        ignore_trials=None,
                        address=None,
                        id="txn_01h9fja7hy8kc43wezhzkvkqen",
                        customer=None,
                        business=None,
                        discount=None,
                        seller=None,
                        adjustments_totals=None,
                        origin="api",
                        subscription_id="sub_01h9fja8n8w8f9he3gbgy518mt",
                        invoice_id=None,
                        invoice_number=None,
                        created_at=datetime.datetime(
                            2023, 9, 4, 7, 43, 2, 794850, tzinfo=datetime.timezone.utc
                        ),
                        updated_at=datetime.datetime(
                            2023, 9, 4, 7, 43, 4, 972217, tzinfo=datetime.timezone.utc
                        ),
                        billed_at="2023-09-04T07:43:02.718183Z",
                        details=TransactionDetails(
                            tax_rates_used=[
                                TaxRatesUsed(
                                    tax_rate="0.27",
                                    totals=TaxRatesTotals(
                                        subtotal="1201",
                                        discount="0",
                                        tax="324",
                                        total="1525",
                                    ),
                                )
                            ],
                            totals=Totals(
                                subtotal="1201",
                                discount="0",
                                tax="324",
                                total="1525",
                                credit="0",
                                balance="1525",
                                grand_total="1525",
                                fee=None,
                                earnings=None,
                                currency_code="USD",
                                exchange_rate="1",
                            ),
                            adjusted_totals=AdjustedTotals(
                                subtotal="1201",
                                tax="324",
                                total="1525",
                                grand_total="1525",
                                fee="0",
                                earnings="0",
                                currency_code="USD",
                            ),
                            payout_totals=None,
                            adjusted_payout_totals=None,
                            line_items=[
                                LineItem(
                                    id="txnitm_01h9fja7kn51ze3d859p7s2eq6",
                                    price_id="pri_01h81k4xtxq5atfyjdfadsavd8",
                                    quantity=1,
                                    proration=LineItemProration(
                                        rate="0",
                                        billing_period=BillingPeriod(
                                            ends_at="0001-01-01T00:00:00Z",
                                            starts_at="0001-01-01T00:00:00Z",
                                        ),
                                    ),
                                    tax_rate="0.27",
                                    unit_totals=LineItemUnitTotals(
                                        subtotal="1201",
                                        discount="0",
                                        tax="324",
                                        total="1525",
                                    ),
                                    totals=LineItemTotals(
                                        subtotal="1201",
                                        discount="0",
                                        tax="324",
                                        total="1525",
                                    ),
                                    product=Product(
                                        name="Test Product New",
                                        tax_category="standard",
                                        description="Test Product Description",
                                        image_url="https://example.com/image.png",
                                        custom_data=None,
                                        status="active",
                                        id="pro_01h81jnhdrz5wfde6cn8wg9y1y",
                                        created_at=None,
                                        prices=None,
                                    ),
                                )
                            ],
                        ),
                        payments=[],
                        checkout={
                            "url": "https://webstormit.com?_ptxn=txn_01h9fja7hy8kc43wezhzkvkqen"
                        },
                    ),
                    occurred_at=datetime.datetime(
                        2023, 9, 4, 7, 43, 5, 231921, tzinfo=datetime.timezone.utc
                    ),
                ),
                Event(
                    notification_id=None,
                    event_id="evt_01h9fja9tz8wt290fzz4rtgk14",
                    event_type="subscription.created",
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
                            2023, 9, 4, 7, 43, 3, 848000, tzinfo=datetime.timezone.utc
                        ),
                        started_at=datetime.datetime(
                            2023, 9, 4, 7, 43, 3, 848000, tzinfo=datetime.timezone.utc
                        ),
                        first_billed_at=datetime.datetime(
                            2023, 9, 4, 7, 43, 3, 848000, tzinfo=datetime.timezone.utc
                        ),
                        next_billed_at=datetime.datetime(
                            2023, 10, 4, 7, 43, 3, 848000, tzinfo=datetime.timezone.utc
                        ),
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
                        scheduled_change=None,
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
                                next_billed_at=datetime.datetime(
                                    2023,
                                    10,
                                    4,
                                    7,
                                    43,
                                    3,
                                    848000,
                                    tzinfo=datetime.timezone.utc,
                                ),
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
                        transaction_id="txn_01h9fja7hy8kc43wezhzkvkqen",
                    ),
                    occurred_at=datetime.datetime(
                        2023, 9, 4, 7, 43, 5, 55474, tzinfo=datetime.timezone.utc
                    ),
                ),
                Event(
                    notification_id=None,
                    event_id="evt_01h9fja9t849ehre6ez2wv4fne",
                    event_type="subscription.activated",
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
                            2023, 9, 4, 7, 43, 3, 848000, tzinfo=datetime.timezone.utc
                        ),
                        started_at=datetime.datetime(
                            2023, 9, 4, 7, 43, 3, 848000, tzinfo=datetime.timezone.utc
                        ),
                        first_billed_at=datetime.datetime(
                            2023, 9, 4, 7, 43, 3, 848000, tzinfo=datetime.timezone.utc
                        ),
                        next_billed_at=datetime.datetime(
                            2023, 10, 4, 7, 43, 3, 848000, tzinfo=datetime.timezone.utc
                        ),
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
                        scheduled_change=None,
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
                                next_billed_at=datetime.datetime(
                                    2023,
                                    10,
                                    4,
                                    7,
                                    43,
                                    3,
                                    848000,
                                    tzinfo=datetime.timezone.utc,
                                ),
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
                        2023, 9, 4, 7, 43, 5, 32827, tzinfo=datetime.timezone.utc
                    ),
                ),
                Event(
                    notification_id=None,
                    event_id="evt_01h9fja8r624yz8d814tt1gm6s",
                    event_type="transaction.billed",
                    data=Transaction(
                        items=[
                            {
                                "price": {
                                    "id": "pri_01h81k4xtxq5atfyjdfadsavd8",
                                    "status": "active",
                                    "quantity": {"maximum": 100, "minimum": 1},
                                    "tax_mode": "account_setting",
                                    "product_id": "pro_01h81jnhdrz5wfde6cn8wg9y1y",
                                    "unit_price": {
                                        "amount": "1201",
                                        "currency_code": "USD",
                                    },
                                    "description": "Test Price Description 2",
                                    "trial_period": None,
                                    "billing_cycle": {
                                        "interval": "month",
                                        "frequency": 1,
                                    },
                                    "unit_price_overrides": [],
                                },
                                "price_id": "pri_01h81k4xtxq5atfyjdfadsavd8",
                                "quantity": 1,
                                "proration": None,
                            }
                        ],
                        status="billed",
                        customer_id="ctm_01h8w66qa8djqjhmdkth2fnebk",
                        address_id="add_01h9fj8v8ej6cqs7v9jrabrjp5",
                        business_id="biz_01h8xg9dgqkehwp72x067vems9",
                        discount_id=None,
                        custom_data=None,
                        collection_mode="manual",
                        billing_details=BillingDetails(
                            enable_checkout=True,
                            payment_terms={"interval": "day", "frequency": 14},
                            purchase_order_number=None,
                            additional_information=None,
                        ),
                        billing_period=None,
                        currency_code="USD",
                        customer_ip_address=None,
                        ignore_trials=None,
                        address=None,
                        id="txn_01h9fja7hy8kc43wezhzkvkqen",
                        customer=None,
                        business=None,
                        discount=None,
                        seller=None,
                        adjustments_totals=None,
                        origin="api",
                        subscription_id=None,
                        invoice_id=None,
                        invoice_number=None,
                        created_at=datetime.datetime(
                            2023, 9, 4, 7, 43, 2, 794850, tzinfo=datetime.timezone.utc
                        ),
                        updated_at=datetime.datetime(
                            2023, 9, 4, 7, 43, 2, 794850, tzinfo=datetime.timezone.utc
                        ),
                        billed_at="2023-09-04T07:43:02.718183659Z",
                        details=TransactionDetails(
                            tax_rates_used=[
                                TaxRatesUsed(
                                    tax_rate="0.27",
                                    totals=TaxRatesTotals(
                                        subtotal="1201",
                                        discount="0",
                                        tax="324",
                                        total="1525",
                                    ),
                                )
                            ],
                            totals=Totals(
                                subtotal="1201",
                                discount="0",
                                tax="324",
                                total="1525",
                                credit="0",
                                balance="1525",
                                grand_total="1525",
                                fee=None,
                                earnings=None,
                                currency_code="USD",
                            ),
                            adjusted_totals=None,
                            payout_totals=None,
                            adjusted_payout_totals=None,
                            line_items=[
                                LineItem(
                                    id="txnitm_01h9fja7kn51ze3d859p7s2eq6",
                                    price_id="pri_01h81k4xtxq5atfyjdfadsavd8",
                                    quantity=1,
                                    proration=None,
                                    tax_rate="0.27",
                                    unit_totals=LineItemUnitTotals(
                                        subtotal="1201",
                                        discount="0",
                                        tax="324",
                                        total="1525",
                                    ),
                                    totals=LineItemTotals(
                                        subtotal="1201",
                                        discount="0",
                                        tax="324",
                                        total="1525",
                                    ),
                                    product=Product(
                                        name="Test Product New",
                                        tax_category="standard",
                                        description="Test Product Description",
                                        image_url="https://example.com/image.png",
                                        custom_data=None,
                                        status="active",
                                        id="pro_01h81jnhdrz5wfde6cn8wg9y1y",
                                        created_at=None,
                                        prices=None,
                                    ),
                                )
                            ],
                        ),
                        payments=[],
                        checkout={
                            "url": "https://webstormit.com?_ptxn=txn_01h9fja7hy8kc43wezhzkvkqen"
                        },
                    ),
                    occurred_at=datetime.datetime(
                        2023, 9, 4, 7, 43, 3, 942510, tzinfo=datetime.timezone.utc
                    ),
                ),
                Event(
                    notification_id=None,
                    event_id="evt_01h9fja8qdwxrfnxj9e61hc937",
                    event_type="transaction.created",
                    data=Transaction(
                        items=[
                            {
                                "price": {
                                    "id": "pri_01h81k4xtxq5atfyjdfadsavd8",
                                    "status": "active",
                                    "quantity": {"maximum": 100, "minimum": 1},
                                    "tax_mode": "account_setting",
                                    "product_id": "pro_01h81jnhdrz5wfde6cn8wg9y1y",
                                    "unit_price": {
                                        "amount": "1201",
                                        "currency_code": "USD",
                                    },
                                    "description": "Test Price Description 2",
                                    "trial_period": None,
                                    "billing_cycle": {
                                        "interval": "month",
                                        "frequency": 1,
                                    },
                                    "unit_price_overrides": [],
                                },
                                "price_id": "pri_01h81k4xtxq5atfyjdfadsavd8",
                                "quantity": 1,
                                "proration": None,
                            }
                        ],
                        status="billed",
                        customer_id="ctm_01h8w66qa8djqjhmdkth2fnebk",
                        address_id="add_01h9fj8v8ej6cqs7v9jrabrjp5",
                        business_id="biz_01h8xg9dgqkehwp72x067vems9",
                        discount_id=None,
                        custom_data=None,
                        collection_mode="manual",
                        billing_details=BillingDetails(
                            enable_checkout=True,
                            payment_terms={"interval": "day", "frequency": 14},
                            purchase_order_number=None,
                            additional_information=None,
                        ),
                        billing_period=None,
                        currency_code="USD",
                        customer_ip_address=None,
                        ignore_trials=None,
                        address=None,
                        id="txn_01h9fja7hy8kc43wezhzkvkqen",
                        customer=None,
                        business=None,
                        discount=None,
                        seller=None,
                        adjustments_totals=None,
                        origin="api",
                        subscription_id=None,
                        invoice_id=None,
                        invoice_number=None,
                        created_at=datetime.datetime(
                            2023, 9, 4, 7, 43, 2, 794850, tzinfo=datetime.timezone.utc
                        ),
                        updated_at=datetime.datetime(
                            2023, 9, 4, 7, 43, 2, 794850, tzinfo=datetime.timezone.utc
                        ),
                        billed_at="2023-09-04T07:43:02.718183659Z",
                        details=TransactionDetails(
                            tax_rates_used=[
                                TaxRatesUsed(
                                    tax_rate="0.27",
                                    totals=TaxRatesTotals(
                                        subtotal="1201",
                                        discount="0",
                                        tax="324",
                                        total="1525",
                                    ),
                                )
                            ],
                            totals=Totals(
                                subtotal="1201",
                                discount="0",
                                tax="324",
                                total="1525",
                                credit="0",
                                balance="1525",
                                grand_total="1525",
                                fee=None,
                                earnings=None,
                                currency_code="USD",
                            ),
                            adjusted_totals=None,
                            payout_totals=None,
                            adjusted_payout_totals=None,
                            line_items=[
                                LineItem(
                                    id="txnitm_01h9fja7kn51ze3d859p7s2eq6",
                                    price_id="pri_01h81k4xtxq5atfyjdfadsavd8",
                                    quantity=1,
                                    proration=None,
                                    tax_rate="0.27",
                                    unit_totals=LineItemUnitTotals(
                                        subtotal="1201",
                                        discount="0",
                                        tax="324",
                                        total="1525",
                                    ),
                                    totals=LineItemTotals(
                                        subtotal="1201",
                                        discount="0",
                                        tax="324",
                                        total="1525",
                                    ),
                                    product=Product(
                                        name="Test Product New",
                                        tax_category="standard",
                                        description="Test Product Description",
                                        image_url="https://example.com/image.png",
                                        custom_data=None,
                                        status="active",
                                        id="pro_01h81jnhdrz5wfde6cn8wg9y1y",
                                        created_at=None,
                                        prices=None,
                                    ),
                                )
                            ],
                        ),
                        payments=[],
                        checkout={
                            "url": "https://webstormit.com?_ptxn=txn_01h9fja7hy8kc43wezhzkvkqen"
                        },
                    ),
                    occurred_at=datetime.datetime(
                        2023, 9, 4, 7, 43, 3, 917930, tzinfo=datetime.timezone.utc
                    ),
                ),
                Event(
                    notification_id=None,
                    event_id="evt_01h9fj9x67gfh0ctfxevkacgzj",
                    event_type="address.updated",
                    data=Address(
                        description=None,
                        first_line="ASD",
                        second_line=None,
                        city="Budapest",
                        postal_code="1035",
                        region=None,
                        country_code="HU",
                        status="active",
                        id="add_01h9fj8v8ej6cqs7v9jrabrjp5",
                        created_at=datetime.datetime(
                            2023, 9, 4, 7, 42, 17, 358000, tzinfo=datetime.timezone.utc
                        ),
                        updated_at=datetime.datetime(
                            2023, 9, 4, 7, 42, 51, 546817, tzinfo=datetime.timezone.utc
                        ),
                    ),
                    occurred_at=datetime.datetime(
                        2023, 9, 4, 7, 42, 52, 103146, tzinfo=datetime.timezone.utc
                    ),
                ),
                Event(
                    notification_id=None,
                    event_id="evt_01h9fj9ehe81rrgy8tk5tnzhs7",
                    event_type="address.updated",
                    data=Address(
                        description=None,
                        first_line="ASD",
                        second_line=None,
                        city=None,
                        postal_code="1035",
                        region=None,
                        country_code="HU",
                        status="active",
                        id="add_01h9fj8v8ej6cqs7v9jrabrjp5",
                        created_at=datetime.datetime(
                            2023, 9, 4, 7, 42, 17, 358000, tzinfo=datetime.timezone.utc
                        ),
                        updated_at=datetime.datetime(
                            2023, 9, 4, 7, 42, 35, 865342, tzinfo=datetime.timezone.utc
                        ),
                    ),
                    occurred_at=datetime.datetime(
                        2023, 9, 4, 7, 42, 37, 102697, tzinfo=datetime.timezone.utc
                    ),
                ),
                Event(
                    notification_id=None,
                    event_id="evt_01h9fj8w0kg2fbb7rw4gakz3c9",
                    event_type="address.created",
                    data=Address(
                        description=None,
                        first_line=None,
                        second_line=None,
                        city=None,
                        postal_code="1035",
                        region=None,
                        country_code="HU",
                        status="active",
                        id="add_01h9fj8v8ej6cqs7v9jrabrjp5",
                        created_at=datetime.datetime(
                            2023, 9, 4, 7, 42, 17, 358000, tzinfo=datetime.timezone.utc
                        ),
                        updated_at=datetime.datetime(
                            2023, 9, 4, 7, 42, 17, 358000, tzinfo=datetime.timezone.utc
                        ),
                    ),
                    occurred_at=datetime.datetime(
                        2023, 9, 4, 7, 42, 18, 131153, tzinfo=datetime.timezone.utc
                    ),
                ),
                Event(
                    notification_id=None,
                    event_id="evt_01h9e61zp76admfnsay0j9az19",
                    event_type="business.created",
                    data=Business(
                        name="Sample",
                        company_number=None,
                        tax_identifier=None,
                        contacts=[],
                        status="active",
                        id="biz_01h9e61yyv66813j7x1v4d2hgt",
                        created_at=datetime.datetime(
                            2023, 9, 3, 18, 49, 34, 427000, tzinfo=datetime.timezone.utc
                        ),
                        updated_at=datetime.datetime(
                            2023, 9, 3, 18, 49, 34, 427000, tzinfo=datetime.timezone.utc
                        ),
                    ),
                    occurred_at=datetime.datetime(
                        2023, 9, 3, 18, 49, 35, 175358, tzinfo=datetime.timezone.utc
                    ),
                ),
                Event(
                    notification_id=None,
                    event_id="evt_01h9e5vfrvah9g9c5y6xbcr8k6",
                    event_type="address.updated",
                    data=Address(
                        description="Head Office Updated",
                        first_line="4050 Jefferson Plaza, 41st Floor",
                        second_line=None,
                        city="New York",
                        postal_code="1035",
                        region="NY",
                        country_code="HU",
                        status="active",
                        id="add_01h8w4y9qfknzaq05xsd8eptjj",
                        created_at=datetime.datetime(
                            2023, 8, 27, 18, 43, 46, 31000, tzinfo=datetime.timezone.utc
                        ),
                        updated_at=datetime.datetime(
                            2023, 9, 3, 18, 46, 1, 804652, tzinfo=datetime.timezone.utc
                        ),
                    ),
                    occurred_at=datetime.datetime(
                        2023, 9, 3, 18, 46, 2, 267387, tzinfo=datetime.timezone.utc
                    ),
                ),
                Event(
                    notification_id=None,
                    event_id="evt_01h9e5ts5y0epk34y16t4hebst",
                    event_type="address.updated",
                    data=Address(
                        description=None,
                        first_line=None,
                        second_line=None,
                        city=None,
                        postal_code="1035",
                        region=None,
                        country_code="HU",
                        status="archived",
                        id="add_01h9e5s7gettzsm73v46sa1vy1",
                        created_at=datetime.datetime(
                            2023, 9, 3, 18, 44, 48, 270000, tzinfo=datetime.timezone.utc
                        ),
                        updated_at=datetime.datetime(
                            2023, 9, 3, 18, 45, 37, 925898, tzinfo=datetime.timezone.utc
                        ),
                    ),
                    occurred_at=datetime.datetime(
                        2023, 9, 3, 18, 45, 39, 134606, tzinfo=datetime.timezone.utc
                    ),
                ),
                Event(
                    notification_id=None,
                    event_id="evt_01h9e5s8f139vzhxtmz5k7g36m",
                    event_type="address.created",
                    data=Address(
                        description=None,
                        first_line=None,
                        second_line=None,
                        city=None,
                        postal_code="1035",
                        region=None,
                        country_code="HU",
                        status="active",
                        id="add_01h9e5s7gettzsm73v46sa1vy1",
                        created_at=datetime.datetime(
                            2023, 9, 3, 18, 44, 48, 270000, tzinfo=datetime.timezone.utc
                        ),
                        updated_at=datetime.datetime(
                            2023, 9, 3, 18, 44, 48, 270000, tzinfo=datetime.timezone.utc
                        ),
                    ),
                    occurred_at=datetime.datetime(
                        2023, 9, 3, 18, 44, 49, 249742, tzinfo=datetime.timezone.utc
                    ),
                ),
                Event(
                    notification_id=None,
                    event_id="evt_01h93ydrtpejggmv2t5yh9x0be",
                    event_type="transaction.updated",
                    data=Transaction(
                        items=[
                            {
                                "price": {
                                    "id": "pri_01h8xce4x86pq3byesf71a7kw1",
                                    "status": "active",
                                    "quantity": {"maximum": 100, "minimum": 1},
                                    "tax_mode": "account_setting",
                                    "product_id": "pro_01h89b2j66qq82x6vn5d39c4av",
                                    "unit_price": {
                                        "amount": "1200",
                                        "currency_code": "USD",
                                    },
                                    "description": "Test Price Updated",
                                    "trial_period": None,
                                    "billing_cycle": {
                                        "interval": "month",
                                        "frequency": 1,
                                    },
                                    "unit_price_overrides": [],
                                },
                                "quantity": 2,
                            },
                            {
                                "price": {
                                    "id": "pri_01h81k4cdv2rygh4gccf864cy9",
                                    "status": "active",
                                    "quantity": {"maximum": 100, "minimum": 1},
                                    "tax_mode": "account_setting",
                                    "product_id": "pro_01h81jnhdrz5wfde6cn8wg9y1y",
                                    "unit_price": {
                                        "amount": "1200",
                                        "currency_code": "USD",
                                    },
                                    "description": "Test Price Description",
                                    "trial_period": None,
                                    "billing_cycle": {
                                        "interval": "month",
                                        "frequency": 1,
                                    },
                                    "unit_price_overrides": [],
                                },
                                "quantity": 2,
                            },
                        ],
                        status="draft",
                        customer_id="ctm_01h7n2fwfhctkfja2dwq2cmx8v",
                        address_id=None,
                        business_id=None,
                        discount_id=None,
                        custom_data={"foo": "bar"},
                        collection_mode="automatic",
                        billing_details=None,
                        billing_period=None,
                        currency_code="USD",
                        customer_ip_address=None,
                        ignore_trials=None,
                        address=None,
                        id="txn_01h93v9qra13qbnagfqqddbrqd",
                        customer=None,
                        business=None,
                        discount=None,
                        seller=None,
                        adjustments_totals=None,
                        origin="api",
                        subscription_id=None,
                        invoice_id=None,
                        invoice_number=None,
                        created_at=datetime.datetime(
                            2023,
                            8,
                            30,
                            18,
                            29,
                            10,
                            576558,
                            tzinfo=datetime.timezone.utc,
                        ),
                        updated_at=datetime.datetime(
                            2023, 8, 30, 19, 23, 48, 77844, tzinfo=datetime.timezone.utc
                        ),
                        billed_at=None,
                        details=TransactionDetails(
                            tax_rates_used=[
                                TaxRatesUsed(
                                    tax_rate="0",
                                    totals=TaxRatesTotals(
                                        subtotal="4800",
                                        discount="0",
                                        tax="0",
                                        total="4800",
                                    ),
                                )
                            ],
                            totals=Totals(
                                subtotal="4800",
                                discount="0",
                                tax="0",
                                total="4800",
                                credit="0",
                                balance="4800",
                                grand_total="4800",
                                fee=None,
                                earnings=None,
                                currency_code="USD",
                                exchange_rate="1",
                            ),
                            adjusted_totals=AdjustedTotals(
                                subtotal="4800",
                                tax="0",
                                total="4800",
                                grand_total="4800",
                                fee="0",
                                earnings="0",
                                currency_code="USD",
                            ),
                            payout_totals=None,
                            adjusted_payout_totals=None,
                            line_items=[
                                LineItem(
                                    id="txnitm_01h93ydrf57ybq9sh9rj07d6z9",
                                    price_id="pri_01h8xce4x86pq3byesf71a7kw1",
                                    quantity=2,
                                    proration=None,
                                    tax_rate="0",
                                    unit_totals=LineItemUnitTotals(
                                        subtotal="1200",
                                        discount="0",
                                        tax="0",
                                        total="1200",
                                    ),
                                    totals=LineItemTotals(
                                        subtotal="2400",
                                        discount="0",
                                        tax="0",
                                        total="2400",
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
                                ),
                                LineItem(
                                    id="txnitm_01h93ydrf57ybq9sh9rmfhhx21",
                                    price_id="pri_01h81k4cdv2rygh4gccf864cy9",
                                    quantity=2,
                                    proration=None,
                                    tax_rate="0",
                                    unit_totals=LineItemUnitTotals(
                                        subtotal="1200",
                                        discount="0",
                                        tax="0",
                                        total="1200",
                                    ),
                                    totals=LineItemTotals(
                                        subtotal="2400",
                                        discount="0",
                                        tax="0",
                                        total="2400",
                                    ),
                                    product=Product(
                                        name="Test Product New",
                                        tax_category="standard",
                                        description="Test Product Description",
                                        image_url="https://example.com/image.png",
                                        custom_data=None,
                                        status="active",
                                        id="pro_01h81jnhdrz5wfde6cn8wg9y1y",
                                        created_at=None,
                                        prices=None,
                                    ),
                                ),
                            ],
                        ),
                        payments=[],
                        checkout={
                            "url": "https://webstormit.com?_ptxn=txn_01h93v9qra13qbnagfqqddbrqd"
                        },
                    ),
                    occurred_at=datetime.datetime(
                        2023, 8, 30, 19, 23, 48, 438396, tzinfo=datetime.timezone.utc
                    ),
                ),
                Event(
                    notification_id=None,
                    event_id="evt_01h93xkm7jdq2s4qyf6mt4rmjz",
                    event_type="transaction.updated",
                    data=Transaction(
                        items=[
                            {
                                "price": {
                                    "id": "pri_01h8xce4x86pq3byesf71a7kw1",
                                    "status": "active",
                                    "quantity": {"maximum": 100, "minimum": 1},
                                    "tax_mode": "account_setting",
                                    "product_id": "pro_01h89b2j66qq82x6vn5d39c4av",
                                    "unit_price": {
                                        "amount": "1200",
                                        "currency_code": "USD",
                                    },
                                    "description": "Test Price Updated",
                                    "trial_period": None,
                                    "billing_cycle": {
                                        "interval": "month",
                                        "frequency": 1,
                                    },
                                    "unit_price_overrides": [],
                                },
                                "quantity": 2,
                            },
                            {
                                "price": {
                                    "id": "pri_01h81k4cdv2rygh4gccf864cy9",
                                    "status": "active",
                                    "quantity": {"maximum": 100, "minimum": 1},
                                    "tax_mode": "account_setting",
                                    "product_id": "pro_01h81jnhdrz5wfde6cn8wg9y1y",
                                    "unit_price": {
                                        "amount": "1200",
                                        "currency_code": "USD",
                                    },
                                    "description": "Test Price Description",
                                    "trial_period": None,
                                    "billing_cycle": {
                                        "interval": "month",
                                        "frequency": 1,
                                    },
                                    "unit_price_overrides": [],
                                },
                                "quantity": 2,
                            },
                        ],
                        status="draft",
                        customer_id="ctm_01h7n2fwfhctkfja2dwq2cmx8v",
                        address_id=None,
                        business_id=None,
                        discount_id=None,
                        custom_data={"foo": "bar"},
                        collection_mode="automatic",
                        billing_details=None,
                        billing_period=None,
                        currency_code="USD",
                        customer_ip_address=None,
                        ignore_trials=None,
                        address=None,
                        id="txn_01h93v9qra13qbnagfqqddbrqd",
                        customer=None,
                        business=None,
                        discount=None,
                        seller=None,
                        adjustments_totals=None,
                        origin="api",
                        subscription_id=None,
                        invoice_id=None,
                        invoice_number=None,
                        created_at=datetime.datetime(
                            2023,
                            8,
                            30,
                            18,
                            29,
                            10,
                            576558,
                            tzinfo=datetime.timezone.utc,
                        ),
                        updated_at=datetime.datetime(
                            2023, 8, 30, 19, 9, 31, 443529, tzinfo=datetime.timezone.utc
                        ),
                        billed_at=None,
                        details=TransactionDetails(
                            tax_rates_used=[
                                TaxRatesUsed(
                                    tax_rate="0",
                                    totals=TaxRatesTotals(
                                        subtotal="4800",
                                        discount="0",
                                        tax="0",
                                        total="4800",
                                    ),
                                )
                            ],
                            totals=Totals(
                                subtotal="4800",
                                discount="0",
                                tax="0",
                                total="4800",
                                credit="0",
                                balance="4800",
                                grand_total="4800",
                                fee=None,
                                earnings=None,
                                currency_code="USD",
                                exchange_rate="1",
                            ),
                            adjusted_totals=AdjustedTotals(
                                subtotal="4800",
                                tax="0",
                                total="4800",
                                grand_total="4800",
                                fee="0",
                                earnings="0",
                                currency_code="USD",
                            ),
                            payout_totals=None,
                            adjusted_payout_totals=None,
                            line_items=[
                                LineItem(
                                    id="txnitm_01h93xkkxas81feqmgwkq3ycrv",
                                    price_id="pri_01h8xce4x86pq3byesf71a7kw1",
                                    quantity=2,
                                    proration=None,
                                    tax_rate="0",
                                    unit_totals=LineItemUnitTotals(
                                        subtotal="1200",
                                        discount="0",
                                        tax="0",
                                        total="1200",
                                    ),
                                    totals=LineItemTotals(
                                        subtotal="2400",
                                        discount="0",
                                        tax="0",
                                        total="2400",
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
                                ),
                                LineItem(
                                    id="txnitm_01h93xkkxas81feqmgwpyrg8vg",
                                    price_id="pri_01h81k4cdv2rygh4gccf864cy9",
                                    quantity=2,
                                    proration=None,
                                    tax_rate="0",
                                    unit_totals=LineItemUnitTotals(
                                        subtotal="1200",
                                        discount="0",
                                        tax="0",
                                        total="1200",
                                    ),
                                    totals=LineItemTotals(
                                        subtotal="2400",
                                        discount="0",
                                        tax="0",
                                        total="2400",
                                    ),
                                    product=Product(
                                        name="Test Product New",
                                        tax_category="standard",
                                        description="Test Product Description",
                                        image_url="https://example.com/image.png",
                                        custom_data=None,
                                        status="active",
                                        id="pro_01h81jnhdrz5wfde6cn8wg9y1y",
                                        created_at=None,
                                        prices=None,
                                    ),
                                ),
                            ],
                        ),
                        payments=[],
                        checkout={
                            "url": "https://webstormit.com?_ptxn=txn_01h93v9qra13qbnagfqqddbrqd"
                        },
                    ),
                    occurred_at=datetime.datetime(
                        2023, 8, 30, 19, 9, 31, 762403, tzinfo=datetime.timezone.utc
                    ),
                ),
                Event(
                    notification_id=None,
                    event_id="evt_01h93x593yfay3xg0jt1zn9hqd",
                    event_type="transaction.updated",
                    data=Transaction(
                        items=[
                            {
                                "price": {
                                    "id": "pri_01h8xce4x86pq3byesf71a7kw1",
                                    "status": "active",
                                    "quantity": {"maximum": 100, "minimum": 1},
                                    "tax_mode": "account_setting",
                                    "product_id": "pro_01h89b2j66qq82x6vn5d39c4av",
                                    "unit_price": {
                                        "amount": "1200",
                                        "currency_code": "USD",
                                    },
                                    "description": "Test Price Updated",
                                    "trial_period": None,
                                    "billing_cycle": {
                                        "interval": "month",
                                        "frequency": 1,
                                    },
                                    "unit_price_overrides": [],
                                },
                                "quantity": 2,
                            },
                            {
                                "price": {
                                    "id": "pri_01h81k4cdv2rygh4gccf864cy9",
                                    "status": "active",
                                    "quantity": {"maximum": 100, "minimum": 1},
                                    "tax_mode": "account_setting",
                                    "product_id": "pro_01h81jnhdrz5wfde6cn8wg9y1y",
                                    "unit_price": {
                                        "amount": "1200",
                                        "currency_code": "USD",
                                    },
                                    "description": "Test Price Description",
                                    "trial_period": None,
                                    "billing_cycle": {
                                        "interval": "month",
                                        "frequency": 1,
                                    },
                                    "unit_price_overrides": [],
                                },
                                "quantity": 2,
                            },
                        ],
                        status="draft",
                        customer_id="ctm_01h7n2fwfhctkfja2dwq2cmx8v",
                        address_id=None,
                        business_id=None,
                        discount_id=None,
                        custom_data={"foo": "bar"},
                        collection_mode="automatic",
                        billing_details=None,
                        billing_period=None,
                        currency_code="USD",
                        customer_ip_address=None,
                        ignore_trials=None,
                        address=None,
                        id="txn_01h93v9qra13qbnagfqqddbrqd",
                        customer=None,
                        business=None,
                        discount=None,
                        seller=None,
                        adjustments_totals=None,
                        origin="api",
                        subscription_id=None,
                        invoice_id=None,
                        invoice_number=None,
                        created_at=datetime.datetime(
                            2023,
                            8,
                            30,
                            18,
                            29,
                            10,
                            576558,
                            tzinfo=datetime.timezone.utc,
                        ),
                        updated_at=datetime.datetime(
                            2023, 8, 30, 19, 1, 41, 142119, tzinfo=datetime.timezone.utc
                        ),
                        billed_at=None,
                        details=TransactionDetails(
                            tax_rates_used=[
                                TaxRatesUsed(
                                    tax_rate="0",
                                    totals=TaxRatesTotals(
                                        subtotal="4800",
                                        discount="0",
                                        tax="0",
                                        total="4800",
                                    ),
                                )
                            ],
                            totals=Totals(
                                subtotal="4800",
                                discount="0",
                                tax="0",
                                total="4800",
                                credit="0",
                                balance="4800",
                                grand_total="4800",
                                fee=None,
                                earnings=None,
                                currency_code="USD",
                                exchange_rate="1",
                            ),
                            adjusted_totals=AdjustedTotals(
                                subtotal="4800",
                                tax="0",
                                total="4800",
                                grand_total="4800",
                                fee="0",
                                earnings="0",
                                currency_code="USD",
                            ),
                            payout_totals=None,
                            adjusted_payout_totals=None,
                            line_items=[
                                LineItem(
                                    id="txnitm_01h93x58mdt95q006vh0ab296j",
                                    price_id="pri_01h8xce4x86pq3byesf71a7kw1",
                                    quantity=2,
                                    proration=None,
                                    tax_rate="0",
                                    unit_totals=LineItemUnitTotals(
                                        subtotal="1200",
                                        discount="0",
                                        tax="0",
                                        total="1200",
                                    ),
                                    totals=LineItemTotals(
                                        subtotal="2400",
                                        discount="0",
                                        tax="0",
                                        total="2400",
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
                                ),
                                LineItem(
                                    id="txnitm_01h93x58mdt95q006vh3nzw6jn",
                                    price_id="pri_01h81k4cdv2rygh4gccf864cy9",
                                    quantity=2,
                                    proration=None,
                                    tax_rate="0",
                                    unit_totals=LineItemUnitTotals(
                                        subtotal="1200",
                                        discount="0",
                                        tax="0",
                                        total="1200",
                                    ),
                                    totals=LineItemTotals(
                                        subtotal="2400",
                                        discount="0",
                                        tax="0",
                                        total="2400",
                                    ),
                                    product=Product(
                                        name="Test Product New",
                                        tax_category="standard",
                                        description="Test Product Description",
                                        image_url="https://example.com/image.png",
                                        custom_data=None,
                                        status="active",
                                        id="pro_01h81jnhdrz5wfde6cn8wg9y1y",
                                        created_at=None,
                                        prices=None,
                                    ),
                                ),
                            ],
                        ),
                        payments=[],
                        checkout={
                            "url": "https://webstormit.com?_ptxn=txn_01h93v9qra13qbnagfqqddbrqd"
                        },
                    ),
                    occurred_at=datetime.datetime(
                        2023, 8, 30, 19, 1, 41, 630648, tzinfo=datetime.timezone.utc
                    ),
                ),
                Event(
                    notification_id=None,
                    event_id="evt_01h93v9rh66f6bzsvft2kr4qxw",
                    event_type="transaction.created",
                    data=Transaction(
                        items=[
                            {
                                "price": {
                                    "id": "pri_01h8xce4x86pq3byesf71a7kw1",
                                    "status": "active",
                                    "quantity": {"maximum": 100, "minimum": 1},
                                    "tax_mode": "account_setting",
                                    "product_id": "pro_01h89b2j66qq82x6vn5d39c4av",
                                    "unit_price": {
                                        "amount": "1200",
                                        "currency_code": "USD",
                                    },
                                    "description": "Test Price Updated",
                                    "trial_period": None,
                                    "billing_cycle": {
                                        "interval": "month",
                                        "frequency": 1,
                                    },
                                    "unit_price_overrides": [],
                                },
                                "price_id": "pri_01h8xce4x86pq3byesf71a7kw1",
                                "quantity": 2,
                                "proration": None,
                            },
                            {
                                "price": {
                                    "id": "pri_01h81k4cdv2rygh4gccf864cy9",
                                    "status": "active",
                                    "quantity": {"maximum": 100, "minimum": 1},
                                    "tax_mode": "account_setting",
                                    "product_id": "pro_01h81jnhdrz5wfde6cn8wg9y1y",
                                    "unit_price": {
                                        "amount": "1200",
                                        "currency_code": "USD",
                                    },
                                    "description": "Test Price Description",
                                    "trial_period": None,
                                    "billing_cycle": {
                                        "interval": "month",
                                        "frequency": 1,
                                    },
                                    "unit_price_overrides": [],
                                },
                                "price_id": "pri_01h81k4cdv2rygh4gccf864cy9",
                                "quantity": 1,
                                "proration": None,
                            },
                        ],
                        status="draft",
                        customer_id="ctm_01h7n2fwfhctkfja2dwq2cmx8v",
                        address_id=None,
                        business_id=None,
                        discount_id=None,
                        custom_data={"foo": "bar"},
                        collection_mode="automatic",
                        billing_details=None,
                        billing_period=None,
                        currency_code="USD",
                        customer_ip_address=None,
                        ignore_trials=None,
                        address=None,
                        id="txn_01h93v9qra13qbnagfqqddbrqd",
                        customer=None,
                        business=None,
                        discount=None,
                        seller=None,
                        adjustments_totals=None,
                        origin="api",
                        subscription_id=None,
                        invoice_id=None,
                        invoice_number=None,
                        created_at=datetime.datetime(
                            2023,
                            8,
                            30,
                            18,
                            29,
                            10,
                            576558,
                            tzinfo=datetime.timezone.utc,
                        ),
                        updated_at=datetime.datetime(
                            2023,
                            8,
                            30,
                            18,
                            29,
                            10,
                            576558,
                            tzinfo=datetime.timezone.utc,
                        ),
                        billed_at=None,
                        details=TransactionDetails(
                            tax_rates_used=[
                                TaxRatesUsed(
                                    tax_rate="0",
                                    totals=TaxRatesTotals(
                                        subtotal="3600",
                                        discount="0",
                                        tax="0",
                                        total="3600",
                                    ),
                                )
                            ],
                            totals=Totals(
                                subtotal="3600",
                                discount="0",
                                tax="0",
                                total="3600",
                                credit="0",
                                balance="3600",
                                grand_total="3600",
                                fee=None,
                                earnings=None,
                                currency_code="USD",
                            ),
                            adjusted_totals=None,
                            payout_totals=None,
                            adjusted_payout_totals=None,
                            line_items=[
                                LineItem(
                                    id="txnitm_01h93v9qs1w9pkah6ren6hxd0d",
                                    price_id="pri_01h8xce4x86pq3byesf71a7kw1",
                                    quantity=2,
                                    proration=None,
                                    tax_rate="0",
                                    unit_totals=LineItemUnitTotals(
                                        subtotal="1200",
                                        discount="0",
                                        tax="0",
                                        total="1200",
                                    ),
                                    totals=LineItemTotals(
                                        subtotal="2400",
                                        discount="0",
                                        tax="0",
                                        total="2400",
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
                                ),
                                LineItem(
                                    id="txnitm_01h93v9qs1w9pkah6rer2n4exy",
                                    price_id="pri_01h81k4cdv2rygh4gccf864cy9",
                                    quantity=1,
                                    proration=None,
                                    tax_rate="0",
                                    unit_totals=LineItemUnitTotals(
                                        subtotal="1200",
                                        discount="0",
                                        tax="0",
                                        total="1200",
                                    ),
                                    totals=LineItemTotals(
                                        subtotal="1200",
                                        discount="0",
                                        tax="0",
                                        total="1200",
                                    ),
                                    product=Product(
                                        name="Test Product New",
                                        tax_category="standard",
                                        description="Test Product Description",
                                        image_url="https://example.com/image.png",
                                        custom_data=None,
                                        status="active",
                                        id="pro_01h81jnhdrz5wfde6cn8wg9y1y",
                                        created_at=None,
                                        prices=None,
                                    ),
                                ),
                            ],
                        ),
                        payments=[],
                        checkout={
                            "url": "https://webstormit.com?_ptxn=txn_01h93v9qra13qbnagfqqddbrqd"
                        },
                    ),
                    occurred_at=datetime.datetime(
                        2023, 8, 30, 18, 29, 11, 334779, tzinfo=datetime.timezone.utc
                    ),
                ),
                Event(
                    notification_id=None,
                    event_id="evt_01h8xgkp7g926qzv0zkqdv53fy",
                    event_type="business.updated",
                    data=Business(
                        name="Test Business 2",
                        company_number="123456789",
                        tax_identifier="123456789",
                        contacts=[Contact(name="Test Contact", email="asd@asd.com")],
                        status="active",
                        id="biz_01h8xg9dgqkehwp72x067vems9",
                        created_at=datetime.datetime(
                            2023, 8, 28, 7, 21, 19, 127000, tzinfo=datetime.timezone.utc
                        ),
                        updated_at=datetime.datetime(
                            2023, 8, 28, 7, 26, 54, 983533, tzinfo=datetime.timezone.utc
                        ),
                    ),
                    occurred_at=datetime.datetime(
                        2023, 8, 28, 7, 26, 55, 728359, tzinfo=datetime.timezone.utc
                    ),
                ),
                Event(
                    notification_id=None,
                    event_id="evt_01h8xg9e4cphddcgb537kf9gab",
                    event_type="business.created",
                    data=Business(
                        name="Test Business",
                        company_number="123456789",
                        tax_identifier="123456789",
                        contacts=[Contact(name="Test Contact", email="asd@asd.com")],
                        status="active",
                        id="biz_01h8xg9dgqkehwp72x067vems9",
                        created_at=datetime.datetime(
                            2023, 8, 28, 7, 21, 19, 127000, tzinfo=datetime.timezone.utc
                        ),
                        updated_at=datetime.datetime(
                            2023, 8, 28, 7, 21, 19, 127000, tzinfo=datetime.timezone.utc
                        ),
                    ),
                    occurred_at=datetime.datetime(
                        2023, 8, 28, 7, 21, 19, 756162, tzinfo=datetime.timezone.utc
                    ),
                ),
                Event(
                    notification_id=None,
                    event_id="evt_01h8xd3gzxmzv9hww37wpsvzm3",
                    event_type="price.updated",
                    data=Price(
                        description="Test Price Updated",
                        product_id="pro_01h89b2j66qq82x6vn5d39c4av",
                        billing_cycle=BillingCycle(interval="month", frequency=1),
                        trial_period=None,
                        tax_mode="account_setting",
                        unit_price_overrides=[],
                        quantity=Quantity(minimum=1, maximum=100),
                        custom_data=None,
                        id="pri_01h8xce4x86pq3byesf71a7kw1",
                        unit_price=UnitPrice(amount="1200", currency_code="USD"),
                        status="active",
                    ),
                    occurred_at=datetime.datetime(
                        2023, 8, 28, 6, 25, 40, 349559, tzinfo=datetime.timezone.utc
                    ),
                ),
                Event(
                    notification_id=None,
                    event_id="evt_01h8xd26k0k112vksbe7mvayy4",
                    event_type="price.updated",
                    data=Price(
                        description="Test Price Updated",
                        product_id="pro_01h89b2j66qq82x6vn5d39c4av",
                        billing_cycle=BillingCycle(interval="month", frequency=1),
                        trial_period=None,
                        tax_mode="account_setting",
                        unit_price_overrides=[],
                        quantity=Quantity(minimum=1, maximum=100),
                        custom_data=None,
                        id="pri_01h8xce4x86pq3byesf71a7kw1",
                        unit_price=UnitPrice(amount="1000", currency_code="USD"),
                        status="active",
                    ),
                    occurred_at=datetime.datetime(
                        2023, 8, 28, 6, 24, 56, 929038, tzinfo=datetime.timezone.utc
                    ),
                ),
                Event(
                    notification_id=None,
                    event_id="evt_01h8xce59ake6mgnv74yrkd4vb",
                    event_type="price.created",
                    data=Price(
                        description="Test Price",
                        product_id="pro_01h89b2j66qq82x6vn5d39c4av",
                        billing_cycle=BillingCycle(interval="month", frequency=1),
                        trial_period=None,
                        tax_mode="account_setting",
                        unit_price_overrides=[],
                        quantity=Quantity(minimum=1, maximum=100),
                        custom_data=None,
                        id="pri_01h8xce4x86pq3byesf71a7kw1",
                        unit_price=UnitPrice(amount="1000", currency_code="USD"),
                        status="active",
                    ),
                    occurred_at=datetime.datetime(
                        2023, 8, 28, 6, 14, 0, 234382, tzinfo=datetime.timezone.utc
                    ),
                ),
                Event(
                    notification_id=None,
                    event_id="evt_01h8w6jhg253gkkvv55d5ref1v",
                    event_type="customer.updated",
                    data=Customer(
                        email="asd123@asd.com",
                        name="Test Customer 2",
                        locale="en",
                        id="ctm_01h8w66qa8djqjhmdkth2fnebk",
                        marketing_consent=False,
                        created_at=datetime.datetime(
                            2023, 8, 27, 19, 5, 50, 664000, tzinfo=datetime.timezone.utc
                        ),
                        updated_at=datetime.datetime(
                            2023,
                            8,
                            27,
                            19,
                            12,
                            16,
                            802971,
                            tzinfo=datetime.timezone.utc,
                        ),
                        imported_at=None,
                        source=None,
                        status="active",
                        is_sanctioned=None,
                        tax_exemptions=None,
                    ),
                    occurred_at=datetime.datetime(
                        2023, 8, 27, 19, 12, 17, 922591, tzinfo=datetime.timezone.utc
                    ),
                ),
                Event(
                    notification_id=None,
                    event_id="evt_01h8w66re7qwzrwtx08nv9x2rn",
                    event_type="customer.created",
                    data=Customer(
                        email="asd1234@asd.com",
                        name="Test Customer",
                        locale="en",
                        id="ctm_01h8w66qa8djqjhmdkth2fnebk",
                        marketing_consent=False,
                        created_at=datetime.datetime(
                            2023, 8, 27, 19, 5, 50, 664000, tzinfo=datetime.timezone.utc
                        ),
                        updated_at=datetime.datetime(
                            2023, 8, 27, 19, 5, 50, 664000, tzinfo=datetime.timezone.utc
                        ),
                        imported_at=None,
                        source=None,
                        status="active",
                        is_sanctioned=None,
                        tax_exemptions=None,
                    ),
                    occurred_at=datetime.datetime(
                        2023, 8, 27, 19, 5, 51, 815366, tzinfo=datetime.timezone.utc
                    ),
                ),
                Event(
                    notification_id=None,
                    event_id="evt_01h8w5a7ayv9t9jvpjxyz1q2v4",
                    event_type="address.updated",
                    data=Address(
                        description="Head Office Updated",
                        first_line="4050 Jefferson Plaza, 41st Floor",
                        second_line=None,
                        city="New York",
                        postal_code="10021",
                        region="NY",
                        country_code="US",
                        status="active",
                        id="add_01h8w4y9qfknzaq05xsd8eptjj",
                        created_at=datetime.datetime(
                            2023, 8, 27, 18, 43, 46, 31000, tzinfo=datetime.timezone.utc
                        ),
                        updated_at=datetime.datetime(
                            2023,
                            8,
                            27,
                            18,
                            50,
                            16,
                            328439,
                            tzinfo=datetime.timezone.utc,
                        ),
                    ),
                    occurred_at=datetime.datetime(
                        2023, 8, 27, 18, 50, 16, 798990, tzinfo=datetime.timezone.utc
                    ),
                ),
                Event(
                    notification_id=None,
                    event_id="evt_01h8w4yagksh4v51jhwkjesama",
                    event_type="address.created",
                    data=Address(
                        description="Head Office",
                        first_line="4050 Jefferson Plaza, 41st Floor",
                        second_line=None,
                        city="New York",
                        postal_code="10021",
                        region="NY",
                        country_code="US",
                        status="active",
                        id="add_01h8w4y9qfknzaq05xsd8eptjj",
                        created_at=datetime.datetime(
                            2023, 8, 27, 18, 43, 46, 31000, tzinfo=datetime.timezone.utc
                        ),
                        updated_at=datetime.datetime(
                            2023, 8, 27, 18, 43, 46, 31000, tzinfo=datetime.timezone.utc
                        ),
                    ),
                    occurred_at=datetime.datetime(
                        2023, 8, 27, 18, 43, 46, 835595, tzinfo=datetime.timezone.utc
                    ),
                ),
            ],
            meta=dict(
                request_id="e3e16e23-fbc9-4ccd-b5da-0a1f82027d38",
                pagination=dict(
                    per_page=50,
                    estimated_total=88,
                    next="http://sandbox-api.paddle.com/events?after=evt_01h8w4yagksh4v51jhwkjesama",
                    has_more=True,
                ),
            ),
        )

        assert deepdiff.DeepDiff(events, expected_events, ignore_order=True) == {}
