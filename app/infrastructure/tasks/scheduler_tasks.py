import random

from app.infrastructure.celery.celery_app import celery_app
from app.infrastructure.tasks.invoice_generator_task import generate_invoice


@celery_app.task(name="tasks.schedule_invoices")
def schedule_invoices():
    random_int = random.randint(8, 12)
    for _ in range(1, random_int):
        clint_id = random.randint(1, 13)
        generate_invoice.delay(clint_id)


@celery_app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(
        3 * 60 * 60,
        schedule_invoices.s(),
        name="Schedule invoices every 3 hours",
    )
