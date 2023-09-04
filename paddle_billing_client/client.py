from __future__ import annotations

from typing import Optional

import logging

from apiclient import (
    APIClient,
    HeaderAuthentication,
    JsonRequestFormatter,
    JsonResponseHandler,
)
from apiclient_pydantic import serialize_all_methods

from paddle_billing_client.endpoints import Endpoints
from paddle_billing_client.formatters import CustomJsonRequestFormatter
from paddle_billing_client.models.address import (
    AddressesResponse,
    AddressQueryParams,
    AddressRequest,
    AddressResponse,
)
from paddle_billing_client.models.adjustment import (
    AdjustmentQueryParams,
    AdjustmentRequest,
    AdjustmentResponse,
    AdjustmentsResponse,
)
from paddle_billing_client.models.business import (
    BusinessesResponse,
    BusinessQueryParams,
    BusinessRequest,
    BusinessResponse,
)
from paddle_billing_client.models.customer import (
    CustomerQueryParams,
    CustomerRequest,
    CustomerResponse,
    CustomersResponse,
)
from paddle_billing_client.models.discount import (
    DiscountQueryParams,
    DiscountRequest,
    DiscountResponse,
    DiscountsResponse,
)
from paddle_billing_client.models.event import EventsResponse, EventTypesResponse
from paddle_billing_client.models.notification import (
    NotificationQueryParams,
    NotificationReplayResponse,
    NotificationResponse,
    NotificationsResponse,
)
from paddle_billing_client.models.notification_setting import (
    NotificationSettingRequest,
    NotificationSettingResponse,
    NotificationSettingsResponse,
)
from paddle_billing_client.models.price import (
    PriceQueryParams,
    PriceRequest,
    PriceResponse,
    PricesResponse,
)
from paddle_billing_client.models.product import (
    ProductQueryParams,
    ProductRequest,
    ProductResponse,
    ProductsResponse,
)
from paddle_billing_client.models.subscription import (
    SubscriptionQueryParams,
    SubscriptionRequest,
    SubscriptionResponse,
    SubscriptionsResponse,
)
from paddle_billing_client.models.transaction import (
    TransactionPdfResponse,
    TransactionPreviewResponse,
    TransactionQueryParams,
    TransactionRequest,
    TransactionResponse,
    TransactionsResponse,
)


