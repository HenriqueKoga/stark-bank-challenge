from datetime import date
from unittest.mock import MagicMock

import pytest

from app.domain.invoice.invoice import Invoice
from app.infrastructure.starkbank.starkbank_client import StarkbankClient


@pytest.fixture
def starkbank_mock(mocker):
    return mocker.patch("app.infrastructure.starkbank.starkbank_client.starkbank")


@pytest.fixture
def get_file_content_mock(mocker):
    return mocker.patch("app.infrastructure.starkbank.starkbank_client.get_file_content")


def test_issue_invoices(monkeypatch,  starkbank_mock: MagicMock, get_file_content_mock: MagicMock):
    monkeypatch.setenv("STARK_BANK_PRIVATE_KEY", "private_key_mock")

    client_mock = MagicMock(
        cpf="12345678901",
        address=MagicMock(
            full_address="Street, 123",
            complement="Apt 123",
            district="District",
            city="City",
            state="ST",
            zip_code="12345678",
        )
    )
    client_mock.name = "Client Name"

    invoice_mock = MagicMock(
        spec=Invoice,
        amount=1000,
        due_date=date(2025, 10, 10),
        client=client_mock
    )

    starkbank_client = StarkbankClient()
    starkbank_client.issue_invoices([invoice_mock])

    starkbank_mock.Boleto.assert_called_once_with(
        amount=1000,
        due="2025-10-10",
        name="Client Name",
        tax_id="12345678901",
        street_line_1="Street, 123",
        street_line_2="Apt 123",
        district="District",
        city="City",
        state_code="ST",
        zip_code="12345678"
    )
    starkbank_mock.boleto.create.assert_called_once_with([starkbank_mock.Boleto.return_value])
    get_file_content_mock.assert_called_once_with("private_key_mock")


def test_transfer(monkeypatch, starkbank_mock: MagicMock, get_file_content_mock: MagicMock):
    monkeypatch.setenv("STARK_BANK_PRIVATE_KEY", "private_key_mock")

    account_mock = MagicMock(
        cnpj="12345678901234",
        bank_code="123",
        branch="1234",
        number="12345",
        account_type="checking"
    )
    account_mock.name = "Account Name"

    starkbank_client = StarkbankClient()
    starkbank_client.transfer(account_mock, 1000)

    starkbank_mock.Transfer.assert_called_once_with(
        amount=1000,
        tax_id="12345678901234",
        name="Account Name",
        bank_code="123",
        branch_code="1234",
        account_number="12345",
        account_type="checking"
    )
    starkbank_mock.transfer.create.assert_called_once_with([starkbank_mock.Transfer.return_value])
    get_file_content_mock.assert_called_once_with("private_key_mock")
