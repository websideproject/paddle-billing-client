import functools

from paddle_billing_client.models.address import Address
from paddle_billing_client.models.adjustment import Adjustment
from paddle_billing_client.models.business import Business
from paddle_billing_client.models.customer import Customer
from paddle_billing_client.models.price import Price
from paddle_billing_client.models.product import Product
from paddle_billing_client.models.subscription import Subscription
from paddle_billing_client.models.transaction import Transaction


def parse_event_to_model(event_type: str, data):
    if not isinstance(data, dict):
        return data
    if event_type.startswith("subscription"):
        return Subscription(**data)
    elif event_type.startswith("transaction"):
        return Transaction(**data)
    elif event_type.startswith("customer"):
        return Customer(**data)
    elif event_type.startswith("product"):
        return Product(**data)
    elif event_type.startswith("price"):
        return Price(**data)
    elif event_type.startswith("address"):
        return Address(**data)
    elif event_type.startswith("business"):
        return Business(**data)
    elif event_type.startswith("adjustment"):
        return Adjustment(**data)
    return data