@serialize_all_methods()
class PaddleApiClient(APIClient):
    def __init__(
        self,
        base_url="https://sandbox-api.paddle.com",
        request_formatter=CustomJsonRequestFormatter,
        response_handler=JsonResponseHandler,
        **kwargs,
    ):
        self.endpoints: Endpoints = Endpoints(base_url=base_url)
        super().__init__(
            request_formatter=request_formatter,
            response_handler=response_handler,
            **kwargs,
        )

    """
    Products
    """

    def create_product(self, data: ProductRequest) -> ProductResponse:
        """Create a product"""
        return self.post(self.endpoints.create_product, dict(data))

    def get_product(self, product_id: str) -> ProductResponse:
        """Get a product"""
        return self.get(self.endpoints.get_product.format(product_id=product_id))

    def list_products(
        self, query_params: ProductQueryParams = None
    ) -> ProductsResponse:
        """List all products"""
        return self.get(self.endpoints.list_products, params=dict(query_params))

    def update_product(self, product_id: str, data: ProductRequest) -> ProductResponse:
        """Update a product"""
        return self.patch(
            self.endpoints.update_product.format(product_id=product_id), dict(data)
        )

    """
    Prices
    """

    def create_price(self, data: PriceRequest) -> PriceResponse:
        """Create a price"""
        return self.post(self.endpoints.create_price, dict(data))

    def get_price(self, price_id: str) -> PriceResponse:
        """Get a price"""
        return self.get(self.endpoints.get_price.format(price_id=price_id))

    def list_prices(self, query_params: PriceQueryParams = None) -> PricesResponse:
        """List all prices"""
        return self.get(self.endpoints.list_prices, params=dict(query_params))

    def update_price(self, price_id: str, data: PriceRequest) -> PriceResponse:
        """Update a price"""
        return self.patch(
            self.endpoints.update_price.format(price_id=price_id), dict(data)
        )

    """
    Discounts
    """

    def create_discount(self, data: DiscountRequest) -> DiscountResponse:
        """Create a discount"""
        return self.post(self.endpoints.create_discount, dict(data))

    def get_discount(self, discount_id: str) -> DiscountResponse:
        """Get a discount"""
        return self.get(self.endpoints.get_discount.format(discount_id=discount_id))

    def list_discounts(
        self, query_params: DiscountQueryParams = None
    ) -> DiscountsResponse:
        """List all discounts"""
        return self.get(self.endpoints.list_discounts, params=dict(query_params))

    def update_discount(
        self, discount_id: str, data: DiscountRequest
    ) -> DiscountResponse:
        """Update a discount"""
        return self.patch(
            self.endpoints.update_discount.format(discount_id=discount_id), dict(data)
        )

    """
    Customers
    """

    def create_customer(self, data: CustomerRequest) -> CustomerResponse:
        """Create a customer"""
        return self.post(self.endpoints.create_customer, dict(data))

    def get_customer(self, customer_id: str) -> CustomerResponse:
        """Get a customer"""
        return self.get(self.endpoints.get_customer.format(customer_id=customer_id))

    def list_customers(
        self, query_params: CustomerQueryParams = None
    ) -> CustomersResponse:
        """List all customers"""
        return self.get(self.endpoints.list_customers, params=dict(query_params))

    def update_customer(
        self, customer_id: str, data: CustomerRequest
    ) -> CustomerResponse:
        """Update a customer"""
        return self.patch(
            self.endpoints.update_customer.format(customer_id=customer_id), dict(data)
        )

    """
    Addresses
    """

    def create_address_for_customer(
        self, customer_id: str, data: AddressRequest
    ) -> AddressResponse:
        """Create an address for a customer"""
        return self.post(
            self.endpoints.create_address_for_customer.format(customer_id=customer_id),
            dict(data),
        )

    def get_address_for_customer(
        self, customer_id: str, address_id: str
    ) -> AddressResponse:
        """Get an address for a customer"""
        return self.get(
            self.endpoints.get_address_for_customer.format(
                customer_id=customer_id, address_id=address_id
            )
        )

    def list_addresses_for_customer(
        self, customer_id: str, query_params: AddressQueryParams = None
    ) -> AddressesResponse:
        """List all addresses for a customer"""
        return self.get(
            self.endpoints.list_addresses_for_customer.format(customer_id=customer_id),
            params=dict(query_params),
        )

    def update_address_for_customer(
        self, customer_id: str, address_id: str, data: AddressRequest
    ) -> AddressResponse:
        """Update an address for a customer"""
        return self.patch(
            self.endpoints.update_address_for_customer.format(
                customer_id=customer_id, address_id=address_id
            ),
            dict(data),
        )

    """
    Businesses
    """

    def create_business_for_customer(
        self, customer_id: str, data: BusinessRequest
    ) -> BusinessResponse:
        """Create a business for a customer"""
        return self.post(
            self.endpoints.create_business_for_customer.format(customer_id=customer_id),
            dict(data),
        )

    def get_business_for_customer(
        self, customer_id: str, business_id: str
    ) -> BusinessResponse:
        """Get a business for a customer"""
        return self.get(
            self.endpoints.get_business_for_customer.format(
                customer_id=customer_id, business_id=business_id
            )
        )

    def list_businesses_for_customer(
        self, customer_id: str, query_params: BusinessQueryParams = None
    ) -> BusinessesResponse:
        """List all businesses for a customer"""
        return self.get(
            self.endpoints.list_businesses_for_customer.format(customer_id=customer_id),
            params=dict(query_params),
        )

    def update_business_for_customer(
        self, customer_id: str, business_id: str, data: BusinessRequest
    ) -> BusinessResponse:
        """Update a business for a customer"""
        return self.patch(
            self.endpoints.update_business_for_customer.format(
                customer_id=customer_id, business_id=business_id
            ),
            dict(data),
        )

    """
    Transactions
    """

    def create_transaction(
        self,
        data: TransactionRequest,
        query_params: TransactionQueryParams = None,
    ) -> TransactionResponse:
        """Create a transaction"""
        return self.post(
            self.endpoints.create_transaction, dict(data), params=dict(query_params)
        )

    def get_transaction(
        self, transaction_id: str, query_params: TransactionQueryParams = None
    ) -> TransactionResponse:
        """Get a transaction"""
        return self.get(
            self.endpoints.get_transaction.format(transaction_id=transaction_id),
            params=dict(query_params),
        )

    def list_transactions(
        self, query_params: TransactionQueryParams = None
    ) -> TransactionsResponse:
        """List all transactions"""
        return self.get(self.endpoints.list_transactions, params=dict(query_params))

    def update_transaction(
        self,
        transaction_id: str,
        data: TransactionRequest,
        query_params: TransactionQueryParams = None,
    ) -> TransactionResponse:
        """Update a transaction"""
        return self.patch(
            self.endpoints.update_transaction.format(transaction_id=transaction_id),
            dict(data),
            params=dict(query_params),
        )

    def preview_transaction(
        self, data: TransactionRequest, query_params: TransactionQueryParams = None
    ) -> TransactionPreviewResponse:
        """Preview a transaction"""
        return self.post(
            self.endpoints.preview_transaction, dict(data), params=dict(query_params)
        )

    def preview_prices(self, data: TransactionRequest) -> TransactionResponse:
        """Preview prices"""
        return self.post(self.endpoints.preview_prices, dict(data))

    def get_pdf_for_transaction(self, transaction_id: str) -> TransactionPdfResponse:
        """Get a PDF for a transaction"""
        return self.get(
            self.endpoints.get_pdf_for_transaction.format(transaction_id=transaction_id)
        )

    """
    Subscriptions
    """

    def get_subscription(self, subscription_id: str) -> SubscriptionResponse:
        """Get a subscription"""
        return self.get(
            self.endpoints.get_subscription.format(subscription_id=subscription_id)
        )

    def list_subscriptions(
        self, query_params: SubscriptionQueryParams = None
    ) -> SubscriptionsResponse:
        """List all subscriptions"""
        return self.get(self.endpoints.list_subscriptions, params=dict(query_params))

    def preview_update_subscription(
        self, subscription_id: str, data: SubscriptionRequest
    ) -> SubscriptionResponse:
        """Preview an update to a subscription"""
        return self.patch(
            self.endpoints.preview_update_subscription.format(
                subscription_id=subscription_id
            ),
            dict(data),
        )

    def update_subscription(
        self, subscription_id: str, data: SubscriptionRequest
    ) -> SubscriptionResponse:
        """Update a subscription"""
        return self.patch(
            self.endpoints.update_subscription.format(subscription_id=subscription_id),
            dict(data),
        )

    def get_transaction_to_update_payment_method(
        self, subscription_id: str
    ) -> TransactionResponse:
        """Get a transaction to update a payment method"""
        return self.get(
            self.endpoints.get_transaction_to_update_payment_method.format(
                subscription_id=subscription_id
            )
        )

    def preview_one_time_charge(
        self, subscription_id: str, data: SubscriptionRequest
    ) -> SubscriptionResponse:
        """Preview a one-time charge"""
        return self.post(
            self.endpoints.preview_one_time_charge.format(
                subscription_id=subscription_id
            ),
            dict(data),
        )

    def create_one_time_charge(
        self, subscription_id: str, data: SubscriptionRequest
    ) -> SubscriptionResponse:
        """Create a one-time charge"""
        return self.post(
            self.endpoints.create_one_time_charge.format(
                subscription_id=subscription_id
            ),
            dict(data),
        )

    def pause_subscription(
        self, subscription_id: str, data: SubscriptionRequest
    ) -> SubscriptionResponse:
        """Pause a subscription"""
        return self.post(
            self.endpoints.pause_subscription.format(subscription_id=subscription_id),
            dict(data),
        )

    def resume_subscription(
        self, subscription_id: str, data: SubscriptionRequest
    ) -> SubscriptionResponse:
        """Resume a subscription"""
        return self.post(
            self.endpoints.resume_subscription.format(subscription_id=subscription_id),
            dict(data),
        )

    def cancel_subscription(
        self, subscription_id: str, data: SubscriptionRequest
    ) -> SubscriptionResponse:
        """Cancel a subscription"""
        return self.post(
            self.endpoints.cancel_subscription.format(subscription_id=subscription_id),
            dict(data),
        )

    """
    Adjustments
    """

    def create_adjustment(self, data: AdjustmentRequest) -> AdjustmentResponse:
        """Create a customer"""
        return self.post(self.endpoints.create_adjustment, dict(data))

    def list_adjustments(
        self, query_params: AdjustmentQueryParams = None
    ) -> AdjustmentsResponse:
        """List all customers"""
        return self.get(self.endpoints.list_adjustments, params=dict(query_params))

    """
    Events
    """

    def list_event_types(self) -> EventTypesResponse:
        """List all customers"""
        return self.get(self.endpoints.list_event_types)

    def list_events(self) -> EventsResponse:
        """List all customers"""
        return self.get(self.endpoints.list_events)

    """
    Notification settings
    """

    def create_notification_setting(
        self, data: NotificationSettingRequest
    ) -> NotificationSettingResponse:
        """Create notification settings"""
        return self.post(self.endpoints.create_notification_setting, dict(data))

    def get_notification_setting(
        self, notification_setting_id: str
    ) -> NotificationSettingResponse:
        """Get notification settings"""
        return self.get(
            self.endpoints.get_notification_setting.format(
                notification_setting_id=notification_setting_id
            )
        )

    def list_notification_settings(self) -> NotificationSettingsResponse:
        """List notification settings"""
        return self.get(self.endpoints.list_notification_settings)

    def update_notification_setting(
        self, notification_setting_id: str, data: NotificationSettingRequest
    ) -> NotificationSettingResponse:
        """Update notification settings"""
        return self.patch(
            self.endpoints.update_notification_setting.format(
                notification_setting_id=notification_setting_id
            ),
            dict(data),
        )

    def delete_notification_setting(
        self, notification_setting_id: str
    ) -> NotificationSettingResponse:
        """Delete notification settings"""
        return self.delete(
            self.endpoints.delete_notification_setting.format(
                notification_setting_id=notification_setting_id
            )
        )

    """
    Notifications
    """

    def get_notification(self, notification_id: str) -> NotificationResponse:
        """Get a notification"""
        return self.get(
            self.endpoints.get_notification.format(notification_id=notification_id)
        )

    def list_notifications(
        self, query_params: NotificationQueryParams = None
    ) -> NotificationsResponse:
        """List all notifications"""
        return self.get(self.endpoints.list_notifications, params=dict(query_params))

    def replay_notification(self, notification_id: str) -> NotificationReplayResponse:
        """Replay a notification"""
        return self.post(
            self.endpoints.replay_notification.format(notification_id=notification_id),
            dict(),
        )
