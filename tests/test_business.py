import os
from datetime import datetime

import deepdiff
import pytest
from apiclient.authentication_methods import HeaderAuthentication

from paddle_billing_client.models.business import (
    Business,
    BusinessesResponse,
    BusinessQueryParams,
    BusinessRequest,
    BusinessResponse,
    Contact,
)


class TestBusiness:
    def setup_class(self):
        from paddle_billing_client.client import PaddleApiClient  # pragma: no cover

        self.client = PaddleApiClient(
            authentication_method=HeaderAuthentication(
                token=os.getenv("PADDLE_SANDBOX_AUTH_TOKEN")
            ),
        )

    @pytest.mark.vcr
    def test_create_business_for_customer(self):
        """
        name: str
        company_number: str
        tax_identifier: str
        contacts: List[Contact]
        status: Optional[Literal["active", "archived"]]
        """
        business = self.client.create_business_for_customer(
            customer_id="ctm_01h8w66qa8djqjhmdkth2fnebk",
            data=BusinessRequest(
                name="Test Business",
                company_number="123456789",
                tax_identifier="123456789",
                contacts=[
                    dict(
                        name="Test Contact",
                        email="asd@asd.com",
                    ),
                ],
            ),
        )
        expected_business = BusinessResponse(
            data=Business(
                id="biz_01h8xg9dgqkehwp72x067vems9",
                customer_id="ctm_01h8w66qa8djqjhmdkth2fnebk",
                name="Test Business",
                company_number="123456789",
                tax_identifier="123456789",
                contacts=[
                    dict(
                        name="Test Contact",
                        email="asd@asd.com",
                    ),
                ],
                status="active",
                created_at="2023-08-28T07:21:19.127Z",
                updated_at="2023-08-28T07:21:19.127Z",
            ),
            meta=dict(request_id="9719e336-ffbe-443c-9dad-0ab57f21946c"),
        )

        assert deepdiff.DeepDiff(business, expected_business, ignore_order=True) == {}

        assert isinstance(business, BusinessResponse)
        assert isinstance(business.data, Business)
        assert str.startswith(business.data.id, "biz_")
        assert business.data.name == "Test Business"
        assert business.data.company_number == "123456789"
        assert business.data.tax_identifier == "123456789"
        assert business.data.contacts == [
            Contact(
                name="Test Contact",
                email="asd@asd.com",
            ),
        ]
        assert business.data.status == "active"
        assert isinstance(business.data.created_at, datetime)
        assert isinstance(business.data.updated_at, datetime)

    @pytest.mark.vcr
    def test_update_business_for_customer(self):
        business = self.client.update_business_for_customer(
            customer_id="ctm_01h8w66qa8djqjhmdkth2fnebk",
            business_id="biz_01h8xg9dgqkehwp72x067vems9",
            data=BusinessRequest(
                name="Test Business 2",
                company_number="123456789",
                tax_identifier="123456789",
                contacts=[
                    dict(
                        name="Test Contact",
                        email="asd@asd.com",
                    ),
                ],
            ),
        )
        expected_business = BusinessResponse(
            data=Business(
                id="biz_01h8xg9dgqkehwp72x067vems9",
                customer_id="ctm_01h8w66qa8djqjhmdkth2fnebk",
                name="Test Business 2",
                company_number="123456789",
                tax_identifier="123456789",
                contacts=[
                    dict(
                        name="Test Contact",
                        email="asd@asd.com",
                    ),
                ],
                status="active",
                created_at="2023-08-28T07:21:19.127Z",
                updated_at="2023-08-28T07:26:54.983533Z",
            ),
            meta=dict(request_id="7cdb6f2f-192f-42e2-ba43-89abdb8ecc9d"),
        )

        assert deepdiff.DeepDiff(business, expected_business, ignore_order=True) == {}

        assert isinstance(business, BusinessResponse)
        assert isinstance(business.data, Business)
        assert str.startswith(business.data.id, "biz_")
        assert business.data.name == "Test Business 2"
        assert business.data.company_number == "123456789"
        assert business.data.tax_identifier == "123456789"
        assert business.data.contacts == [
            Contact(
                name="Test Contact",
                email="asd@asd.com",
            ),
        ]
        assert business.data.status == "active"
        assert isinstance(business.data.created_at, datetime)
        assert isinstance(business.data.updated_at, datetime)

    @pytest.mark.vcr
    def test_get_business_for_customer(self):
        business = self.client.get_business_for_customer(
            customer_id="ctm_01h8w66qa8djqjhmdkth2fnebk",
            business_id="biz_01h8xg9dgqkehwp72x067vems9",
        )
        expected_business = BusinessResponse(
            data=Business(
                id="biz_01h8xg9dgqkehwp72x067vems9",
                customer_id="ctm_01h8w66qa8djqjhmdkth2fnebk",
                name="Test Business 2",
                company_number="123456789",
                tax_identifier="123456789",
                contacts=[
                    dict(
                        name="Test Contact",
                        email="asd@asd.com",
                    ),
                ],
                status="active",
                created_at="2023-08-28T07:21:19.127Z",
                updated_at="2023-08-28T07:26:54.983533Z",
            ),
            meta=dict(request_id="ed450d42-5332-4c29-9754-858fe55639d0"),
        )

        assert deepdiff.DeepDiff(business, expected_business, ignore_order=True) == {}

        assert isinstance(business, BusinessResponse)
        assert isinstance(business.data, Business)
        assert str.startswith(business.data.id, "biz_")
        assert business.data.name == "Test Business 2"
        assert business.data.company_number == "123456789"
        assert business.data.tax_identifier == "123456789"
        assert business.data.contacts == [
            Contact(
                name="Test Contact",
                email="asd@asd.com",
            ),
        ]
        assert business.data.status == "active"
        assert isinstance(business.data.created_at, datetime)
        assert isinstance(business.data.updated_at, datetime)

    @pytest.mark.vcr
    def test_list_businesses_for_customer(self):
        businesses = self.client.list_businesses_for_customer(
            customer_id="ctm_01h8w66qa8djqjhmdkth2fnebk",
            query_params=BusinessQueryParams(
                status="active",
            ),
        )
        expected_businesses = BusinessesResponse(
            data=[
                Business(
                    id="biz_01h8xg9dgqkehwp72x067vems9",
                    customer_id="ctm_01h8w66qa8djqjhmdkth2fnebk",
                    name="Test Business 2",
                    company_number="123456789",
                    tax_identifier="123456789",
                    contacts=[
                        dict(
                            name="Test Contact",
                            email="asd@asd.com",
                        ),
                    ],
                    status="active",
                    created_at="2023-08-28T07:21:19.127Z",
                    updated_at="2023-08-28T07:26:54.983533Z",
                ),
            ],
            meta=dict(
                request_id="880590b7-599e-49f3-b883-df5444fb8c5e",
                pagination=dict(
                    per_page=50,
                    next="https://sandbox-api.paddle.com/customers/ctm_01h8w66qa8djqjhmdkth2fnebk/businesses?after"
                    "=biz_01h8xg9dgqkehwp72x067vems9&status=active",
                    has_more=False,
                    estimated_total=1,
                ),
            ),
        )

        assert (
            deepdiff.DeepDiff(businesses, expected_businesses, ignore_order=True) == {}
        )

        assert isinstance(businesses, BusinessesResponse)
        assert isinstance(businesses.data, list)
        assert len(businesses.data) == 1
        assert isinstance(businesses.data[0], Business)
        assert str.startswith(businesses.data[0].id, "biz_")
        assert businesses.data[0].name == "Test Business 2"
        assert businesses.data[0].company_number == "123456789"
        assert businesses.data[0].tax_identifier == "123456789"
        assert businesses.data[0].contacts == [
            Contact(
                name="Test Contact",
                email="asd@asd.com",
            ),
        ]
        assert businesses.data[0].status == "active"
        assert isinstance(businesses.data[0].created_at, datetime)
        assert isinstance(businesses.data[0].updated_at, datetime)
