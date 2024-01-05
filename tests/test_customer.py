import os
from datetime import datetime

import deepdiff
import pytest
from apiclient import HeaderAuthentication

from paddle_billing_client.models.customer import (
    Customer,
    CustomerQueryParams,
    CustomerRequest,
    CustomerResponse,
    CustomersResponse,
)


class TestCustomer:
    def setup_class(self):
        from paddle_billing_client.client import PaddleApiClient  # pragma: no cover

        self.client = PaddleApiClient(
            authentication_method=HeaderAuthentication(
                token=os.getenv("PADDLE_SANDBOX_AUTH_TOKEN")
            ),
        )

    """
    create_customer: str = "customers"
    get_customer: str = "customers/{customer_id}"
    list_customers: str = "customers"
    update_customer: str = "customers/{customer_id}"
    """

    @pytest.mark.vcr
    def test_create_customer(self):
        customer = self.client.create_customer(
            data=CustomerRequest(
                name="Test Customer",
                email="asd1234@asd.com",
            )
        )
        expected_customer = CustomerResponse(
            data=Customer(
                id="ctm_01h8w66qa8djqjhmdkth2fnebk",
                name="Test Customer",
                email="asd1234@asd.com",
                locale="en",
                status="active",
                marketing_consent=False,
                created_at="2023-08-27T19:05:50.664Z",
                updated_at="2023-08-27T19:05:50.664Z",
                imported_at=None,
                source=None,
            ),
            meta=dict(request_id="e29fd968-27c5-4362-8503-3b56664d8fbe"),
        )
        assert (
            deepdiff.DeepDiff(
                customer,
                expected_customer,
                ignore_order=True,
                exclude_regex_paths=r".+\.model_fields_set",
            )
            == {}
        )

        assert isinstance(customer, CustomerResponse)
        assert isinstance(customer.data, Customer)
        assert str.startswith(customer.data.id, "ctm_")
        assert customer.data.name == "Test Customer"
        assert customer.data.email == "asd1234@asd.com"
        assert customer.data.locale == "en"
        assert customer.data.status == "active"
        assert customer.data.marketing_consent is False
        assert isinstance(customer.data.created_at, datetime)
        assert isinstance(customer.data.updated_at, datetime)
        assert customer.data.imported_at is None
        assert customer.data.source is None

    @pytest.mark.vcr
    def test_update_customer(self):
        customer = self.client.update_customer(
            customer_id="ctm_01h8w66qa8djqjhmdkth2fnebk",
            data=CustomerRequest(
                name="Test Customer 2",
                email="asd123@asd.com",
            ),
        )
        expected_customer = CustomerResponse(
            data=Customer(
                id="ctm_01h8w66qa8djqjhmdkth2fnebk",
                name="Test Customer 2",
                email="asd123@asd.com",
                locale="en",
                status="active",
                marketing_consent=False,
                created_at="2023-08-27T19:05:50.664Z",
                updated_at="2023-08-27T19:12:16.802971Z",
                imported_at=None,
                source=None,
            ),
            meta=dict(request_id="53538604-e97c-488f-8e8e-baa80c9dfc6d"),
        )

        assert (
            deepdiff.DeepDiff(
                customer,
                expected_customer,
                ignore_order=True,
                exclude_regex_paths=r".+\.model_fields_set",
            )
            == {}
        )

        assert isinstance(customer, CustomerResponse)
        assert isinstance(customer.data, Customer)
        assert str.startswith(customer.data.id, "ctm_")
        assert customer.data.name == "Test Customer 2"
        assert customer.data.email == "asd123@asd.com"
        assert customer.data.locale == "en"
        assert customer.data.status == "active"
        assert customer.data.marketing_consent is False
        assert isinstance(customer.data.created_at, datetime)
        assert isinstance(customer.data.updated_at, datetime)
        assert customer.data.imported_at is None
        assert customer.data.source is None

    @pytest.mark.vcr
    def test_get_customer(self):
        customer = self.client.get_customer(
            customer_id="ctm_01h8w66qa8djqjhmdkth2fnebk",
        )
        expected_customer = CustomerResponse(
            data=Customer(
                id="ctm_01h8w66qa8djqjhmdkth2fnebk",
                name="Test Customer 2",
                email="asd123@asd.com",
                locale="en",
                status="active",
                marketing_consent=False,
                created_at="2023-08-27T19:05:50.664Z",
                updated_at="2023-08-27T19:12:16.802971Z",
                imported_at=None,
                source=None,
            ),
            meta=dict(request_id="a7fb5f17-64cb-4539-b041-d067df13f791"),
        )

        assert (
            deepdiff.DeepDiff(
                customer,
                expected_customer,
                ignore_order=True,
                exclude_regex_paths=r".+\.model_fields_set",
            )
            == {}
        )

        assert isinstance(customer, CustomerResponse)
        assert isinstance(customer.data, Customer)
        assert str.startswith(customer.data.id, "ctm_")
        assert customer.data.name == "Test Customer 2"
        assert customer.data.email == "asd123@asd.com"
        assert customer.data.locale == "en"
        assert customer.data.status == "active"
        assert customer.data.marketing_consent is False
        assert isinstance(customer.data.created_at, datetime)
        assert isinstance(customer.data.updated_at, datetime)
        assert customer.data.imported_at is None
        assert customer.data.source is None

    @pytest.mark.vcr
    def test_list_customers(self):
        customers = self.client.list_customers(
            query_params=CustomerQueryParams(
                status="active",
            )
        )
        expected_customers = CustomersResponse(
            data=[
                Customer(
                    id="ctm_01h8w66qa8djqjhmdkth2fnebk",
                    name="Test Customer 2",
                    email="asd123@asd.com",
                    locale="en",
                    status="active",
                    marketing_consent=False,
                    created_at="2023-08-27T19:05:50.664Z",
                    updated_at="2023-08-27T19:12:16.802971Z",
                    imported_at=None,
                    source=None,
                ),
            ],
            meta=dict(
                request_id="a990372f-4438-44f9-9678-61ee4eccc1d8",
                pagination=dict(
                    per_page=50,
                    next="https://sandbox-api.paddle.com/customers?after=ctm_01h7mrr5j8rnawwzh9nschgp1v&status=active",
                    has_more=False,
                    estimated_total=1,
                ),
            ),
        )

        assert deepdiff.DeepDiff(customers, expected_customers, ignore_order=True) == {}

        assert isinstance(customers, CustomersResponse)
        assert isinstance(customers.data, list)
        assert len(customers.data) == 1
        assert isinstance(customers.data[0], Customer)
        assert str.startswith(customers.data[0].id, "ctm_")
        assert customers.data[0].name == "Test Customer 2"
        assert customers.data[0].email == "asd123@asd.com"
        assert customers.data[0].locale == "en"
        assert customers.data[0].status == "active"
        assert customers.data[0].marketing_consent is False
        assert isinstance(customers.data[0].created_at, datetime)
        assert isinstance(customers.data[0].updated_at, datetime)
        assert customers.data[0].imported_at is None
        assert customers.data[0].source is None
