import os
from datetime import datetime

import deepdiff
import pytest
from apiclient import HeaderAuthentication

from paddle_billing_client.models.address import (
    Address,
    AddressesResponse,
    AddressQueryParams,
    AddressRequest,
    AddressResponse,
)


class TestAddress:
    def setup_class(self):
        from paddle_billing_client.client import PaddleApiClient  # pragma: no cover

        self.client = PaddleApiClient(
            authentication_method=HeaderAuthentication(
                token=os.getenv("PADDLE_SANDBOX_AUTH_TOKEN")
            ),
        )

    @pytest.mark.vcr
    def test_create_address_for_customer(self):
        address = self.client.create_address_for_customer(
            customer_id="ctm_01h7n2fwfhctkfja2dwq2cmx8v",
            data=AddressRequest(
                description="Head Office",
                first_line="4050 Jefferson Plaza, 41st Floor",
                city="New York",
                postal_code="10021",
                region="NY",
                country_code="US",
            ),
        )
        expected_address = AddressResponse(
            data=Address(
                id="add_01h8w4y9qfknzaq05xsd8eptjj",
                description="Head Office",
                first_line="4050 Jefferson Plaza, 41st Floor",
                second_line=None,
                city="New York",
                postal_code="10021",
                region="NY",
                country_code="US",
                status="active",
                created_at="2023-08-27T18:43:46.031Z",
                updated_at="2023-08-27T18:43:46.031Z",
            ),
            meta=dict(request_id="ef6a7bc9-4087-428d-b2f6-aee5d55d84c6"),
        )
        assert deepdiff.DeepDiff(address, expected_address, ignore_order=True) == {}

        assert isinstance(address, AddressResponse)
        assert isinstance(address.data, Address)
        assert str.startswith(address.data.id, "add_")
        assert address.data.description == "Head Office"
        assert address.data.first_line == "4050 Jefferson Plaza, 41st Floor"
        assert address.data.second_line is None
        assert address.data.city == "New York"
        assert address.data.postal_code == "10021"
        assert address.data.region == "NY"
        assert address.data.country_code == "US"
        assert address.data.status == "active"
        assert isinstance(address.data.created_at, datetime)
        assert isinstance(address.data.updated_at, datetime)

    @pytest.mark.vcr
    def test_update_address_for_customer(self):
        address = self.client.update_address_for_customer(
            customer_id="ctm_01h7n2fwfhctkfja2dwq2cmx8v",
            address_id="add_01h8w4y9qfknzaq05xsd8eptjj",
            data=AddressRequest(
                description="Head Office Updated",
                first_line="4050 Jefferson Plaza, 41st Floor",
                city="New York",
                postal_code="10021",
                region="NY",
                country_code="US",
            ),
        )
        expected_address = AddressResponse(
            data=Address(
                id="add_01h8w4y9qfknzaq05xsd8eptjj",
                description="Head Office Updated",
                first_line="4050 Jefferson Plaza, 41st Floor",
                second_line=None,
                city="New York",
                postal_code="10021",
                region="NY",
                country_code="US",
                status="active",
                created_at="2023-08-27T18:43:46.031Z",
                updated_at="2023-08-27T18:50:16.328439Z",
            ),
            meta=dict(request_id="83f66168-ca33-4ad1-b3c5-f1f7057da808"),
        )
        assert deepdiff.DeepDiff(address, expected_address, ignore_order=True) == {}

        assert isinstance(address, AddressResponse)
        assert isinstance(address.data, Address)
        assert str.startswith(address.data.id, "add_")
        assert address.data.description == "Head Office Updated"
        assert address.data.first_line == "4050 Jefferson Plaza, 41st Floor"
        assert address.data.second_line is None
        assert address.data.city == "New York"
        assert address.data.postal_code == "10021"
        assert address.data.region == "NY"
        assert address.data.country_code == "US"
        assert address.data.status == "active"
        assert isinstance(address.data.created_at, datetime)
        assert isinstance(address.data.updated_at, datetime)

    @pytest.mark.vcr
    def test_get_address_for_customer(self):
        address = self.client.get_address_for_customer(
            customer_id="ctm_01h7n2fwfhctkfja2dwq2cmx8v",
            address_id="add_01h8w4y9qfknzaq05xsd8eptjj",
        )
        expected_address = AddressResponse(
            data=Address(
                id="add_01h8w4y9qfknzaq05xsd8eptjj",
                description="Head Office Updated",
                first_line="4050 Jefferson Plaza, 41st Floor",
                second_line=None,
                city="New York",
                postal_code="10021",
                region="NY",
                country_code="US",
                status="active",
                created_at="2023-08-27T18:43:46.031Z",
                updated_at="2023-08-27T18:50:16.328439Z",
            ),
            meta=dict(request_id="f80b049f-27f1-4531-ac79-bad5ca448797"),
        )
        assert deepdiff.DeepDiff(address, expected_address, ignore_order=True) == {}

        assert isinstance(address, AddressResponse)
        assert isinstance(address.data, Address)
        assert str.startswith(address.data.id, "add_")
        assert address.data.description == "Head Office Updated"
        assert address.data.first_line == "4050 Jefferson Plaza, 41st Floor"
        assert address.data.second_line is None
        assert address.data.city == "New York"
        assert address.data.postal_code == "10021"
        assert address.data.region == "NY"
        assert address.data.country_code == "US"
        assert address.data.status == "active"
        assert isinstance(address.data.created_at, datetime)
        assert isinstance(address.data.updated_at, datetime)

    @pytest.mark.vcr
    def test_list_addresses_for_customer(self):
        addresses = self.client.list_addresses_for_customer(
            customer_id="ctm_01h7n2fwfhctkfja2dwq2cmx8v",
            query_params=AddressQueryParams(
                status="active",
            ),
        )
        expected_addresses = AddressesResponse(
            data=[
                Address(
                    id="add_01h8w4y9qfknzaq05xsd8eptjj",
                    description="Head Office Updated",
                    first_line="4050 Jefferson Plaza, 41st Floor",
                    second_line=None,
                    city="New York",
                    postal_code="10021",
                    region="NY",
                    country_code="US",
                    status="active",
                    created_at="2023-08-27T18:43:46.031Z",
                    updated_at="2023-08-27T18:50:16.328439Z",
                ),
            ],
            meta=dict(
                request_id="beb10a9c-b1d8-470e-9087-20378beaaffa",
                pagination=dict(
                    per_page=50,
                    next="https://sandbox-api.paddle.com/customers/ctm_01h7n2fwfhctkfja2dwq2cmx8v/addresses?after=add_01h8w4y9qfknzaq05xsd8eptjj&status=active",
                    has_more=False,
                    estimated_total=1,
                ),
            ),
        )
        assert deepdiff.DeepDiff(addresses, expected_addresses, ignore_order=True) == {}

        assert isinstance(addresses, AddressesResponse)
        assert isinstance(addresses.data, list)
        assert len(addresses.data) == 1
        assert isinstance(addresses.data[0], Address)
        assert str.startswith(addresses.data[0].id, "add_")
        assert addresses.data[0].description == "Head Office Updated"
        assert addresses.data[0].first_line == "4050 Jefferson Plaza, 41st Floor"
        assert addresses.data[0].second_line is None
        assert addresses.data[0].city == "New York"
        assert addresses.data[0].postal_code == "10021"
        assert addresses.data[0].region == "NY"
        assert addresses.data[0].country_code == "US"
        assert addresses.data[0].status == "active"
        assert isinstance(addresses.data[0].created_at, datetime)
        assert isinstance(addresses.data[0].updated_at, datetime)
