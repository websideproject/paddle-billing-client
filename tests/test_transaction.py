import os
from datetime import datetime

import deepdiff
import pytest
from apiclient import HeaderAuthentication

from paddle_billing_client.models.customer import Customer
from paddle_billing_client.models.transaction import (
    AdjustedTotals,
    LineItem,
    Transaction,
    TransactionDetails,
    TransactionPreview,
    TransactionPreviewResponse,
    TransactionQueryParams,
    TransactionRequest,
    TransactionResponse,
    TransactionsResponse,
)


class TestTransaction:
    def setup_class(self):
        from paddle_billing_client.client import PaddleApiClient  # pragma: no cover

        self.client = PaddleApiClient(
            authentication_method=HeaderAuthentication(
                token=os.getenv("PADDLE_SANDBOX_AUTH_TOKEN")
            ),
        )

    @pytest.mark.vcr
    def test_create_transaction(self):
        transaction = self.client.create_transaction(
            TransactionRequest(
                items=[
                    {
                        "price_id": "pri_01h8xce4x86pq3byesf71a7kw1",
                        "quantity": 2,
                    },
                    {
                        "price_id": "pri_01h81k4cdv2rygh4gccf864cy9",
                        "quantity": 1,
                    },
                ],
                customer_id="ctm_01h7n2fwfhctkfja2dwq2cmx8v",
                custom_data={"foo": "bar"},
                collection_mode="automatic",
                currency_code="USD",
            ),
        )
        expected_transaction = TransactionResponse(
            data=Transaction(
                id="txn_01h93v9qra13qbnagfqqddbrqd",
                status="draft",
                customer_id="ctm_01h7n2fwfhctkfja2dwq2cmx8v",
                address_id=None,
                business_id=None,
                custom_data={"foo": "bar"},
                origin="api",
                collection_mode="automatic",
                subscription_id=None,
                invoice_id=None,
                invoice_number=None,
                billing_details=None,
                billing_period=None,
                currency_code="USD",
                discount_id=None,
                created_at="2023-08-30T18:29:10.576558762Z",
                updated_at="2023-08-30T18:29:10.576558762Z",
                billed_at=None,
                payments=[],
                checkout={
                    "url": "https://webstormit.com?_ptxn=txn_01h93v9qra13qbnagfqqddbrqd"
                },
                details={
                    "tax_rates_used": [
                        {
                            "tax_rate": "0",
                            "totals": {
                                "subtotal": "3600",
                                "discount": "0",
                                "tax": "0",
                                "total": "3600",
                            },
                        }
                    ],
                    "totals": {
                        "subtotal": "3600",
                        "tax": "0",
                        "discount": "0",
                        "total": "3600",
                        "grand_total": "3600",
                        "fee": None,
                        "credit": "0",
                        "balance": "3600",
                        "earnings": None,
                        "currency_code": "USD",
                    },
                    "adjusted_totals": {
                        "subtotal": "3600",
                        "tax": "0",
                        "total": "3600",
                        "grand_total": "3600",
                        "fee": "0",
                        "earnings": "0",
                        "currency_code": "USD",
                    },
                    "payout_totals": None,
                    "adjusted_payout_totals": None,
                    "line_items": [
                        {
                            "id": "txnitm_01h93v9qs1w9pkah6ren6hxd0d",
                            "price_id": "pri_01h8xce4x86pq3byesf71a7kw1",
                            "quantity": 2,
                            "totals": {
                                "subtotal": "2400",
                                "tax": "0",
                                "discount": "0",
                                "total": "2400",
                            },
                            "product": {
                                "id": "pro_01h89b2j66qq82x6vn5d39c4av",
                                "name": "Test Product New 2",
                                "description": "Test Product Description",
                                "tax_category": "standard",
                                "image_url": "https://example.com/image.png",
                                "status": "active",
                            },
                            "tax_rate": "0",
                            "unit_totals": {
                                "subtotal": "1200",
                                "tax": "0",
                                "discount": "0",
                                "total": "1200",
                            },
                        },
                        {
                            "id": "txnitm_01h93v9qs1w9pkah6rer2n4exy",
                            "price_id": "pri_01h81k4cdv2rygh4gccf864cy9",
                            "quantity": 1,
                            "totals": {
                                "subtotal": "1200",
                                "tax": "0",
                                "discount": "0",
                                "total": "1200",
                            },
                            "product": {
                                "id": "pro_01h81jnhdrz5wfde6cn8wg9y1y",
                                "name": "Test Product New",
                                "description": "Test Product Description",
                                "tax_category": "standard",
                                "image_url": "https://example.com/image.png",
                                "status": "active",
                            },
                            "tax_rate": "0",
                            "unit_totals": {
                                "subtotal": "1200",
                                "tax": "0",
                                "discount": "0",
                                "total": "1200",
                            },
                        },
                    ],
                },
                items=[
                    {
                        "price": {
                            "id": "pri_01h8xce4x86pq3byesf71a7kw1",
                            "description": "Test Price Updated",
                            "product_id": "pro_01h89b2j66qq82x6vn5d39c4av",
                            "billing_cycle": {
                                "interval": "month",
                                "frequency": 1,
                            },
                            "trial_period": None,
                            "tax_mode": "account_setting",
                            "unit_price": {
                                "amount": "1200",
                                "currency_code": "USD",
                            },
                            "unit_price_overrides": [],
                            "quantity": {
                                "minimum": 1,
                                "maximum": 100,
                            },
                            "status": "active",
                        },
                        "quantity": 2,
                    },
                    {
                        "price": {
                            "id": "pri_01h81k4cdv2rygh4gccf864cy9",
                            "description": "Test Price Description",
                            "product_id": "pro_01h81jnhdrz5wfde6cn8wg9y1y",
                            "billing_cycle": {
                                "interval": "month",
                                "frequency": 1,
                            },
                            "trial_period": None,
                            "tax_mode": "account_setting",
                            "unit_price": {
                                "amount": "1200",
                                "currency_code": "USD",
                            },
                            "unit_price_overrides": [],
                            "quantity": {
                                "minimum": 1,
                                "maximum": 100,
                            },
                            "status": "active",
                        },
                        "quantity": 1,
                    },
                ],
            ),
            meta=dict(request_id="00f4aec5-126c-4dd8-9077-79ef42c16271"),
        )

        assert (
            deepdiff.DeepDiff(
                transaction,
                expected_transaction,
                ignore_order=True,
                exclude_regex_paths=r".+\.model_fields_set",
            )
            == {}
        )

        assert isinstance(transaction, TransactionResponse)
        assert isinstance(transaction.data, Transaction)
        assert str.startswith(transaction.data.id, "txn_")
        assert transaction.data.status == "draft"
        assert transaction.data.customer_id == "ctm_01h7n2fwfhctkfja2dwq2cmx8v"
        assert transaction.data.address_id is None
        assert transaction.data.business_id is None
        assert transaction.data.custom_data == {"foo": "bar"}
        assert transaction.data.origin == "api"
        assert transaction.data.collection_mode == "automatic"
        assert transaction.data.subscription_id is None
        assert transaction.data.invoice_id is None
        assert transaction.data.invoice_number is None
        assert transaction.data.billing_details is None
        assert transaction.data.billing_period is None
        assert transaction.data.currency_code == "USD"
        assert transaction.data.discount_id is None
        assert isinstance(transaction.data.created_at, datetime)
        assert isinstance(transaction.data.updated_at, datetime)
        assert transaction.data.billed_at is None
        assert transaction.data.payments == []
        assert transaction.data.checkout == {
            "url": "https://webstormit.com?_ptxn=txn_01h93v9qra13qbnagfqqddbrqd"
        }
        assert isinstance(transaction.data.details, TransactionDetails)
        assert isinstance(transaction.data.details.adjusted_totals, AdjustedTotals)
        assert isinstance(transaction.data.details.line_items[0], LineItem)

    @pytest.mark.vcr
    def test_update_transaction(self):
        transaction = self.client.update_transaction(
            transaction_id="txn_01h93v9qra13qbnagfqqddbrqd",
            data=TransactionRequest(
                items=[
                    {
                        "price_id": "pri_01h8xce4x86pq3byesf71a7kw1",
                        "quantity": 2,
                    },
                    {
                        "price_id": "pri_01h81k4cdv2rygh4gccf864cy9",
                        "quantity": 2,
                    },
                ],
                customer_id="ctm_01h7n2fwfhctkfja2dwq2cmx8v",
                custom_data={"foo": "bar"},
                collection_mode="automatic",
                currency_code="USD",
            ),
            # address|business|customer|discount|seller|adjustment|adjustments_totals
            query_params=TransactionQueryParams(
                include="address,business,customer,discount,seller,adjustment,adjustments_totals",
            ),
        )
        expected_transaction = TransactionResponse(
            data=Transaction(
                id="txn_01h93v9qra13qbnagfqqddbrqd",
                status="draft",
                customer_id="ctm_01h7n2fwfhctkfja2dwq2cmx8v",
                address_id=None,
                business_id=None,
                custom_data={"foo": "bar"},
                origin="api",
                collection_mode="automatic",
                subscription_id=None,
                invoice_id=None,
                invoice_number=None,
                billing_details=None,
                billing_period=None,
                currency_code="USD",
                discount_id=None,
                created_at="2023-08-30T18:29:10.576558762Z",
                updated_at="2023-08-30T19:23:48.077844303Z",
                billed_at=None,
                payments=[],
                checkout={
                    "url": "https://webstormit.com?_ptxn=txn_01h93v9qra13qbnagfqqddbrqd"
                },
                details={
                    "tax_rates_used": [
                        {
                            "tax_rate": "0",
                            "totals": {
                                "subtotal": "4800",
                                "discount": "0",
                                "tax": "0",
                                "total": "4800",
                            },
                        }
                    ],
                    "totals": {
                        "subtotal": "4800",
                        "tax": "0",
                        "discount": "0",
                        "total": "4800",
                        "grand_total": "4800",
                        "fee": None,
                        "credit": "0",
                        "balance": "4800",
                        "earnings": None,
                        "currency_code": "USD",
                    },
                    "adjusted_totals": {
                        "subtotal": "4800",
                        "tax": "0",
                        "total": "4800",
                        "grand_total": "4800",
                        "fee": "0",
                        "earnings": "0",
                        "currency_code": "USD",
                    },
                    "payout_totals": None,
                    "adjusted_payout_totals": None,
                    "line_items": [
                        {
                            "id": "txnitm_01h93ydrf57ybq9sh9rj07d6z9",
                            "price_id": "pri_01h8xce4x86pq3byesf71a7kw1",
                            "quantity": 2,
                            "totals": {
                                "subtotal": "2400",
                                "tax": "0",
                                "discount": "0",
                                "total": "2400",
                            },
                            "product": {
                                "id": "pro_01h89b2j66qq82x6vn5d39c4av",
                                "name": "Test Product New 2",
                                "description": "Test Product Description",
                                "tax_category": "standard",
                                "image_url": "https://example.com/image.png",
                                "status": "active",
                            },
                            "tax_rate": "0",
                            "unit_totals": {
                                "subtotal": "1200",
                                "tax": "0",
                                "discount": "0",
                                "total": "1200",
                            },
                        },
                        {
                            "id": "txnitm_01h93ydrf57ybq9sh9rmfhhx21",
                            "price_id": "pri_01h81k4cdv2rygh4gccf864cy9",
                            "quantity": 2,
                            "totals": {
                                "subtotal": "2400",
                                "tax": "0",
                                "discount": "0",
                                "total": "2400",
                            },
                            "product": {
                                "id": "pro_01h81jnhdrz5wfde6cn8wg9y1y",
                                "name": "Test Product New",
                                "description": "Test Product Description",
                                "tax_category": "standard",
                                "image_url": "https://example.com/image.png",
                                "status": "active",
                            },
                            "tax_rate": "0",
                            "unit_totals": {
                                "subtotal": "1200",
                                "tax": "0",
                                "discount": "0",
                                "total": "1200",
                            },
                        },
                    ],
                },
                items=[
                    {
                        "price": {
                            "id": "pri_01h8xce4x86pq3byesf71a7kw1",
                            "description": "Test Price Updated",
                            "product_id": "pro_01h89b2j66qq82x6vn5d39c4av",
                            "billing_cycle": {
                                "interval": "month",
                                "frequency": 1,
                            },
                            "trial_period": None,
                            "tax_mode": "account_setting",
                            "unit_price": {
                                "amount": "1200",
                                "currency_code": "USD",
                            },
                            "unit_price_overrides": [],
                            "quantity": {
                                "minimum": 1,
                                "maximum": 100,
                            },
                            "status": "active",
                        },
                        "quantity": 2,
                    },
                    {
                        "price": {
                            "id": "pri_01h81k4cdv2rygh4gccf864cy9",
                            "description": "Test Price Description",
                            "product_id": "pro_01h81jnhdrz5wfde6cn8wg9y1y",
                            "billing_cycle": {
                                "interval": "month",
                                "frequency": 1,
                            },
                            "trial_period": None,
                            "tax_mode": "account_setting",
                            "unit_price": {
                                "amount": "1200",
                                "currency_code": "USD",
                            },
                            "unit_price_overrides": [],
                            "quantity": {
                                "minimum": 1,
                                "maximum": 100,
                            },
                            "status": "active",
                        },
                        "quantity": 2,
                    },
                ],
                customer=Customer(
                    id="ctm_01h7n2fwfhctkfja2dwq2cmx8v",
                    email="asd2@asd.com",
                    name="",
                    locale="en",
                    marketing_consent=False,
                    status="active",
                    suitable_for=["automatic"],
                    is_sanctioned=False,
                    tax_exemptions=[],
                ),
                adjustments_totals={
                    "subtotal": "0",
                    "tax": "0",
                    "total": "0",
                    "fee": "0",
                    "currency_code": "USD",
                    "earnings": "0",
                    "breakdown": {
                        "chargeback": "0",
                        "refund": "0",
                        "credit": "0",
                    },
                },
                seller={
                    "active": True,
                    "created_at": "2022-11-05T15:36:49Z",
                    "display_name": "",
                    "enabled_currencies": None,
                    "id": 8939,
                    "legal_name": "Webstormit",
                    "payout_country": "HU",
                    "primary_currency": "USD",
                    "updated_at": "2022-11-05T16:02:10Z",
                },
            ),
            meta=dict(request_id="1f5a7831-f09e-4190-9b32-69261e82c2b5"),
        )

        assert (
            deepdiff.DeepDiff(
                transaction,
                expected_transaction,
                ignore_order=True,
                exclude_regex_paths=r".+\.model_fields_set",
            )
            == {}
        )

        assert isinstance(transaction, TransactionResponse)
        assert isinstance(transaction.data, Transaction)
        assert str.startswith(transaction.data.id, "txn_")
        assert transaction.data.status == "draft"
        assert transaction.data.customer_id == "ctm_01h7n2fwfhctkfja2dwq2cmx8v"
        assert transaction.data.address_id is None
        assert transaction.data.business_id is None
        assert transaction.data.custom_data == {"foo": "bar"}
        assert transaction.data.origin == "api"
        assert transaction.data.collection_mode == "automatic"
        assert transaction.data.subscription_id is None
        assert transaction.data.invoice_id is None
        assert transaction.data.invoice_number is None
        assert transaction.data.billing_details is None
        assert transaction.data.billing_period is None
        assert transaction.data.currency_code == "USD"
        assert transaction.data.discount_id is None
        assert isinstance(transaction.data.created_at, datetime)
        assert isinstance(transaction.data.updated_at, datetime)
        assert transaction.data.billed_at is None
        assert transaction.data.payments == []
        assert transaction.data.checkout == {
            "url": "https://webstormit.com?_ptxn=txn_01h93v9qra13qbnagfqqddbrqd"
        }
        assert isinstance(transaction.data.details, TransactionDetails)
        assert isinstance(transaction.data.details.adjusted_totals, AdjustedTotals)
        assert isinstance(transaction.data.details.line_items[0], LineItem)
        assert isinstance(transaction.data.customer, Customer)
        assert isinstance(transaction.data.adjustments_totals, dict)
        assert isinstance(transaction.data.seller, dict)

    @pytest.mark.vcr
    def test_get_transaction(self):
        transaction = self.client.get_transaction(
            transaction_id="txn_01h93v9qra13qbnagfqqddbrqd",
            query_params=TransactionQueryParams(
                include="address,business,customer,discount,seller,adjustment,adjustments_totals",
            ),
        )
        expected_transaction = TransactionResponse(
            data=Transaction(
                id="txn_01h93v9qra13qbnagfqqddbrqd",
                status="draft",
                customer_id="ctm_01h7n2fwfhctkfja2dwq2cmx8v",
                address_id=None,
                business_id=None,
                custom_data={"foo": "bar"},
                origin="api",
                collection_mode="automatic",
                subscription_id=None,
                invoice_id=None,
                invoice_number=None,
                billing_details=None,
                billing_period=None,
                currency_code="USD",
                discount_id=None,
                created_at="2023-08-30T18:29:10.576558762Z",
                updated_at="2023-08-30T19:23:48.077844303Z",
                billed_at=None,
                payments=[],
                checkout={
                    "url": "https://webstormit.com?_ptxn=txn_01h93v9qra13qbnagfqqddbrqd"
                },
                details={
                    "tax_rates_used": [
                        {
                            "tax_rate": "0",
                            "totals": {
                                "subtotal": "4800",
                                "discount": "0",
                                "tax": "0",
                                "total": "4800",
                            },
                        }
                    ],
                    "totals": {
                        "subtotal": "4800",
                        "tax": "0",
                        "discount": "0",
                        "total": "4800",
                        "grand_total": "4800",
                        "fee": None,
                        "credit": "0",
                        "balance": "4800",
                        "earnings": None,
                        "currency_code": "USD",
                    },
                    "adjusted_totals": {
                        "subtotal": "4800",
                        "tax": "0",
                        "total": "4800",
                        "grand_total": "4800",
                        "fee": "0",
                        "earnings": "0",
                        "currency_code": "USD",
                    },
                    "payout_totals": None,
                    "adjusted_payout_totals": None,
                    "line_items": [
                        {
                            "id": "txnitm_01h93ydrf57ybq9sh9rj07d6z9",
                            "price_id": "pri_01h8xce4x86pq3byesf71a7kw1",
                            "quantity": 2,
                            "totals": {
                                "subtotal": "2400",
                                "tax": "0",
                                "discount": "0",
                                "total": "2400",
                            },
                            "product": {
                                "id": "pro_01h89b2j66qq82x6vn5d39c4av",
                                "name": "Test Product New 2",
                                "description": "Test Product Description",
                                "tax_category": "standard",
                                "image_url": "https://example.com/image.png",
                                "status": "active",
                            },
                            "tax_rate": "0",
                            "unit_totals": {
                                "subtotal": "1200",
                                "tax": "0",
                                "discount": "0",
                                "total": "1200",
                            },
                        },
                        {
                            "id": "txnitm_01h93ydrf57ybq9sh9rmfhhx21",
                            "price_id": "pri_01h81k4cdv2rygh4gccf864cy9",
                            "quantity": 2,
                            "totals": {
                                "subtotal": "2400",
                                "tax": "0",
                                "discount": "0",
                                "total": "2400",
                            },
                            "product": {
                                "id": "pro_01h81jnhdrz5wfde6cn8wg9y1y",
                                "name": "Test Product New",
                                "description": "Test Product Description",
                                "tax_category": "standard",
                                "image_url": "https://example.com/image.png",
                                "status": "active",
                            },
                            "tax_rate": "0",
                            "unit_totals": {
                                "subtotal": "1200",
                                "tax": "0",
                                "discount": "0",
                                "total": "1200",
                            },
                        },
                    ],
                },
                items=[
                    {
                        "price": {
                            "id": "pri_01h8xce4x86pq3byesf71a7kw1",
                            "description": "Test Price Updated",
                            "product_id": "pro_01h89b2j66qq82x6vn5d39c4av",
                            "billing_cycle": {
                                "interval": "month",
                                "frequency": 1,
                            },
                            "trial_period": None,
                            "tax_mode": "account_setting",
                            "unit_price": {
                                "amount": "1200",
                                "currency_code": "USD",
                            },
                            "unit_price_overrides": [],
                            "quantity": {
                                "minimum": 1,
                                "maximum": 100,
                            },
                            "status": "active",
                        },
                        "quantity": 2,
                    },
                    {
                        "price": {
                            "id": "pri_01h81k4cdv2rygh4gccf864cy9",
                            "description": "Test Price Description",
                            "product_id": "pro_01h81jnhdrz5wfde6cn8wg9y1y",
                            "billing_cycle": {
                                "interval": "month",
                                "frequency": 1,
                            },
                            "trial_period": None,
                            "tax_mode": "account_setting",
                            "unit_price": {
                                "amount": "1200",
                                "currency_code": "USD",
                            },
                            "unit_price_overrides": [],
                            "quantity": {
                                "minimum": 1,
                                "maximum": 100,
                            },
                            "status": "active",
                        },
                        "quantity": 2,
                    },
                ],
                customer=Customer(
                    id="ctm_01h7n2fwfhctkfja2dwq2cmx8v",
                    email="asd2@asd.com",
                    name="",
                    locale="en",
                    marketing_consent=False,
                    status="active",
                    suitable_for=["automatic"],
                    is_sanctioned=False,
                    tax_exemptions=[],
                ),
                adjustments_totals={
                    "subtotal": "0",
                    "tax": "0",
                    "total": "0",
                    "fee": "0",
                    "currency_code": "USD",
                    "earnings": "0",
                    "breakdown": {
                        "chargeback": "0",
                        "refund": "0",
                        "credit": "0",
                    },
                },
                seller={
                    "active": True,
                    "created_at": "2022-11-05T15:36:49Z",
                    "display_name": "",
                    "enabled_currencies": None,
                    "id": 8939,
                    "legal_name": "Webstormit",
                    "payout_country": "HU",
                    "primary_currency": "USD",
                    "updated_at": "2022-11-05T16:02:10Z",
                },
            ),
            meta=dict(request_id="1cba911f-4b5b-42d3-9da7-1686f1d62ca0"),
        )

        assert (
            deepdiff.DeepDiff(
                transaction,
                expected_transaction,
                ignore_order=True,
                exclude_regex_paths=r".+\.model_fields_set",
            )
            == {}
        )

        assert isinstance(transaction, TransactionResponse)
        assert isinstance(transaction.data, Transaction)
        assert str.startswith(transaction.data.id, "txn_")
        assert transaction.data.status == "draft"
        assert transaction.data.customer_id == "ctm_01h7n2fwfhctkfja2dwq2cmx8v"
        assert transaction.data.address_id is None
        assert transaction.data.business_id is None
        assert transaction.data.custom_data == {"foo": "bar"}
        assert transaction.data.origin == "api"
        assert transaction.data.collection_mode == "automatic"
        assert transaction.data.subscription_id is None
        assert transaction.data.invoice_id is None
        assert transaction.data.invoice_number is None
        assert transaction.data.billing_details is None
        assert transaction.data.billing_period is None
        assert transaction.data.currency_code == "USD"
        assert transaction.data.discount_id is None
        assert isinstance(transaction.data.created_at, datetime)
        assert isinstance(transaction.data.updated_at, datetime)
        assert transaction.data.billed_at is None
        assert transaction.data.payments == []
        assert transaction.data.checkout == {
            "url": "https://webstormit.com?_ptxn=txn_01h93v9qra13qbnagfqqddbrqd"
        }
        assert isinstance(transaction.data.details, TransactionDetails)
        assert isinstance(transaction.data.details.adjusted_totals, AdjustedTotals)
        assert isinstance(transaction.data.details.line_items[0], LineItem)
        assert isinstance(transaction.data.customer, Customer)
        assert isinstance(transaction.data.adjustments_totals, dict)
        assert isinstance(transaction.data.seller, dict)

    @pytest.mark.vcr
    def test_list_transactions(self):
        transactions = self.client.list_transactions(
            query_params=TransactionQueryParams(
                include="address,business,customer,discount,seller,adjustment,adjustments_totals",
            ),
        )
        expected_transactions = TransactionsResponse(
            data=[
                Transaction(
                    id="txn_01h93v9qra13qbnagfqqddbrqd",
                    status="draft",
                    customer_id="ctm_01h7n2fwfhctkfja2dwq2cmx8v",
                    address_id=None,
                    business_id=None,
                    custom_data={"foo": "bar"},
                    origin="api",
                    collection_mode="automatic",
                    subscription_id=None,
                    invoice_id=None,
                    invoice_number=None,
                    billing_details=None,
                    billing_period=None,
                    currency_code="USD",
                    discount_id=None,
                    created_at="2023-08-30T18:29:10.576558762Z",
                    updated_at="2023-08-30T19:23:48.077844303Z",
                    billed_at=None,
                    payments=[],
                    checkout={
                        "url": "https://webstormit.com?_ptxn=txn_01h93v9qra13qbnagfqqddbrqd"
                    },
                    details={
                        "tax_rates_used": [
                            {
                                "tax_rate": "0",
                                "totals": {
                                    "subtotal": "4800",
                                    "discount": "0",
                                    "tax": "0",
                                    "total": "4800",
                                },
                            }
                        ],
                        "totals": {
                            "subtotal": "4800",
                            "tax": "0",
                            "discount": "0",
                            "total": "4800",
                            "grand_total": "4800",
                            "fee": None,
                            "credit": "0",
                            "balance": "4800",
                            "earnings": None,
                            "currency_code": "USD",
                        },
                        "adjusted_totals": {
                            "subtotal": "4800",
                            "tax": "0",
                            "total": "4800",
                            "grand_total": "4800",
                            "fee": "0",
                            "earnings": "0",
                            "currency_code": "USD",
                        },
                        "payout_totals": None,
                        "adjusted_payout_totals": None,
                        "line_items": [
                            {
                                "id": "txnitm_01h93ydrf57ybq9sh9rj07d6z9",
                                "price_id": "pri_01h8xce4x86pq3byesf71a7kw1",
                                "quantity": 2,
                                "totals": {
                                    "subtotal": "2400",
                                    "tax": "0",
                                    "discount": "0",
                                    "total": "2400",
                                },
                                "product": {
                                    "id": "pro_01h89b2j66qq82x6vn5d39c4av",
                                    "name": "Test Product New 2",
                                    "description": "Test Product Description",
                                    "tax_category": "standard",
                                    "image_url": "https://example.com/image.png",
                                    "status": "active",
                                },
                                "tax_rate": "0",
                                "unit_totals": {
                                    "subtotal": "1200",
                                    "tax": "0",
                                    "discount": "0",
                                    "total": "1200",
                                },
                            },
                            {
                                "id": "txnitm_01h93ydrf57ybq9sh9rmfhhx21",
                                "price_id": "pri_01h81k4cdv2rygh4gccf864cy9",
                                "quantity": 2,
                                "totals": {
                                    "subtotal": "2400",
                                    "tax": "0",
                                    "discount": "0",
                                    "total": "2400",
                                },
                                "product": {
                                    "id": "pro_01h81jnhdrz5wfde6cn8wg9y1y",
                                    "name": "Test Product New",
                                    "description": "Test Product Description",
                                    "tax_category": "standard",
                                    "image_url": "https://example.com/image.png",
                                    "status": "active",
                                },
                                "tax_rate": "0",
                                "unit_totals": {
                                    "subtotal": "1200",
                                    "tax": "0",
                                    "discount": "0",
                                    "total": "1200",
                                },
                            },
                        ],
                    },
                    items=[
                        {
                            "price": {
                                "id": "pri_01h8xce4x86pq3byesf71a7kw1",
                                "description": "Test Price Updated",
                                "product_id": "pro_01h89b2j66qq82x6vn5d39c4av",
                                "billing_cycle": {
                                    "interval": "month",
                                    "frequency": 1,
                                },
                                "trial_period": None,
                                "tax_mode": "account_setting",
                                "unit_price": {
                                    "amount": "1200",
                                    "currency_code": "USD",
                                },
                                "unit_price_overrides": [],
                                "quantity": {
                                    "minimum": 1,
                                    "maximum": 100,
                                },
                                "status": "active",
                            },
                            "quantity": 2,
                        },
                        {
                            "price": {
                                "id": "pri_01h81k4cdv2rygh4gccf864cy9",
                                "description": "Test Price Description",
                                "product_id": "pro_01h81jnhdrz5wfde6cn8wg9y1y",
                                "billing_cycle": {
                                    "interval": "month",
                                    "frequency": 1,
                                },
                                "trial_period": None,
                                "tax_mode": "account_setting",
                                "unit_price": {
                                    "amount": "1200",
                                    "currency_code": "USD",
                                },
                                "unit_price_overrides": [],
                                "quantity": {
                                    "minimum": 1,
                                    "maximum": 100,
                                },
                                "status": "active",
                            },
                            "quantity": 2,
                        },
                    ],
                    customer=Customer(
                        id="ctm_01h7n2fwfhctkfja2dwq2cmx8v",
                        email="asd2@asd.com",
                        name="",
                        locale="en",
                        marketing_consent=False,
                        status="active",
                        suitable_for=["automatic"],
                        is_sanctioned=False,
                        tax_exemptions=[],
                    ),
                    adjustments_totals={
                        "subtotal": "0",
                        "tax": "0",
                        "total": "0",
                        "fee": "0",
                        "currency_code": "USD",
                        "earnings": "0",
                        "breakdown": {
                            "chargeback": "0",
                            "refund": "0",
                            "credit": "0",
                        },
                    },
                    seller={
                        "active": True,
                        "created_at": "2022-11-05T15:36:49Z",
                        "display_name": "",
                        "enabled_currencies": None,
                        "id": 8939,
                        "legal_name": "Webstormit",
                        "payout_country": "HU",
                        "primary_currency": "USD",
                        "updated_at": "2022-11-05T16:02:10Z",
                    },
                ),
            ],
            meta=dict(
                request_id="d2e768da-eb05-4c16-8f54-afd97e00a67d",
                pagination=dict(
                    per_page=30,
                    next="https://sandbox-api.paddle.com/transactions?after=txn_01h7n3a7g7h0qr49zt9ckgketd&include"
                    "=address&include=business&include=customer&include=discount&include=seller&include"
                    "=adjustment&include=adjustments_totals",
                    has_more=False,
                    estimated_total=1,
                ),
            ),
        )

        assert (
            deepdiff.DeepDiff(
                transactions,
                expected_transactions,
                ignore_order=True,
                exclude_regex_paths=r".+\.model_fields_set",
            )
            == {}
        )

        assert isinstance(transactions, TransactionsResponse)
        assert isinstance(transactions.data[0], Transaction)

    @pytest.mark.vcr
    def test_preview_transaction(self):
        transaction = self.client.preview_transaction(
            data=TransactionRequest(
                items=[
                    {
                        "price_id": "pri_01h8xce4x86pq3byesf71a7kw1",
                        "quantity": 1,
                    },
                    {
                        "price_id": "pri_01h81k4cdv2rygh4gccf864cy9",
                        "quantity": 1,
                    },
                ],
                customer_id="ctm_01h7n2fwfhctkfja2dwq2cmx8v",
                currency_code="USD",
            ),
            # address|business|customer|discount|seller|adjustment|adjustments_totals
            query_params=TransactionQueryParams(
                include="address,business,customer,discount,seller,adjustment,adjustments_totals",
            ),
        )

        expected_transaction = TransactionPreviewResponse(
            data=TransactionPreview(
                customer_id="ctm_01h7n2fwfhctkfja2dwq2cmx8v",
                address_id=None,
                business_id=None,
                billing_details=None,
                billing_period=None,
                currency_code="USD",
                discount_id=None,
                ignore_trials=False,
                details={
                    "tax_rates_used": [
                        {
                            "tax_rate": "0",
                            "totals": {
                                "subtotal": "2400",
                                "discount": "0",
                                "tax": "0",
                                "total": "2400",
                            },
                        }
                    ],
                    "totals": {
                        "subtotal": "2400",
                        "tax": "0",
                        "discount": "0",
                        "total": "2400",
                        "grand_total": "2400",
                        "fee": None,
                        "credit": "0",
                        "balance": "2400",
                        "earnings": None,
                        "currency_code": "USD",
                    },
                    "line_items": [
                        {
                            "price_id": "pri_01h8xce4x86pq3byesf71a7kw1",
                            "quantity": 1,
                            "totals": {
                                "subtotal": "1200",
                                "tax": "0",
                                "discount": "0",
                                "total": "1200",
                            },
                            "product": {
                                "id": "pro_01h89b2j66qq82x6vn5d39c4av",
                                "name": "Test Product New 2",
                                "description": "Test Product Description",
                                "tax_category": "standard",
                                "image_url": "https://example.com/image.png",
                                "status": "active",
                            },
                            "tax_rate": "0",
                            "unit_totals": {
                                "subtotal": "1200",
                                "tax": "0",
                                "discount": "0",
                                "total": "1200",
                            },
                        },
                        {
                            "price_id": "pri_01h81k4cdv2rygh4gccf864cy9",
                            "quantity": 1,
                            "totals": {
                                "subtotal": "1200",
                                "tax": "0",
                                "discount": "0",
                                "total": "1200",
                            },
                            "product": {
                                "id": "pro_01h81jnhdrz5wfde6cn8wg9y1y",
                                "name": "Test Product New",
                                "description": "Test Product Description",
                                "tax_category": "standard",
                                "image_url": "https://example.com/image.png",
                                "status": "active",
                            },
                            "tax_rate": "0",
                            "unit_totals": {
                                "subtotal": "1200",
                                "tax": "0",
                                "discount": "0",
                                "total": "1200",
                            },
                        },
                    ],
                },
                items=[
                    {
                        "price": {
                            "id": "pri_01h8xce4x86pq3byesf71a7kw1",
                            "description": "Test Price Updated",
                            "product_id": "pro_01h89b2j66qq82x6vn5d39c4av",
                            "billing_cycle": {
                                "interval": "month",
                                "frequency": 1,
                            },
                            "trial_period": None,
                            "tax_mode": "account_setting",
                            "unit_price": {
                                "amount": "1200",
                                "currency_code": "USD",
                            },
                            "unit_price_overrides": [],
                            "quantity": {
                                "minimum": 1,
                                "maximum": 100,
                            },
                            "status": "active",
                        },
                        "proration": None,
                        "include_in_totals": True,
                        "quantity": 1,
                    },
                    {
                        "price": {
                            "id": "pri_01h81k4cdv2rygh4gccf864cy9",
                            "description": "Test Price Description",
                            "product_id": "pro_01h81jnhdrz5wfde6cn8wg9y1y",
                            "billing_cycle": {
                                "interval": "month",
                                "frequency": 1,
                            },
                            "trial_period": None,
                            "tax_mode": "account_setting",
                            "unit_price": {
                                "amount": "1200",
                                "currency_code": "USD",
                            },
                            "unit_price_overrides": [],
                            "quantity": {
                                "minimum": 1,
                                "maximum": 100,
                            },
                            "status": "active",
                        },
                        "proration": None,
                        "include_in_totals": True,
                        "quantity": 1,
                    },
                ],
            ),
            meta=dict(request_id="165d958f-260c-494c-b70e-670eba1e2661"),
        )

        assert (
            deepdiff.DeepDiff(
                transaction,
                expected_transaction,
                ignore_order=True,
                exclude_regex_paths=r".+\.model_fields_set",
            )
            == {}
        )
