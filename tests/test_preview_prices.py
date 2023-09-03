import os
from datetime import datetime

import deepdiff
import pytest
from apiclient import HeaderAuthentication

from paddle_billing_client.models.address import Address
from paddle_billing_client.models.customer import Customer
from paddle_billing_client.models.product import Product
from paddle_billing_client.models.transaction import (
    AdjustedTotals,
    LineItem,
    LineItemTotals,
    LineItemUnitTotals,
    Transaction,
    TransactionDetails,
    TransactionPreview,
    TransactionPreviewResponse,
    TransactionQueryParams,
    TransactionRequest,
    TransactionResponse,
    TransactionsResponse,
)


class TestPreviewPrices:
    def setup_class(self):
        from paddle_billing_client.client import PaddleApiClient  # pragma: no cover

        self.client = PaddleApiClient(
            authentication_method=HeaderAuthentication(
                token=os.getenv("PADDLE_SANDBOX_AUTH_TOKEN")
            ),
        )

    """
    customer_ip_address: Paddle fetches location using the IP address to calculate totals.
    address: Paddle uses the country and ZIP code (where supplied) to calculate totals.
    customer_id, address_id, business_id: Paddle uses existing customer data to calculate totals. Typically used for logged-in customers.
    """

    @pytest.mark.vcr
    def test_preview_prices_customer_ip_address(self):
        transaction = self.client.preview_prices(
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
                # customer_id="ctm_01h7n2fwfhctkfja2dwq2cmx8v",
                currency_code="USD",
                customer_ip_address="94.21.112.101",
            ),
        )
        expected_transaction = TransactionResponse(
            data=Transaction(
                id=None,
                customer_ip_address="94.21.112.101",
                status=None,
                customer_id=None,
                address=Address(
                    id=None,
                    description=None,
                    first_line=None,
                    second_line=None,
                    city=None,
                    postal_code="1035",
                    region=None,
                    country_code="HU",
                    status=None,
                    created_at=None,
                    updated_at=None,
                ),
                business_id=None,
                origin=None,
                subscription_id=None,
                invoice_id=None,
                invoice_number=None,
                billing_details=None,
                billing_period=None,
                currency_code="USD",
                payments=None,
                details={
                    "line_items": [
                        LineItem(
                            id=None,
                            price_id=None,
                            quantity=2,
                            proration=None,
                            tax_rate="0.27",
                            unit_totals=LineItemUnitTotals(
                                subtotal="1200", discount="0", tax="324", total="1524"
                            ),
                            totals=LineItemTotals(
                                subtotal="2400", discount="0", tax="648", total="3048"
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
                            formatted_totals={
                                "subtotal": "$24.00",
                                "discount": "$0.00",
                                "tax": "$6.48",
                                "total": "$30.48",
                            },
                            formatted_unit_totals={
                                "subtotal": "$12.00",
                                "discount": "$0.00",
                                "tax": "$3.24",
                                "total": "$15.24",
                            },
                            discounts=[],
                            price={
                                "id": "pri_01h8xce4x86pq3byesf71a7kw1",
                                "description": "Test Price Updated",
                                "product_id": "pro_01h89b2j66qq82x6vn5d39c4av",
                                "billing_cycle": {"interval": "month", "frequency": 1},
                                "trial_period": None,
                                "tax_mode": "account_setting",
                                "unit_price": {
                                    "amount": "1200",
                                    "currency_code": "USD",
                                },
                                "unit_price_overrides": [],
                                "quantity": {"minimum": 1, "maximum": 100},
                                "status": "active",
                            },
                        ),
                        LineItem(
                            id=None,
                            price_id=None,
                            quantity=2,
                            proration=None,
                            tax_rate="0.27",
                            unit_totals=LineItemUnitTotals(
                                subtotal="1200", discount="0", tax="324", total="1524"
                            ),
                            totals=LineItemTotals(
                                subtotal="2400", discount="0", tax="648", total="3048"
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
                            formatted_totals={
                                "subtotal": "$24.00",
                                "discount": "$0.00",
                                "tax": "$6.48",
                                "total": "$30.48",
                            },
                            formatted_unit_totals={
                                "subtotal": "$12.00",
                                "discount": "$0.00",
                                "tax": "$3.24",
                                "total": "$15.24",
                            },
                            discounts=[],
                            price={
                                "id": "pri_01h81k4cdv2rygh4gccf864cy9",
                                "description": "Test Price Description",
                                "product_id": "pro_01h81jnhdrz5wfde6cn8wg9y1y",
                                "billing_cycle": {"interval": "month", "frequency": 1},
                                "trial_period": None,
                                "tax_mode": "account_setting",
                                "unit_price": {
                                    "amount": "1200",
                                    "currency_code": "USD",
                                },
                                "unit_price_overrides": [],
                                "quantity": {"minimum": 1, "maximum": 100},
                                "status": "active",
                            },
                        ),
                    ],
                },
                items=None,
            ),
            meta=dict(request_id="957e5251-d08b-49d2-9c99-61433ad90678"),
        )

        assert (
            deepdiff.DeepDiff(transaction, expected_transaction, ignore_order=True)
            == {}
        )

    @pytest.mark.vcr
    def test_preview_prices_address(self):
        transaction = self.client.preview_prices(
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
                # customer_id="ctm_01h7n2fwfhctkfja2dwq2cmx8v",
                address=Address(
                    description=None,
                    first_line=None,
                    second_line=None,
                    city=None,
                    postal_code="1035",
                    region=None,
                    country_code="HU",
                ),
                currency_code="USD",
            ),
        )
        expected_transaction = TransactionResponse(
            data=Transaction(
                id=None,
                status=None,
                customer_id=None,
                address=Address(
                    id=None,
                    description=None,
                    first_line=None,
                    second_line=None,
                    city=None,
                    postal_code="1035",
                    region=None,
                    country_code="HU",
                    status=None,
                    created_at=None,
                    updated_at=None,
                ),
                business_id=None,
                origin=None,
                subscription_id=None,
                invoice_id=None,
                invoice_number=None,
                billing_details=None,
                billing_period=None,
                currency_code="USD",
                payments=None,
                details={
                    "line_items": [
                        LineItem(
                            id=None,
                            price_id=None,
                            quantity=2,
                            proration=None,
                            tax_rate="0.27",
                            unit_totals=LineItemUnitTotals(
                                subtotal="1200", discount="0", tax="324", total="1524"
                            ),
                            totals=LineItemTotals(
                                subtotal="2400", discount="0", tax="648", total="3048"
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
                            formatted_totals={
                                "subtotal": "$24.00",
                                "discount": "$0.00",
                                "tax": "$6.48",
                                "total": "$30.48",
                            },
                            formatted_unit_totals={
                                "subtotal": "$12.00",
                                "discount": "$0.00",
                                "tax": "$3.24",
                                "total": "$15.24",
                            },
                            discounts=[],
                            price={
                                "id": "pri_01h8xce4x86pq3byesf71a7kw1",
                                "description": "Test Price Updated",
                                "product_id": "pro_01h89b2j66qq82x6vn5d39c4av",
                                "billing_cycle": {"interval": "month", "frequency": 1},
                                "trial_period": None,
                                "tax_mode": "account_setting",
                                "unit_price": {
                                    "amount": "1200",
                                    "currency_code": "USD",
                                },
                                "unit_price_overrides": [],
                                "quantity": {"minimum": 1, "maximum": 100},
                                "status": "active",
                            },
                        ),
                        LineItem(
                            id=None,
                            price_id=None,
                            quantity=2,
                            proration=None,
                            tax_rate="0.27",
                            unit_totals=LineItemUnitTotals(
                                subtotal="1200", discount="0", tax="324", total="1524"
                            ),
                            totals=LineItemTotals(
                                subtotal="2400", discount="0", tax="648", total="3048"
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
                            formatted_totals={
                                "subtotal": "$24.00",
                                "discount": "$0.00",
                                "tax": "$6.48",
                                "total": "$30.48",
                            },
                            formatted_unit_totals={
                                "subtotal": "$12.00",
                                "discount": "$0.00",
                                "tax": "$3.24",
                                "total": "$15.24",
                            },
                            discounts=[],
                            price={
                                "id": "pri_01h81k4cdv2rygh4gccf864cy9",
                                "description": "Test Price Description",
                                "product_id": "pro_01h81jnhdrz5wfde6cn8wg9y1y",
                                "billing_cycle": {"interval": "month", "frequency": 1},
                                "trial_period": None,
                                "tax_mode": "account_setting",
                                "unit_price": {
                                    "amount": "1200",
                                    "currency_code": "USD",
                                },
                                "unit_price_overrides": [],
                                "quantity": {"minimum": 1, "maximum": 100},
                                "status": "active",
                            },
                        ),
                    ],
                },
                items=None,
            ),
            meta=dict(request_id="c0dba93e-6c23-469d-9de8-6bda09dfdd09"),
        )

        assert (
            deepdiff.DeepDiff(transaction, expected_transaction, ignore_order=True)
            == {}
        )

    @pytest.mark.vcr
    def test_preview_prices_customer_id_with_address_id(self):
        transaction = self.client.preview_prices(
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
                address_id="add_01h8w4y9qfknzaq05xsd8eptjj",
                currency_code="USD",
            ),
        )
        expected_transaction = TransactionResponse(
            data=Transaction(
                id=None,
                status=None,
                customer_id="ctm_01h7n2fwfhctkfja2dwq2cmx8v",
                address_id="add_01h8w4y9qfknzaq05xsd8eptjj",
                address=Address(
                    id=None,
                    description=None,
                    first_line=None,
                    second_line=None,
                    city=None,
                    postal_code="1035",
                    region=None,
                    country_code="HU",
                    status=None,
                    created_at=None,
                    updated_at=None,
                ),
                business_id=None,
                origin=None,
                subscription_id=None,
                invoice_id=None,
                invoice_number=None,
                billing_details=None,
                billing_period=None,
                currency_code="USD",
                payments=None,
                details={
                    "line_items": [
                        LineItem(
                            id=None,
                            price_id=None,
                            quantity=2,
                            proration=None,
                            tax_rate="0.27",
                            unit_totals=LineItemUnitTotals(
                                subtotal="1200", discount="0", tax="324", total="1524"
                            ),
                            totals=LineItemTotals(
                                subtotal="2400", discount="0", tax="648", total="3048"
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
                            formatted_totals={
                                "subtotal": "$24.00",
                                "discount": "$0.00",
                                "tax": "$6.48",
                                "total": "$30.48",
                            },
                            formatted_unit_totals={
                                "subtotal": "$12.00",
                                "discount": "$0.00",
                                "tax": "$3.24",
                                "total": "$15.24",
                            },
                            discounts=[],
                            price={
                                "id": "pri_01h8xce4x86pq3byesf71a7kw1",
                                "description": "Test Price Updated",
                                "product_id": "pro_01h89b2j66qq82x6vn5d39c4av",
                                "billing_cycle": {"interval": "month", "frequency": 1},
                                "trial_period": None,
                                "tax_mode": "account_setting",
                                "unit_price": {
                                    "amount": "1200",
                                    "currency_code": "USD",
                                },
                                "unit_price_overrides": [],
                                "quantity": {"minimum": 1, "maximum": 100},
                                "status": "active",
                            },
                        ),
                        LineItem(
                            id=None,
                            price_id=None,
                            quantity=2,
                            proration=None,
                            tax_rate="0.27",
                            unit_totals=LineItemUnitTotals(
                                subtotal="1200", discount="0", tax="324", total="1524"
                            ),
                            totals=LineItemTotals(
                                subtotal="2400", discount="0", tax="648", total="3048"
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
                            formatted_totals={
                                "subtotal": "$24.00",
                                "discount": "$0.00",
                                "tax": "$6.48",
                                "total": "$30.48",
                            },
                            formatted_unit_totals={
                                "subtotal": "$12.00",
                                "discount": "$0.00",
                                "tax": "$3.24",
                                "total": "$15.24",
                            },
                            discounts=[],
                            price={
                                "id": "pri_01h81k4cdv2rygh4gccf864cy9",
                                "description": "Test Price Description",
                                "product_id": "pro_01h81jnhdrz5wfde6cn8wg9y1y",
                                "billing_cycle": {"interval": "month", "frequency": 1},
                                "trial_period": None,
                                "tax_mode": "account_setting",
                                "unit_price": {
                                    "amount": "1200",
                                    "currency_code": "USD",
                                },
                                "unit_price_overrides": [],
                                "quantity": {"minimum": 1, "maximum": 100},
                                "status": "active",
                            },
                        ),
                    ],
                },
                items=None,
            ),
            meta=dict(request_id="d6fdc1fc-7688-46ec-8beb-e0ab65e27cf9"),
        )

        assert (
            deepdiff.DeepDiff(transaction, expected_transaction, ignore_order=True)
            == {}
        )

    @pytest.mark.vcr
    def test_preview_prices_customer_id_with_business_id(self):
        transaction = self.client.preview_prices(
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
                business_id="biz_01h9e61yyv66813j7x1v4d2hgt",
                currency_code="USD",
            ),
        )
        expected_transaction = TransactionResponse(
            data=Transaction(
                id=None,
                status=None,
                customer_id="ctm_01h7n2fwfhctkfja2dwq2cmx8v",
                address_id=None,
                address=None,
                business_id="biz_01h9e61yyv66813j7x1v4d2hgt",
                origin=None,
                subscription_id=None,
                invoice_id=None,
                invoice_number=None,
                billing_details=None,
                billing_period=None,
                currency_code="USD",
                payments=None,
                details={
                    "line_items": [
                        LineItem(
                            id=None,
                            price_id=None,
                            quantity=2,
                            proration=None,
                            tax_rate="0",
                            unit_totals=LineItemUnitTotals(
                                subtotal="1200", discount="0", tax="0", total="1200"
                            ),
                            totals=LineItemTotals(
                                subtotal="2400", discount="0", tax="0", total="2400"
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
                            formatted_totals={
                                "subtotal": "$24.00",
                                "discount": "$0.00",
                                "tax": "$0.00",
                                "total": "$24.00",
                            },
                            formatted_unit_totals={
                                "subtotal": "$12.00",
                                "discount": "$0.00",
                                "tax": "$0.00",
                                "total": "$12.00",
                            },
                            discounts=[],
                            price={
                                "id": "pri_01h8xce4x86pq3byesf71a7kw1",
                                "description": "Test Price Updated",
                                "product_id": "pro_01h89b2j66qq82x6vn5d39c4av",
                                "billing_cycle": {"interval": "month", "frequency": 1},
                                "trial_period": None,
                                "tax_mode": "account_setting",
                                "unit_price": {
                                    "amount": "1200",
                                    "currency_code": "USD",
                                },
                                "unit_price_overrides": [],
                                "quantity": {"minimum": 1, "maximum": 100},
                                "status": "active",
                            },
                        ),
                        LineItem(
                            id=None,
                            price_id=None,
                            quantity=2,
                            proration=None,
                            tax_rate="0",
                            unit_totals=LineItemUnitTotals(
                                subtotal="1200", discount="0", tax="0", total="1200"
                            ),
                            totals=LineItemTotals(
                                subtotal="2400", discount="0", tax="0", total="2400"
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
                            formatted_totals={
                                "subtotal": "$24.00",
                                "discount": "$0.00",
                                "tax": "$0.00",
                                "total": "$24.00",
                            },
                            formatted_unit_totals={
                                "subtotal": "$12.00",
                                "discount": "$0.00",
                                "tax": "$0.00",
                                "total": "$12.00",
                            },
                            discounts=[],
                            price={
                                "id": "pri_01h81k4cdv2rygh4gccf864cy9",
                                "description": "Test Price Description",
                                "product_id": "pro_01h81jnhdrz5wfde6cn8wg9y1y",
                                "billing_cycle": {"interval": "month", "frequency": 1},
                                "trial_period": None,
                                "tax_mode": "account_setting",
                                "unit_price": {
                                    "amount": "1200",
                                    "currency_code": "USD",
                                },
                                "unit_price_overrides": [],
                                "quantity": {"minimum": 1, "maximum": 100},
                                "status": "active",
                            },
                        ),
                    ],
                },
                items=None,
            ),
            meta=dict(request_id="aadb26eb-0e84-4dee-964e-e936fe93beee"),
        )

        assert (
            deepdiff.DeepDiff(transaction, expected_transaction, ignore_order=True)
            == {}
        )
