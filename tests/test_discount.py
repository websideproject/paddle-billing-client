import os
from datetime import datetime, timedelta, timezone

import deepdiff
import pytest
from apiclient.authentication_methods import HeaderAuthentication

from paddle_billing_client.models.discount import (
    Discount,
    DiscountQueryParams,
    DiscountRequest,
    DiscountResponse,
    DiscountsResponse,
)


class TestDiscount:
    def setup_class(self):
        from paddle_billing_client.client import PaddleApiClient  # pragma: no cover

        self.client = PaddleApiClient(
            authentication_method=HeaderAuthentication(
                token=os.getenv("PADDLE_SANDBOX_AUTH_TOKEN")
            ),
        )

    @pytest.mark.vcr
    def test_create_discount(self):
        discount = self.client.create_discount(
            data=DiscountRequest(
                amount="1000",
                description="Test Discount",
                type="flat",
                enabled_for_checkout=True,
                code="TESTDISCOUNT",
                currency_code="USD",
                recur=True,
                maximum_recurring_intervals=12,
                usage_limit=100,
                restrict_to=["pro_01h89b2j66qq82x6vn5d39c4av"],
                expires_at=(
                    datetime.now(timezone.utc) + timedelta(days=30)
                ).isoformat(),
            ),
        )
        expected_discount = DiscountResponse(
            data=Discount(
                id="dsc_01h8xfbnfy4gtfd15fjgxfbrfs",
                amount="1000",
                description="Test Discount",
                type="flat",
                enabled_for_checkout=True,
                code="TESTDISCOUNT",
                currency_code="USD",
                recur=True,
                maximum_recurring_intervals=12,
                usage_limit=100,
                restrict_to=["pro_01h89b2j66qq82x6vn5d39c4av"],
                expires_at="2023-09-27T07:05:03.808311Z",
                status="active",
                times_used=0,
                created_at="2023-08-28T07:05:04.254Z",
                updated_at="2023-08-28T07:05:04.254Z",
            ),
            meta=dict(request_id="cacccc0e-f2bc-4f9a-8c27-45a067e7e13c"),
        )

        assert deepdiff.DeepDiff(discount, expected_discount, ignore_order=True) == {}

        assert isinstance(discount, DiscountResponse)
        assert isinstance(discount.data, Discount)
        assert str.startswith(discount.data.id, "dsc_")

        assert discount.data.amount == "1000"
        assert discount.data.description == "Test Discount"
        assert discount.data.type == "flat"
        assert discount.data.enabled_for_checkout == True
        assert discount.data.code == "TESTDISCOUNT"
        assert discount.data.currency_code == "USD"
        assert discount.data.recur == True
        assert discount.data.maximum_recurring_intervals == 12
        assert discount.data.usage_limit == 100
        assert discount.data.restrict_to == ["pro_01h89b2j66qq82x6vn5d39c4av"]
        assert discount.data.status == "active"
        assert discount.data.times_used == 0
        assert isinstance(discount.data.expires_at, datetime)
        assert isinstance(discount.data.created_at, datetime)
        assert isinstance(discount.data.updated_at, datetime)

    @pytest.mark.vcr
    def test_update_discount(self):
        discount = self.client.update_discount(
            discount_id="dsc_01h8xfbnfy4gtfd15fjgxfbrfs",
            data=DiscountRequest(
                amount="800",
                description="Test Discount Updated",
                type="flat",
                enabled_for_checkout=True,
                code="TESTDISCOUNT",
                currency_code="USD",
                recur=True,
                maximum_recurring_intervals=12,
                usage_limit=100,
                restrict_to=["pro_01h89b2j66qq82x6vn5d39c4av"],
                status="active",
            ),
        )
        expected_discount = DiscountResponse(
            data=Discount(
                id="dsc_01h8xfbnfy4gtfd15fjgxfbrfs",
                amount="800",
                description="Test Discount Updated",
                type="flat",
                enabled_for_checkout=True,
                code="TESTDISCOUNT",
                currency_code="USD",
                recur=True,
                maximum_recurring_intervals=12,
                usage_limit=100,
                restrict_to=["pro_01h89b2j66qq82x6vn5d39c4av"],
                expires_at="2023-09-27T07:05:03.808311Z",
                status="active",
                times_used=0,
                created_at="2023-08-28T07:05:04.254Z",
                updated_at="2023-08-28T07:09:23.763Z",
            ),
            meta=dict(request_id="82d39996-2c37-4de0-9f45-221eb53689fd"),
        )

        assert deepdiff.DeepDiff(discount, expected_discount, ignore_order=True) == {}

        assert isinstance(discount, DiscountResponse)
        assert isinstance(discount.data, Discount)
        assert str.startswith(discount.data.id, "dsc_")
        assert discount.data.amount == "800"
        assert discount.data.description == "Test Discount Updated"
        assert discount.data.type == "flat"
        assert discount.data.enabled_for_checkout == True
        assert discount.data.code == "TESTDISCOUNT"
        assert discount.data.currency_code == "USD"
        assert discount.data.recur == True
        assert discount.data.maximum_recurring_intervals == 12
        assert discount.data.usage_limit == 100
        assert discount.data.restrict_to == ["pro_01h89b2j66qq82x6vn5d39c4av"]
        assert discount.data.status == "active"
        assert discount.data.times_used == 0
        assert isinstance(discount.data.expires_at, datetime)
        assert isinstance(discount.data.created_at, datetime)
        assert isinstance(discount.data.updated_at, datetime)

    @pytest.mark.vcr
    def test_get_discount(self):
        discount = self.client.get_discount(
            discount_id="dsc_01h8xfbnfy4gtfd15fjgxfbrfs",
        )
        expected_discount = DiscountResponse(
            data=Discount(
                id="dsc_01h8xfbnfy4gtfd15fjgxfbrfs",
                amount="800",
                description="Test Discount Updated",
                type="flat",
                enabled_for_checkout=True,
                code="TESTDISCOUNT",
                currency_code="USD",
                recur=True,
                maximum_recurring_intervals=12,
                usage_limit=100,
                restrict_to=["pro_01h89b2j66qq82x6vn5d39c4av"],
                expires_at="2023-09-27T07:05:03.808311Z",
                status="active",
                times_used=0,
                created_at="2023-08-28T07:05:04.254Z",
                updated_at="2023-08-28T07:09:23.763Z",
            ),
            meta=dict(request_id="2379637f-ea2e-4066-8934-6341c6ef44dc"),
        )

        assert deepdiff.DeepDiff(discount, expected_discount, ignore_order=True) == {}

        assert isinstance(discount, DiscountResponse)
        assert isinstance(discount.data, Discount)
        assert str.startswith(discount.data.id, "dsc_")
        assert discount.data.amount == "800"
        assert discount.data.description == "Test Discount Updated"
        assert discount.data.type == "flat"
        assert discount.data.enabled_for_checkout == True
        assert discount.data.code == "TESTDISCOUNT"
        assert discount.data.currency_code == "USD"
        assert discount.data.recur == True
        assert discount.data.maximum_recurring_intervals == 12
        assert discount.data.usage_limit == 100
        assert discount.data.restrict_to == ["pro_01h89b2j66qq82x6vn5d39c4av"]
        assert discount.data.status == "active"
        assert discount.data.times_used == 0
        assert isinstance(discount.data.expires_at, datetime)
        assert isinstance(discount.data.created_at, datetime)
        assert isinstance(discount.data.updated_at, datetime)

    @pytest.mark.vcr
    def test_list_discounts(self):
        discounts = self.client.list_discounts(
            query_params=DiscountQueryParams(
                status="active",
            ),
        )
        expected_discounts = DiscountsResponse(
            data=[
                Discount(
                    id="dsc_01h8xfbnfy4gtfd15fjgxfbrfs",
                    amount="800",
                    description="Test Discount Updated",
                    type="flat",
                    enabled_for_checkout=True,
                    code="TESTDISCOUNT",
                    currency_code="USD",
                    recur=True,
                    maximum_recurring_intervals=12,
                    usage_limit=100,
                    restrict_to=["pro_01h89b2j66qq82x6vn5d39c4av"],
                    expires_at="2023-09-27T07:05:03.808311Z",
                    status="active",
                    times_used=0,
                    created_at="2023-08-28T07:05:04.254Z",
                    updated_at="2023-08-28T07:09:23.763Z",
                ),
            ],
            meta=dict(
                request_id="7b919b8c-2bf8-48aa-8e7a-8107146ed7c2",
                pagination=dict(
                    per_page=50,
                    next="https://sandbox-api.paddle.com/discounts?after=dsc_01h8xfbnfy4gtfd15fjgxfbrfs&status=active",
                    has_more=False,
                    estimated_total=1,
                ),
            ),
        )

        assert deepdiff.DeepDiff(discounts, expected_discounts, ignore_order=True) == {}

        assert isinstance(discounts, DiscountsResponse)
        assert isinstance(discounts.data, list)
        assert isinstance(discounts.data[0], Discount)
        assert str.startswith(discounts.data[0].id, "dsc_")
        assert discounts.data[0].amount == "800"
        assert discounts.data[0].description == "Test Discount Updated"
        assert discounts.data[0].type == "flat"
        assert discounts.data[0].enabled_for_checkout == True
        assert discounts.data[0].code == "TESTDISCOUNT"
        assert discounts.data[0].currency_code == "USD"
        assert discounts.data[0].recur == True
        assert discounts.data[0].maximum_recurring_intervals == 12
        assert discounts.data[0].usage_limit == 100
        assert discounts.data[0].restrict_to == ["pro_01h89b2j66qq82x6vn5d39c4av"]
        assert discounts.data[0].status == "active"
        assert discounts.data[0].times_used == 0
        assert isinstance(discounts.data[0].expires_at, datetime)
        assert isinstance(discounts.data[0].created_at, datetime)
        assert isinstance(discounts.data[0].updated_at, datetime)
