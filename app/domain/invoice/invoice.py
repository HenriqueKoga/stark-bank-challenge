from pydantic import BaseModel, FutureDate, PositiveInt

from app.domain.client.client import Client


class Invoice(BaseModel):
    client: Client
    amount: PositiveInt
    due_date: FutureDate
