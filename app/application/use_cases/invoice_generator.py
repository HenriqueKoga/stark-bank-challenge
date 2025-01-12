import random
from datetime import date, timedelta

from app.application.interfaces.invoice_generator_service import InvoiceGeneratorServiceInterface
from app.domain.client.client import Client
from app.domain.invoice.invoice import Invoice
from app.infrastructure.starkbank.starkbank_client import StarkbankClient
from app.utils.date_utils import get_today


class InvoiceGeneratorService(InvoiceGeneratorServiceInterface):

    def generate(self, client: Client):
        data = {
            "amount": random.randint(200, 1000),
            "due_date": get_today() + timedelta(days=random.randint(1, 30)),
        }
        invoice = Invoice(client=client, amount=data["amount"], due_date=data["due_date"])
        starkbank_client = StarkbankClient()
        starkbank_client.issue_invoices([invoice])
