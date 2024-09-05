from __future__ import annotations

from typing import Literal

from datetime import datetime

from pydantic import ConfigDict, model_validator

from paddle_billing_client.models import LazyBaseModel as BaseModel
from paddle_billing_client.models import PaddleResponse
from paddle_billing_client.models.address import Address
from paddle_billing_client.models.business import Business
from paddle_billing_client.models.common import BillingDetails, BillingPeriod
from paddle_billing_client.models.customer import Customer
from paddle_billing_client.models.discount import Discount
from paddle_billing_client.models.product import Product


class TaxRatesTotals(BaseModel):
    subtotal: str
    discount: str
    tax: str
    total: str


class TaxRatesUsed(BaseModel):
    tax_rate: str
    totals: TaxRatesTotals


class Totals(BaseModel):
    subtotal: str
    discount: str
    tax: str
    total: str
    credit: str
    balance: str
    grand_total: str
    fee: str | None = None
    earnings: str | None = None
    currency_code: str


class AdjustedTotals(BaseModel):
    subtotal: str
    tax: str
    total: str
    grand_total: str
    fee: str | None = None
    earnings: str | None = None
    currency_code: str


class PayoutTotals(BaseModel):
    subtotal: str
    discount: str
    tax: str
    total: str
    credit: str
    balance: str
    grand_total: str
    fee: str
    earnings: str
    currency_code: str


class ChargebackFeeOriginal(BaseModel):
    amount: str
    currency_code: str


class ChargebackFee(BaseModel):
    amount: str
    original: ChargebackFeeOriginal | None = None


class AdjustedPayoutTotals(BaseModel):
    subtotal: str
    tax: str
    total: str
    fee: str
    chargeback_fee: ChargebackFee | None = None
    earnings: str
    currency_code: str


class LineItemProration(BaseModel):
    rate: str
    billing_period: BillingPeriod


class LineItemUnitTotals(BaseModel):
    subtotal: str
    discount: str
    tax: str
    total: str


class LineItemTotals(BaseModel):
    subtotal: str
    discount: str
    tax: str
    total: str


class LineItem(BaseModel):
    id: str | None = None
    price_id: str | None = None
    quantity: int
    proration: LineItemProration | None = None
    tax_rate: str
    unit_totals: LineItemUnitTotals
    totals: LineItemTotals
    product: Product


class TransactionDetails(BaseModel):
    tax_rates_used: list[TaxRatesUsed] | None = None
    totals: Totals | None = None
    adjusted_totals: AdjustedTotals | None = None
    payout_totals: PayoutTotals | None = None
    adjusted_payout_totals: AdjustedPayoutTotals | None = None
    line_items: list[LineItem] | None = None


class TransactionBase(BaseModel):
    items: list[dict] | None = None
    status: None | (
        Literal["draft", "ready", "billed", "paid", "completed", "canceled", "past_due"]
    ) = None
    customer_id: str | None = None
    address_id: str | None = None
    business_id: str | None = None
    discount_id: str | None = None
    custom_data: dict[str, int | str | None | dict | list] | None = None
    collection_mode: Literal["automatic", "manual"] | None = None
    billing_details: BillingDetails | None = None
    billing_period: BillingPeriod | None = None
    currency_code: str | None = None
    customer_ip_address: str | None = None
    ignore_trials: bool | None = None
    address: Address | None = None


class Transaction(TransactionBase):
    id: str | None = None
    customer: Customer | None = None
    business: Business | None = None
    discount: Discount | None = None
    seller: dict | None = None
    adjustments_totals: dict | None = None
    origin: str | None = None
    subscription_id: str | None = None
    invoice_id: str | None = None
    invoice_number: str | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None
    billed_at: str | None = None
    details: TransactionDetails
    payments: list[dict] | None = None
    checkout: dict | None = None


class TransactionPreview(TransactionBase):
    pass


class TransactionQueryParams(BaseModel):
    # Return entities after the specified cursor. Used for working through paginated results.
    after: str | None = None
    # Return entities billed at a specific time.
    # Pass an RFC 3339 datetime string,
    # or use [LT] (less than), [LTE] (less than or equal to),
    # [GT] (greater than), or [GTE] (greater than or equal to) operators.
    # For example, billed_at=2023-04-18T17:03:26 or billed_at[LT]=2023-04-18T17:03:26.
    billed_at: datetime | str | None = None
    collection_mode: Literal["automatic", "manual"] | None = None
    # Return entities created at a specific time.
    # Pass an RFC 3339 datetime string,
    # or use [LT] (less than), [LTE] (less than or equal to),
    # [GT] (greater than), or [GTE] (greater than or equal to) operators.
    # For example, billed_at=2023-04-18T17:03:26 or billed_at[LT]=2023-04-18T17:03:26.
    created_at: datetime | str | None = None
    # Return entities related to the specified customer. Use a comma separated list to specify multiple customer IDs.
    customer_id: str | None = None
    # Return only the IDs specified. Use a comma separated list to get multiple entities.
    id: str | None = None
    # Include related entities in the response.
    # address|business|customer|discount|seller|adjustment|adjustments_totals
    include: str | None = None
    invoice_number: str | None = None
    # Order returned entities by the specified field and direction ([ASC] or [DESC]).
    order_by: Literal["[ASC]", "[DESC]"] | None = None
    # Set how many entities are returned per page. Default: 50
    per_page: int | None = None
    # Return entities that match the specified status. Use a comma separated list to specify multiple status values.
    status: str | None = None
    # Return entities related to the specified subscription.
    # Use a comma separated list to specify multiple subscription IDs.
    subscription_id: str | None = None
    # Return entities updated at a specific time.
    # Pass an RFC 3339 datetime string,
    # or use [LT] (less than), [LTE] (less than or equal to),
    # [GT] (greater than), or [GTE] (greater than or equal to) operators.
    # For example, billed_at=2023-04-18T17:03:26 or billed_at[LT]=2023-04-18T17:03:26.
    updated_at: datetime | str | None = None

    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="after")
    def check_status(self):
        valid_statuses = [
            "draft",
            "ready",
            "billed",
            "paid",
            "completed",
            "canceled",
            "past_due",
        ]
        if self.status and not all(
            [s in valid_statuses for s in self.status.split(",")]
        ):
            raise ValueError(
                f"Query param invalid status: {self.status}, allowed values: {valid_statuses}"
            )
        return self


class TransactionResponse(PaddleResponse):
    data: Transaction


class TransactionsResponse(PaddleResponse):
    data: list[Transaction]


class TransactionRequest(TransactionBase):
    pass


class TransactionPreviewResponse(PaddleResponse):
    data: TransactionPreview


class TransactionPdf(BaseModel):
    url: str


class TransactionPdfResponse(PaddleResponse):
    data: TransactionPdf
