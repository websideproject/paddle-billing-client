import os
from datetime import datetime

import deepdiff
import pytest
from apiclient import HeaderAuthentication

from paddle_billing_client.models.adjustment import (
    Adjustment,
    AdjustmentQueryParams,
    AdjustmentRequest,
    AdjustmentResponse,
    AdjustmentsResponse,
)


class TestAdjustment:
    def setup_class(self):
        from paddle_billing_client.client import PaddleApiClient  # pragma: no cover

        self.client = PaddleApiClient(
            authentication_method=HeaderAuthentication(
                token=os.getenv("PADDLE_SANDBOX_AUTH_TOKEN")
            ),
        )

    @pytest.mark.vcr
    def test_create_adjustment(self):
        adjustment = self.client.create_adjustment(
            data=AdjustmentRequest(
                transaction_id="txn_01h7n3a7g7h0qr49zt9ckgketd",
                reason="Test Adjustment Reason",
                action="refund",
                items=[
                    dict(
                        item_id="txnitm_01h7n3a7jefxzqhpaw6hdc523q",
                        type="partial",
                        amount=100,
                    ),
                ],
            )
        )
        expected_adjustment = AdjustmentResponse(
            data=Adjustment(
                id="adj_01h9fk7y5yj1m9bcn270a6rs81",
                status="pending_approval",
                transaction_id="txn_01h7n3a7g7h0qr49zt9ckgketd",
                subscription_id="sub_01h7n3a88jwktex2tfjzahmn57",
                customer_id="ctm_01h7mrr5j8rnawwzh9nschgp1v",
                reason="Test Adjustment Reason",
                action="refund",
                currency_code="USD",
                items=[
                    {
                        "id": "adjitm_01h9fk7y5yj1m9bcn2726rdepp",
                        "item_id": "txnitm_01h7n3a7jefxzqhpaw6hdc523q",
                        "type": "partial",
                        "amount": "100",
                        "proration": None,
                        "totals": {"subtotal": "79", "tax": "21", "total": "100"},
                    },
                ],
                totals={
                    "subtotal": "79",
                    "tax": "21",
                    "total": "100",
                    "fee": "3",
                    "earnings": "76",
                    "currency_code": "USD",
                },
                payout_totals={
                    "subtotal": "79",
                    "tax": "21",
                    "total": "100",
                    "fee": "3",
                    "earnings": "76",
                    "currency_code": "USD",
                },
                created_at="2023-09-04T07:59:16.172081Z",
                updated_at="0001-01-01T00:00:00Z",
            ),
            meta=dict(request_id="d0e5be7c-46d9-4ffd-838e-bd4b6098ad99"),
        )

        assert (
            deepdiff.DeepDiff(adjustment, expected_adjustment, ignore_order=True) == {}
        )

        assert isinstance(adjustment, AdjustmentResponse)
        assert isinstance(adjustment.data, Adjustment)
        assert str.startswith(adjustment.data.id, "adj_")

    @pytest.mark.vcr
    def test_list_adjustments_pending(self):
        adjustments = self.client.list_adjustments(
            query_params=AdjustmentQueryParams(
                status="pending_approval",
            )
        )
        expected_adjustments = AdjustmentsResponse(
            data=[
                Adjustment(
                    id="adj_01h9fk7y5yj1m9bcn270a6rs81",
                    status="pending_approval",
                    transaction_id="txn_01h7n3a7g7h0qr49zt9ckgketd",
                    subscription_id="sub_01h7n3a88jwktex2tfjzahmn57",
                    customer_id="ctm_01h7mrr5j8rnawwzh9nschgp1v",
                    reason="Test Adjustment Reason",
                    action="refund",
                    currency_code="USD",
                    items=[
                        {
                            "id": "adjitm_01h9fk7y5yj1m9bcn2726rdepp",
                            "item_id": "txnitm_01h7n3a7jefxzqhpaw6hdc523q",
                            "type": "partial",
                            "amount": "100",
                            "proration": None,
                            "totals": {"subtotal": "79", "tax": "21", "total": "100"},
                        },
                    ],
                    totals={
                        "subtotal": "79",
                        "tax": "21",
                        "total": "100",
                        "fee": "3",
                        "earnings": "76",
                        "currency_code": "USD",
                    },
                    payout_totals={
                        "subtotal": "79",
                        "tax": "21",
                        "total": "100",
                        "fee": "3",
                        "earnings": "76",
                        "currency_code": "USD",
                    },
                    created_at="2023-09-04T07:59:16.172081Z",
                    updated_at="2023-09-04T07:59:16.172081Z",
                )
            ],
            meta=dict(
                request_id="3e3cc0b8-ac0a-49a2-bec4-a2a322e5147c",
                pagination=dict(
                    per_page=10,
                    next="https://sandbox-api.paddle.com/adjustments?after=adj_01h9fk7y5yj1m9bcn270a6rs81&status=pending_approval",
                    has_more=False,
                    estimated_total=1,
                ),
            ),
        )

        assert (
            deepdiff.DeepDiff(adjustments, expected_adjustments, ignore_order=True)
            == {}
        )

    @pytest.mark.vcr
    def test_list_adjustments_approved(self):
        adjustments = self.client.list_adjustments(
            query_params=AdjustmentQueryParams(
                status="approved",
            )
        )
        expected_adjustments = AdjustmentsResponse(
            data=[
                # Adjustment()
            ],
            meta=dict(
                request_id="7ef9a244-24e8-42b2-9428-6c2c54e4bbfa",
                pagination=dict(
                    per_page=10,
                    next="https://sandbox-api.paddle.com/adjustments?status=approved",
                    has_more=False,
                    estimated_total=3,
                ),
            ),
        )

        assert (
            deepdiff.DeepDiff(adjustments, expected_adjustments, ignore_order=True)
            == {}
        )
