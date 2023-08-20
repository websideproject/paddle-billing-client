from typing import Dict, List, Literal, Optional

from datetime import datetime

from pydantic import validator

from paddle_billing_client.models import LazyBaseModel as BaseModel
from paddle_billing_client.models import PaddleResponse
from paddle_billing_client.models.address import Address
from paddle_billing_client.models.business import Business
from paddle_billing_client.models.customer import Customer
from paddle_billing_client.models.discount import Discount
from paddle_billing_client.models.product import Product
from paddle_billing_client.models.subscription import BillingPeriod


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
    fee: Optional[str]
    earnings: Optional[str]
    currency_code: str


class AdjustedTotals(BaseModel):
    subtotal: str
    tax: str
    total: str
    grand_total: str
    fee: Optional[str]
    earnings: Optional[str]
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
    original: Optional[ChargebackFeeOriginal]


class AdjustedPayoutTotals(BaseModel):
    subtotal: str
    tax: str
    total: str
    fee: str
    chargeback_fee: Optional[ChargebackFee]
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
    id: str
    price_id: str
    quantity: int
    proration: Optional[LineItemProration]
    tax_rate: str
    unit_totals: LineItemUnitTotals
    totals: LineItemTotals
    product: Product


class TransactionDetails(BaseModel):
    tax_rates_used: List[TaxRatesUsed]
    totals: Totals
    adjusted_totals: Optional[AdjustedTotals]
    payout_totals: Optional[PayoutTotals]
    adjusted_payout_totals: Optional[AdjustedPayoutTotals]
    line_items: List[LineItem]


class BillingDetails(BaseModel):
    enable_checkout: Optional[bool]
    payment_terms: Optional[dict]
    purchase_order_number: Optional[str]
    additional_information: Optional[str]


class TransactionBase(BaseModel):
    items: List[dict]
    status: Optional[
        Literal["draft", "ready", "billed", "paid", "completed", "canceled", "past_due"]
    ]
    customer_id: Optional[str]
    address_id: Optional[str]
    business_id: Optional[str]
    discount_id: Optional[str]
    custom_data: Optional[dict]
    collection_mode: Literal["automatic", "manual"]
    billing_details: Optional[BillingDetails]
    billing_period: Optional[BillingPeriod]
    currency_code: str


class Transaction(TransactionBase):
    id: str
    customer: Optional[Customer]
    address: Optional[Address]
    business: Optional[Business]
    discount: Optional[Discount]
    adjustments_totals: Optional[dict]
    origin: str
    subscription_id: Optional[str]
    invoice_id: Optional[str]
    invoice_number: Optional[str]
    created_at: datetime
    updated_at: datetime
    billed_at: Optional[str]
    details: TransactionDetails
    payments: List[dict]
    checkout: Optional[dict]


class TransactionQueryParams(BaseModel):
    # Return entities after the specified cursor. Used for working through paginated results.
    after: Optional[str] = None
    # Return entities billed at a specific time.
    # Pass an RFC 3339 datetime string,
    # or use [LT] (less than), [LTE] (less than or equal to),
    # [GT] (greater than), or [GTE] (greater than or equal to) operators.
    # For example, billed_at=2023-04-18T17:03:26 or billed_at[LT]=2023-04-18T17:03:26.
    billed_at: Optional[datetime | str] = None
    collection_mode: Optional[Literal["automatic", "manual"]] = None
    # Return entities created at a specific time.
    # Pass an RFC 3339 datetime string,
    # or use [LT] (less than), [LTE] (less than or equal to),
    # [GT] (greater than), or [GTE] (greater than or equal to) operators.
    # For example, billed_at=2023-04-18T17:03:26 or billed_at[LT]=2023-04-18T17:03:26.
    created_at: Optional[datetime | str] = None
    # Return entities related to the specified customer. Use a comma separated list to specify multiple customer IDs.
    customer_id: Optional[str]
    # Return only the IDs specified. Use a comma separated list to get multiple entities.
    id: Optional[str] = None
    # Include related entities in the response.
    # 'address', 'adjustment', 'adjustment_totals', 'business', 'customer', 'discount'
    include: Optional[str] = None
    invoice_number: Optional[str] = None
    # Order returned entities by the specified field and direction ([ASC] or [DESC]).
    order_by: Optional[Literal["[ASC]", "[DESC]"]] = None
    # Set how many entities are returned per page. Default: 50
    per_page: Optional[int] = None
    # Return entities that match the specified status. Use a comma separated list to specify multiple status values.
    status: Optional[str] = None
    # Return entities related to the specified subscription.
    # Use a comma separated list to specify multiple subscription IDs.
    subscription_id: Optional[str]
    # Return entities updated at a specific time.
    # Pass an RFC 3339 datetime string,
    # or use [LT] (less than), [LTE] (less than or equal to),
    # [GT] (greater than), or [GTE] (greater than or equal to) operators.
    # For example, billed_at=2023-04-18T17:03:26 or billed_at[LT]=2023-04-18T17:03:26.
    updated_at: Optional[datetime | str] = None

    @validator("status", allow_reuse=True)
    def check_status(cls, v: str) -> str:  # pragma: no cover
        valid_statuses = [
            "draft",
            "ready",
            "billed",
            "paid",
            "completed",
            "canceled",
            "past_due",
        ]
        if not all([s in valid_statuses for s in v.split(",")]):
            raise ValueError(
                f"Query param invalid status: {v}, allowed values: {valid_statuses}"
            )
        return v


class TransactionResponse(PaddleResponse):
    data: Transaction


class TransactionsResponse(PaddleResponse):
    data: List[Transaction]


class TransactionRequest(TransactionBase):
    pass


class TransactionPdf(BaseModel):
    url: str


class TransactionPdfResponse(PaddleResponse):
    data: TransactionPdf
