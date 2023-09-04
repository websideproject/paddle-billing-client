from pydantic import BaseModel


class BillingPeriod(BaseModel):
    ends_at: str
    starts_at: str
