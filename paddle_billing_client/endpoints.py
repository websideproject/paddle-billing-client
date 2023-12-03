class Endpoints:
    def __init__(self, base_url="https://sandbox-api.paddle.com"):
        self._base_url = base_url

    def __getattribute__(self, name):
        value = super().__getattribute__(name)
        if name.startswith("_"):
            return value
        return f"{self._base_url}/{value.lstrip('/')}"

    # Products
    create_product: str = "products"
    get_product: str = "products/{product_id}"
    list_products: str = "products"
    update_product: str = "products/{product_id}"

    # Prices
    create_price: str = "prices"
    get_price: str = "prices/{price_id}"
    list_prices: str = "prices"
    update_price: str = "prices/{price_id}"

    # Discounts
    create_discount: str = "discounts"
    get_discount: str = "discounts/{discount_id}"
    list_discounts: str = "discounts"
    update_discount: str = "discounts/{discount_id}"

    # Customers
    create_customer: str = "customers"
    get_customer: str = "customers/{customer_id}"
    list_customers: str = "customers"
    update_customer: str = "customers/{customer_id}"
    list_customer_credit_balances: str = "customers/{customer_id}/credit-balances"

    # Addresses
    create_address_for_customer: str = "customers/{customer_id}/addresses"
    get_address_for_customer: str = "customers/{customer_id}/addresses/{address_id}"
    list_addresses_for_customer: str = "customers/{customer_id}/addresses"
    update_address_for_customer: str = "customers/{customer_id}/addresses/{address_id}"

    # Businesses
    create_business_for_customer: str = "customers/{customer_id}/businesses"
    get_business_for_customer: str = "customers/{customer_id}/businesses/{business_id}"
    list_businesses_for_customer: str = "customers/{customer_id}/businesses"
    update_business_for_customer: str = (
        "customers/{customer_id}/businesses/{business_id}"
    )

    # Transactions
    create_transaction: str = "transactions"
    get_transaction: str = "transactions/{transaction_id}"
    list_transactions: str = "transactions"
    update_transaction: str = "transactions/{transaction_id}"
    preview_transaction: str = "transactions/preview"
    get_pdf_for_transaction: str = "transactions/{transaction_id}/invoice"

    # Subscriptions
    get_subscription: str = "subscriptions/{subscription_id}"
    list_subscriptions: str = "subscriptions"
    preview_update_subscription: str = "subscriptions/{subscription_id}/preview"
    update_subscription: str = "subscriptions/{subscription_id}"
    get_transaction_to_update_payment_method: str = (
        "subscriptions/{subscription_id}/update-payment-method-transaction"
    )
    preview_one_time_charge: str = "subscriptions/{subscription_id}/charge/preview"
    create_one_time_charge: str = "subscriptions/{subscription_id}/charge"
    activate_trialing_subscription: str = "subscriptions/{subscription_id}/activate"
    pause_subscription: str = "subscriptions/{subscription_id}/pause"
    resume_subscription: str = "subscriptions/{subscription_id}/resume"
    cancel_subscription: str = "subscriptions/{subscription_id}/cancel"

    # Adjustments
    create_adjustment: str = "adjustments"
    list_adjustments: str = "adjustments"

    # Pricing Preview
    preview_prices: str = "pricing-preview"

    # Events
    list_event_types: str = "event-types"
    list_events: str = "events"

    # Notification settings
    create_notification_setting: str = "notification-settings"
    get_notification_setting: str = "notification-settings/{notification_setting_id}"
    list_notification_settings: str = "notification-settings"
    update_notification_setting: str = "notification-settings/{notification_setting_id}"
    delete_notification_setting: str = "notification-settings/{notification_setting_id}"

    # Notifications
    get_notification: str = "notifications/{notification_id}"
    list_notifications: str = "notifications"
    replay_notification: str = "notifications/{notification_id}/replay"
