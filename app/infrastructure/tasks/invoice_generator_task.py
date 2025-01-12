import random

from app.application.use_cases.invoice_generator import InvoiceGeneratorService
from app.infrastructure.celery.celery_app import celery_app
from app.infrastructure.repositories.client_local_repository import ClientLocalRepository


@celery_app.task(name="tasks.generate_invoice")
def generate_invoice(client_id: int):
    client_repository = ClientLocalRepository()
    invoice_generator = InvoiceGeneratorService()

    client = client_repository.get_by_id(client_id)
    invoice_generator.generate(client)
