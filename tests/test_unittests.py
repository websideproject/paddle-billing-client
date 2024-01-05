import pytest

from paddle_billing_client.models.address import AddressQueryParams
from paddle_billing_client.models.adjustment import AdjustmentQueryParams
from paddle_billing_client.models.business import BusinessQueryParams
from paddle_billing_client.models.customer import CustomerQueryParams
from paddle_billing_client.models.discount import DiscountQueryParams
from paddle_billing_client.models.event import EventQueryParams
from paddle_billing_client.models.notification import NotificationQueryParams
from paddle_billing_client.models.price import PriceQueryParams
from paddle_billing_client.models.product import ProductQueryParams
from paddle_billing_client.models.subscription import SubscriptionQueryParams
from paddle_billing_client.models.transaction import TransactionQueryParams


def test_address_query_params_valid():
    query_params = {
        "status": "active",
    }
    AddressQueryParams(**query_params)


def test_address_query_params_invalid():
    query_params = {
        "status": "invalid",
    }
    with pytest.raises(ValueError):
        AddressQueryParams(**query_params)


def test_adjustment_query_params_valid():
    query_params = {
        "status": "pending_approval,approved,rejected",
    }
    AdjustmentQueryParams(**query_params)


def test_adjustment_query_params_invalid():
    query_params = {
        "status": "invalid",
    }
    with pytest.raises(ValueError):
        AdjustmentQueryParams(**query_params)


def test_business_query_params_valid():
    query_params = {
        "status": "active",
    }
    BusinessQueryParams(**query_params)


def test_business_query_params_invalid():
    query_params = {
        "status": "invalid",
    }
    with pytest.raises(ValueError):
        BusinessQueryParams(**query_params)


def test_customer_query_params_valid():
    query_params = {
        "status": "active",
    }
    CustomerQueryParams(**query_params)


def test_customer_query_params_invalid():
    query_params = {
        "status": "invalid",
    }
    with pytest.raises(ValueError):
        CustomerQueryParams(**query_params)


def test_discount_query_params_valid():
    query_params = {
        "status": "active",
    }
    DiscountQueryParams(**query_params)


def test_discount_query_params_invalid():
    query_params = {
        "status": "invalid",
    }
    with pytest.raises(ValueError):
        DiscountQueryParams(**query_params)


def test_notification_query_params_valid():
    query_params = {
        "status": "delivered",
    }
    NotificationQueryParams(**query_params)


def test_notification_query_params_invalid():
    query_params = {
        "status": "invalid",
    }
    with pytest.raises(ValueError):
        NotificationQueryParams(**query_params)


def test_price_query_params_valid():
    query_params = {
        "status": "active",
    }
    PriceQueryParams(**query_params)


def test_price_query_params_invalid():
    query_params = {
        "status": "invalid",
    }
    with pytest.raises(ValueError):
        PriceQueryParams(**query_params)


def test_product_query_params_valid():
    query_params = {
        "status": "active",
    }
    ProductQueryParams(**query_params)


def test_product_query_params_invalid():
    query_params = {
        "status": "invalid",
    }
    with pytest.raises(ValueError):
        ProductQueryParams(**query_params)


def test_subscription_query_params_valid():
    query_params = {
        "status": "active",
    }
    SubscriptionQueryParams(**query_params)


def test_subscription_query_params_invalid():
    query_params = {
        "status": "invalid",
    }
    with pytest.raises(ValueError):
        SubscriptionQueryParams(**query_params)


def test_transaction_query_params_valid():
    query_params = {
        "status": "billed,completed",
    }
    TransactionQueryParams(**query_params)


def test_transaction_query_params_invalid():
    query_params = {
        "status": "invalid",
    }
    with pytest.raises(ValueError):
        TransactionQueryParams(**query_params)
