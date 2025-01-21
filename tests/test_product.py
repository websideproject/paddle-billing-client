import os
from datetime import datetime

import deepdiff
import pytest
from apiclient.authentication_methods import HeaderAuthentication

from paddle_billing_client.models.product import (
    Product,
    ProductRequest,
    ProductResponse,
    ProductsResponse,
)


class TestProduct:
    def setup_class(self):
        from paddle_billing_client.client import PaddleApiClient  # pragma: no cover

        self.client = PaddleApiClient(
            authentication_method=HeaderAuthentication(
                token=os.getenv("PADDLE_SANDBOX_AUTH_TOKEN")
            ),
        )

    @pytest.mark.vcr
    def test_product_create(self):
        product = self.client.create_product(
            ProductRequest(
                name="Test Product New",
                tax_category="standard",
                description="Test Product Description",
                image_url="https://example.com/image.png",
                custom_data=dict(foo="bar"),
            )
        )
        expected_product = ProductResponse(
            data=Product(
                id="pro_01h89b2j66qq82x6vn5d39c4av",
                name="Test Product New",
                description="Test Product Description",
                image_url="https://example.com/image.png",
                custom_data=dict(foo="bar"),
                tax_category="standard",
                status="active",
                created_at="2023-08-20T11:25:23.014Z",
            ),
            meta=dict(request_id="492e8db0-d230-495d-86ae-ca74cf53a78e"),
        )
        assert (
            deepdiff.DeepDiff(
                product,
                expected_product,
                ignore_order=True,
                exclude_regex_paths=r".+\.model_fields_set",
            )
            == {}
        )

        assert isinstance(product, ProductResponse)
        assert isinstance(product.data, Product)
        assert str.startswith(product.data.id, "pro_")
        assert product.data.name == "Test Product New"
        assert product.data.description == "Test Product Description"
        assert product.data.image_url == "https://example.com/image.png"
        assert product.data.custom_data == dict(foo="bar")
        assert product.data.tax_category == "standard"
        assert product.data.status == "active"
        assert isinstance(product.data.created_at, datetime)

    @pytest.mark.vcr
    def test_product_update(self):
        updated_product = self.client.update_product(
            "pro_01h89b2j66qq82x6vn5d39c4av",
            ProductRequest(
                name="Test Product New 2",
                tax_category="standard",
                description="Test Product Description",
                image_url="https://example.com/image.png",
                custom_data=dict(foo="bar2"),
            ),
        )
        expected_product = ProductResponse(
            data=Product(
                id="pro_01h89b2j66qq82x6vn5d39c4av",
                name="Test Product New 2",
                description="Test Product Description",
                image_url="https://example.com/image.png",
                custom_data=dict(foo="bar2"),
                tax_category="standard",
                status="active",
                created_at="2023-08-20T11:25:23.014Z",
            ),
            meta=dict(request_id="06710870-10ae-40d4-87a3-6dbd107ed1c2"),
        )
        assert (
            deepdiff.DeepDiff(
                updated_product,
                expected_product,
                ignore_order=True,
                exclude_regex_paths=r".+\.model_fields_set",
            )
            == {}
        )

    @pytest.mark.vcr
    def test_product_get(self):
        product = self.client.get_product("pro_01h89b2j66qq82x6vn5d39c4av")
        expected_product = ProductResponse(
            data=Product(
                id="pro_01h89b2j66qq82x6vn5d39c4av",
                name="Test Product New 2",
                description="Test Product Description",
                image_url="https://example.com/image.png",
                custom_data=dict(foo="bar2"),
                tax_category="standard",
                status="active",
                created_at="2023-08-20T11:25:23.014Z",
            ),
            meta=dict(request_id="f3d5a132-493b-4111-9143-d600869121e7"),
        )

        assert (
            deepdiff.DeepDiff(
                product,
                expected_product,
                ignore_order=True,
                exclude_regex_paths=r".+\.model_fields_set",
            )
            == {}
        )

    @pytest.mark.vcr
    def test_product_list(self):
        products = self.client.list_products()
        expected_products = ProductsResponse(
            data=[
                Product(
                    id="pro_01h89b2j66qq82x6vn5d39c4av",
                    name="Test Product New 2",
                    description="Test Product Description",
                    image_url="https://example.com/image.png",
                    custom_data=dict(foo="bar2"),
                    tax_category="standard",
                    status="active",
                    created_at="2023-08-20T11:25:23.014Z",
                ),
                Product(
                    id="pro_01h81jnhdrz5wfde6cn8wg9y1y",
                    name="Test Product New",
                    description="Test Product Description",
                    image_url="https://example.com/image.png",
                    custom_data=dict(foo="bar"),
                    tax_category="standard",
                    status="active",
                    created_at="2023-08-17T11:04:09.4Z",
                ),
            ],
            meta=dict(
                request_id="7c4b0302-a257-4609-b250-e6ba55c815e5",
                pagination=dict(
                    per_page=50,
                    next="https://sandbox-api.paddle.com/products?after=pro_01h7mrm9f0xvrvvwvkg1b7q8e3",
                    has_more=False,
                    estimated_total=7,
                ),
            ),
        )

        assert (
            deepdiff.DeepDiff(
                products,
                expected_products,
                ignore_order=True,
                exclude_regex_paths=r".+\.model_fields_set",
            )
            == {}
        )
