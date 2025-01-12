from datetime import date
from unittest.mock import MagicMock

import pytest

from app.application.use_cases.invoice_generator import InvoiceGeneratorService
from app.domain.client.client import Client


@pytest.fixture
def randint_mock(mocker):
    return mocker.patch("app.application.use_cases.invoice_generator.random.randint")


@pytest.fixture
def get_today_mock(mocker):
    return mocker.patch("app.application.use_cases.invoice_generator.get_today")


@pytest.fixture
def starkbank_client_mock(mocker):
    return mocker.patch("app.application.use_cases.invoice_generator.StarkbankClient")


@pytest.fixture
def invoice_mock(mocker):
    return mocker.patch("app.application.use_cases.invoice_generator.Invoice")


def test_generate(
    randint_mock: MagicMock,
    get_today_mock: MagicMock,
    starkbank_client_mock: MagicMock,
    invoice_mock: MagicMock,
):
    randint_mock.side_effect = [500, 10]
    get_today_mock.return_value = date(2025, 1, 1)

    client = MagicMock(spec=Client)

    service = InvoiceGeneratorService()
    service.generate(client)

    invoice_mock.assert_called_once_with(client=client, amount=500, due_date=date(2025, 1, 11))
    starkbank_client_mock.return_value.issue_invoices.assert_called_once_with([invoice_mock.return_value])
