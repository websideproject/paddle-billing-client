from __future__ import annotations

from apiclient import APIClient, JsonResponseHandler
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
from paddle_billing_client.models.common import Paginate
from paddle_billing_client.models.customer import (
    CustomerBalancesQueryParams,
    CustomerBalancesResponse,
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
        return self.post(
            self.endpoints.create_product, data.model_dump(exclude_none=True)
        )

    def get_product(self, product_id: str) -> ProductResponse:
        """Get a product"""
        return self.get(self.endpoints.get_product.format(product_id=product_id))

    def list_products(
        self,
        query_params: ProductQueryParams = ProductQueryParams(),
        paginate: Paginate = None,
    ) -> ProductsResponse:
        """List all products"""
        return self.get(
            dict(paginate)["next"] if paginate else self.endpoints.list_products,
            params=query_params.model_dump(exclude_none=True),
        )

    def update_product(self, product_id: str, data: ProductRequest) -> ProductResponse:
        """Update a product"""
        return self.patch(
            self.endpoints.update_product.format(product_id=product_id),
            data.model_dump(exclude_none=True),
        )

    """
    Prices
    """

    def create_price(self, data: PriceRequest) -> PriceResponse:
        """Create a price"""
        return self.post(
            self.endpoints.create_price,
            data.model_dump(exclude_none=True),
        )

    def get_price(self, price_id: str) -> PriceResponse:
        """Get a price"""
        return self.get(self.endpoints.get_price.format(price_id=price_id))

    def list_prices(
        self,
        query_params: PriceQueryParams = PriceQueryParams(),
        paginate: Paginate = None,
    ) -> PricesResponse:
        """List all prices"""
        return self.get(
            dict(paginate)["next"] if paginate else self.endpoints.list_prices,
            params=query_params.model_dump(exclude_none=True),
        )

    def update_price(self, price_id: str, data: PriceRequest) -> PriceResponse:
        """Update a price"""
        return self.patch(
            self.endpoints.update_price.format(price_id=price_id),
            data.model_dump(exclude_none=True),
        )

    """
    Discounts
    """

    def create_discount(self, data: DiscountRequest) -> DiscountResponse:
        """Create a discount"""
        return self.post(
            self.endpoints.create_discount,
            data.model_dump(exclude_none=True),
        )

    def get_discount(self, discount_id: str) -> DiscountResponse:
        """Get a discount"""
        return self.get(self.endpoints.get_discount.format(discount_id=discount_id))

    def list_discounts(
        self,
        query_params: DiscountQueryParams = DiscountQueryParams(),
        paginate: Paginate = None,
    ) -> DiscountsResponse:
        """List all discounts"""
        return self.get(
            dict(paginate)["next"] if paginate else self.endpoints.list_discounts,
            params=query_params.model_dump(exclude_none=True),
        )

    def update_discount(
        self, discount_id: str, data: DiscountRequest
    ) -> DiscountResponse:
        """Update a discount"""
        return self.patch(
            self.endpoints.update_discount.format(discount_id=discount_id),
            data.model_dump(exclude_none=True),
        )

    """
    Customers
    """

    def create_customer(self, data: CustomerRequest) -> CustomerResponse:
        """Create a customer"""
        return self.post(
            self.endpoints.create_customer,
            data.model_dump(exclude_none=True),
        )

    def get_customer(self, customer_id: str) -> CustomerResponse:
        """Get a customer"""
        return self.get(self.endpoints.get_customer.format(customer_id=customer_id))

    def list_customers(
        self,
        query_params: CustomerQueryParams = CustomerQueryParams(),
        paginate: Paginate = None,
    ) -> CustomersResponse:
        """List all customers"""
        return self.get(
            dict(paginate)["next"] if paginate else self.endpoints.list_customers,
            params=query_params.model_dump(exclude_none=True),
        )

    def update_customer(
        self, customer_id: str, data: CustomerRequest
    ) -> CustomerResponse:
        """Update a customer"""
        return self.patch(
            self.endpoints.update_customer.format(customer_id=customer_id),
            data.model_dump(exclude_none=True),
        )

    def list_customer_credit_balances(
        self,
        customer_id: str,
        query_params: CustomerBalancesQueryParams = CustomerBalancesQueryParams(),
    ) -> CustomerBalancesResponse:
        """List credit balances for a customer"""
        return self.get(
            self.endpoints.list_customer_credit_balances.format(
                customer_id=customer_id
            ),
            params=query_params.model_dump(exclude_none=True),
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
            data.model_dump(exclude_none=True),
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
        self,
        customer_id: str,
        query_params: AddressQueryParams = AddressQueryParams(),
        paginate: Paginate = None,
    ) -> AddressesResponse:
        """List all addresses for a customer"""
        return self.get(
            (
                dict(paginate)["next"]
                if paginate
                else self.endpoints.list_addresses_for_customer.format(
                    customer_id=customer_id
                )
            ),
            params=query_params.model_dump(exclude_none=True),
        )

    def update_address_for_customer(
        self, customer_id: str, address_id: str, data: AddressRequest
    ) -> AddressResponse:
        """Update an address for a customer"""
        return self.patch(
            self.endpoints.update_address_for_customer.format(
                customer_id=customer_id, address_id=address_id
            ),
            data.model_dump(exclude_none=True),
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
            data.model_dump(exclude_none=True),
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
        self,
        customer_id: str,
        query_params: BusinessQueryParams = BusinessQueryParams(),
        paginate: Paginate = None,
    ) -> BusinessesResponse:
        """List all businesses for a customer"""
        return self.get(
            (
                dict(paginate)["next"]
                if paginate
                else self.endpoints.list_businesses_for_customer.format(
                    customer_id=customer_id
                )
            ),
            params=query_params.model_dump(exclude_none=True),
        )

    def update_business_for_customer(
        self, customer_id: str, business_id: str, data: BusinessRequest
    ) -> BusinessResponse:
        """Update a business for a customer"""
        return self.patch(
            self.endpoints.update_business_for_customer.format(
                customer_id=customer_id, business_id=business_id
            ),
            data.model_dump(exclude_none=True),
        )

    """
    Transactions
    """

    def create_transaction(
        self,
        data: TransactionRequest,
        query_params: TransactionQueryParams = TransactionQueryParams(),
    ) -> TransactionResponse:
        """Create a transaction"""
        return self.post(
            self.endpoints.create_transaction,
            data.model_dump(exclude_none=True),
            params=query_params.model_dump(exclude_none=True),
        )

    def get_transaction(
        self,
        transaction_id: str,
        query_params: TransactionQueryParams = TransactionQueryParams(),
    ) -> TransactionResponse:
        """Get a transaction"""
        return self.get(
            self.endpoints.get_transaction.format(transaction_id=transaction_id),
            params=query_params.model_dump(exclude_none=True),
        )

    def list_transactions(
        self,
        query_params: TransactionQueryParams = TransactionQueryParams(),
        paginate: Paginate = None,
    ) -> TransactionsResponse:
        """List all transactions"""
        return self.get(
            dict(paginate)["next"] if paginate else self.endpoints.list_transactions,
            params=query_params.model_dump(exclude_none=True),
        )

    def update_transaction(
        self,
        transaction_id: str,
        data: TransactionRequest,
        query_params: TransactionQueryParams = TransactionQueryParams(),
    ) -> TransactionResponse:
        """Update a transaction"""
        return self.patch(
            self.endpoints.update_transaction.format(transaction_id=transaction_id),
            data.model_dump(exclude_none=True),
            params=query_params.model_dump(exclude_none=True),
        )

    def preview_transaction(
        self,
        data: TransactionRequest,
        query_params: TransactionQueryParams = TransactionQueryParams(),
    ) -> TransactionPreviewResponse:
        """Preview a transaction"""
        return self.post(
            self.endpoints.preview_transaction,
            data.model_dump(exclude_none=True),
            params=query_params.model_dump(exclude_none=True),
        )

    def preview_prices(self, data: TransactionRequest) -> TransactionResponse:
        """Preview prices"""
        return self.post(
            self.endpoints.preview_prices,
            data.model_dump(exclude_none=True),
        )

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
        self,
        query_params: SubscriptionQueryParams = SubscriptionQueryParams(),
        paginate: Paginate = None,
    ) -> SubscriptionsResponse:
        """List all subscriptions"""
        return self.get(
            dict(paginate)["next"] if paginate else self.endpoints.list_subscriptions,
            params=query_params.model_dump(exclude_none=True),
        )

    def preview_update_subscription(
        self, subscription_id: str, data: SubscriptionRequest
    ) -> SubscriptionResponse:
        """Preview an update to a subscription"""
        return self.patch(
            self.endpoints.preview_update_subscription.format(
                subscription_id=subscription_id
            ),
            data.model_dump(exclude_none=True),
        )

    def update_subscription(
        self, subscription_id: str, data: SubscriptionRequest
    ) -> SubscriptionResponse:
        """Update a subscription"""
        return self.patch(
            self.endpoints.update_subscription.format(subscription_id=subscription_id),
            data.model_dump(exclude_none=True),
        )

    def unschedule_scheduled_action_from_subscription(
        self, subscription_id: str
    ) -> SubscriptionResponse:
        """Remove a scheduled action from a subscription"""
        return self.patch(
            self.endpoints.update_subscription.format(subscription_id=subscription_id),
            {"scheduled_change": None},
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
            data.model_dump(exclude_none=True),
        )

    def create_one_time_charge(
        self, subscription_id: str, data: SubscriptionRequest
    ) -> SubscriptionResponse:
        """Create a one-time charge"""
        return self.post(
            self.endpoints.create_one_time_charge.format(
                subscription_id=subscription_id
            ),
            data.model_dump(exclude_none=True),
        )

    def activate_trialing_subscription(
        self, subscription_id: str, data: SubscriptionRequest
    ) -> SubscriptionResponse:
        """Activate a trialing subscription"""
        return self.post(
            self.endpoints.activate_trialing_subscription.format(
                subscription_id=subscription_id
            ),
            data.model_dump(exclude_none=True),
        )

    def pause_subscription(
        self, subscription_id: str, data: SubscriptionRequest
    ) -> SubscriptionResponse:
        """Pause a subscription"""
        return self.post(
            self.endpoints.pause_subscription.format(subscription_id=subscription_id),
            data.model_dump(),
        )

    def resume_subscription(
        self, subscription_id: str, data: SubscriptionRequest
    ) -> SubscriptionResponse:
        """Resume a subscription"""
        return self.post(
            self.endpoints.resume_subscription.format(subscription_id=subscription_id),
            data.model_dump(exclude_none=True),
        )

    def cancel_subscription(
        self, subscription_id: str, data: SubscriptionRequest
    ) -> SubscriptionResponse:
        """Cancel a subscription"""
        return self.post(
            self.endpoints.cancel_subscription.format(subscription_id=subscription_id),
            data.model_dump(exclude_none=True),
        )

    """
    Adjustments
    """

    def create_adjustment(self, data: AdjustmentRequest) -> AdjustmentResponse:
        """Create a customer"""
        return self.post(
            self.endpoints.create_adjustment, data.model_dump(exclude_none=True)
        )

    def list_adjustments(
        self,
        query_params: AdjustmentQueryParams = AdjustmentQueryParams(),
        paginate: Paginate = None,
    ) -> AdjustmentsResponse:
        """List all customers"""
        return self.get(
            dict(paginate)["next"] if paginate else self.endpoints.list_adjustments,
            params=query_params.model_dump(exclude_none=True),
        )

    """
    Events
    """

    def list_event_types(self) -> EventTypesResponse:
        """List all customers"""
        return self.get(self.endpoints.list_event_types)

    def list_events(self, paginate: Paginate = None) -> EventsResponse:
        """List all customers"""
        return self.get(
            dict(paginate)["next"] if paginate else self.endpoints.list_events,
        )

    """
    Notification settings
    """

    def create_notification_setting(
        self, data: NotificationSettingRequest
    ) -> NotificationSettingResponse:
        """Create notification settings"""
        return self.post(
            self.endpoints.create_notification_setting,
            data.model_dump(exclude_none=True),
        )

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
            data.model_dump(exclude_none=True),
        )

    def delete_notification_setting(
        self, notification_setting_id: str
    ) -> NotificationSettingResponse | None:
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
        self,
        query_params: NotificationQueryParams = NotificationQueryParams(),
        paginate: Paginate = None,
    ) -> NotificationsResponse:
        """List all notifications"""
        return self.get(
            dict(paginate)["next"] if paginate else self.endpoints.list_notifications,
            params=query_params.model_dump(exclude_none=True),
        )

    def replay_notification(self, notification_id: str) -> NotificationReplayResponse:
        """Replay a notification"""
        return self.post(
            self.endpoints.replay_notification.format(notification_id=notification_id),
            dict(),
        )
