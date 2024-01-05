import os
from datetime import datetime

import deepdiff
import pytest
from apiclient import HeaderAuthentication

from paddle_billing_client.models.price import (
    BillingCycle,
    Price,
    PriceQueryParams,
    PriceRequest,
    PriceResponse,
    PricesResponse,
    Quantity,
    TrialPeriod,
    UnitPrice,
)


class TestPrice:
    def setup_class(self):
        from paddle_billing_client.client import PaddleApiClient  # pragma: no cover

        self.client = PaddleApiClient(
            authentication_method=HeaderAuthentication(
                token=os.getenv("PADDLE_SANDBOX_AUTH_TOKEN")
            ),
        )

    @pytest.mark.vcr
    def test_create_price(self):
        price = self.client.create_price(
            data=PriceRequest(
                product_id="pro_01h89b2j66qq82x6vn5d39c4av",
                description="Test Price",
                unit_price=dict(
                    amount="1000",
                    currency_code="USD",
                ),
                billing_cycle=BillingCycle(
                    interval="month",
                    frequency=1,
                ),
                tax_mode="account_setting",
            ),
        )
        expected_price = PriceResponse(
            data=Price(
                id="pri_01h8xce4x86pq3byesf71a7kw1",
                product_id="pro_01h89b2j66qq82x6vn5d39c4av",
                description="Test Price",
                unit_price=dict(
                    amount="1000",
                    currency_code="USD",
                ),
                billing_cycle=BillingCycle(
                    interval="month",
                    frequency=1,
                ),
                quantity=Quantity(
                    minimum=1,
                    maximum=100,
                ),
                tax_mode="account_setting",
                unit_price_overrides=[],
                status="active",
            ),
            meta=dict(request_id="d6fc2607-992b-480a-b2b1-f41f296cacc5"),
        )
        assert (
            deepdiff.DeepDiff(
                price,
                expected_price,
                ignore_order=True,
                exclude_regex_paths=r".+\.model_fields_set",
            )
            == {}
        )

        assert isinstance(price, PriceResponse)
        assert isinstance(price.data, Price)
        assert str.startswith(price.data.id, "pri_")
        assert price.data.product_id == "pro_01h89b2j66qq82x6vn5d39c4av"
        assert price.data.description == "Test Price"
        assert price.data.unit_price == UnitPrice(
            amount="1000",
            currency_code="USD",
        )
        assert price.data.billing_cycle == BillingCycle(
            interval="month",
            frequency=1,
        )
        assert price.data.quantity == Quantity(
            minimum=1,
            maximum=100,
        )
        assert price.data.tax_mode == "account_setting"
        assert price.data.unit_price_overrides == []
        assert price.data.status == "active"

    @pytest.mark.vcr
    def test_update_price(self):
        price = self.client.update_price(
            price_id="pri_01h8xce4x86pq3byesf71a7kw1",
            data=PriceRequest(
                description="Test Price Updated",
                unit_price=dict(
                    amount="1200",
                    currency_code="USD",
                ),
                billing_cycle=BillingCycle(
                    interval="month",
                    frequency=1,
                ),
                tax_mode="account_setting",
            ),
        )
        expected_price = PriceResponse(
            data=Price(
                id="pri_01h8xce4x86pq3byesf71a7kw1",
                product_id="pro_01h89b2j66qq82x6vn5d39c4av",
                description="Test Price Updated",
                unit_price=dict(
                    amount="1200",
                    currency_code="USD",
                ),
                billing_cycle=BillingCycle(
                    interval="month",
                    frequency=1,
                ),
                quantity=Quantity(
                    minimum=1,
                    maximum=100,
                ),
                tax_mode="account_setting",
                unit_price_overrides=[],
                status="active",
            ),
            meta=dict(request_id="213c471d-a71c-43f0-b336-34ff914166d3"),
        )
        assert (
            deepdiff.DeepDiff(
                price,
                expected_price,
                ignore_order=True,
                exclude_regex_paths=r".+\.model_fields_set",
            )
            == {}
        )

        assert isinstance(price, PriceResponse)
        assert isinstance(price.data, Price)
        assert str.startswith(price.data.id, "pri_")
        assert price.data.product_id == "pro_01h89b2j66qq82x6vn5d39c4av"
        assert price.data.description == "Test Price Updated"
        assert price.data.unit_price == UnitPrice(
            amount="1200",
            currency_code="USD",
        )
        assert price.data.billing_cycle == BillingCycle(
            interval="month",
            frequency=1,
        )
        assert price.data.quantity == Quantity(
            minimum=1,
            maximum=100,
        )
        assert price.data.tax_mode == "account_setting"
        assert price.data.unit_price_overrides == []
        assert price.data.status == "active"

    @pytest.mark.vcr
    def test_get_price(self):
        price = self.client.get_price(
            price_id="pri_01h8xce4x86pq3byesf71a7kw1",
        )
        expected_price = PriceResponse(
            data=Price(
                id="pri_01h8xce4x86pq3byesf71a7kw1",
                product_id="pro_01h89b2j66qq82x6vn5d39c4av",
                description="Test Price Updated",
                unit_price=dict(
                    amount="1200",
                    currency_code="USD",
                ),
                trial_period=TrialPeriod(
                    interval="day",
                    frequency=3,
                ),
                billing_cycle=BillingCycle(
                    interval="month",
                    frequency=1,
                ),
                quantity=Quantity(
                    minimum=1,
                    maximum=100,
                ),
                tax_mode="account_setting",
                unit_price_overrides=[],
                status="active",
            ),
            meta=dict(request_id="2f32b40b-c38c-49c5-9dfe-4e779a66208c"),
        )
        assert (
            deepdiff.DeepDiff(
                price,
                expected_price,
                ignore_order=True,
                exclude_regex_paths=r".+\.model_fields_set",
            )
            == {}
        )

        assert isinstance(price, PriceResponse)
        assert isinstance(price.data, Price)
        assert str.startswith(price.data.id, "pri_")
        assert price.data.product_id == "pro_01h89b2j66qq82x6vn5d39c4av"
        assert price.data.description == "Test Price Updated"
        assert price.data.unit_price == UnitPrice(
            amount="1200",
            currency_code="USD",
        )
        assert price.data.billing_cycle == BillingCycle(
            interval="month",
            frequency=1,
        )
        assert price.data.quantity == Quantity(
            minimum=1,
            maximum=100,
        )
        assert price.data.tax_mode == "account_setting"
        assert price.data.unit_price_overrides == []
        assert price.data.status == "active"

    @pytest.mark.vcr
    def test_list_prices(self):
        prices = self.client.list_prices(
            query_params=PriceQueryParams(
                recurring=True,
            ),
        )
        expected_prices = PricesResponse(
            data=[
                Price(
                    id="pri_01h8xce4x86pq3byesf71a7kw1",
                    product_id="pro_01h89b2j66qq82x6vn5d39c4av",
                    description="Test Price Updated",
                    unit_price=dict(
                        amount="1200",
                        currency_code="USD",
                    ),
                    billing_cycle=BillingCycle(
                        interval="month",
                        frequency=1,
                    ),
                    quantity=Quantity(
                        minimum=1,
                        maximum=100,
                    ),
                    tax_mode="account_setting",
                    unit_price_overrides=[],
                    status="active",
                ),
            ],
            meta=dict(
                request_id="7fd9eeea-8a71-4962-8abf-6049c56aad28",
                pagination=dict(
                    per_page=50,
                    next="https://sandbox-api.paddle.com/prices?after=pri_01h7mrnc315chey77qhrd32vfs\u0026recurring=True",
                    has_more=False,
                    estimated_total=1,
                ),
            ),
        )
        assert (
            deepdiff.DeepDiff(
                prices,
                expected_prices,
                ignore_order=True,
                exclude_regex_paths=r".+\.model_fields_set",
            )
            == {}
        )

        assert isinstance(prices, PricesResponse)
        assert isinstance(prices.data, list)
        assert isinstance(prices.data[0], Price)
        assert str.startswith(prices.data[0].id, "pri_")
        assert prices.data[0].product_id == "pro_01h89b2j66qq82x6vn5d39c4av"
        assert prices.data[0].description == "Test Price Updated"
        assert prices.data[0].unit_price == UnitPrice(
            amount="1200",
            currency_code="USD",
        )
        assert prices.data[0].billing_cycle == BillingCycle(
            interval="month",
            frequency=1,
        )
        assert prices.data[0].quantity == Quantity(
            minimum=1,
            maximum=100,
        )
        assert prices.data[0].tax_mode == "account_setting"
        assert prices.data[0].unit_price_overrides == []
        assert prices.data[0].status == "active"
