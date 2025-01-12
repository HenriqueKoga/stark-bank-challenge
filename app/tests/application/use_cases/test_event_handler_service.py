from unittest.mock import MagicMock

import pytest

from app.application.interfaces.transfer_service import TransferServiceInterface
from app.application.use_cases.event_handler_service import EventHandlerService
from app.domain.event.event import Event, InvalidEvent, InvoiceEvent


def test_handle_invoice_event_paid():
    event = MagicMock(spec=InvoiceEvent, type="paid", data={
        'receiverTaxId': '12345678901234',
        'amount': 1000,
        'fee': 50
    })

    transfer_service = MagicMock(spec=TransferServiceInterface)

    service = EventHandlerService(transfer_service)
    service.handle(event)

    transfer_service.transfer.assert_called_once_with('12345678901234', 1000, 50)


def test_handle_invalid_event():
    event = MagicMock(spec=Event, type="invalid", raw="raw")

    transfer_service = MagicMock(spec=TransferServiceInterface)

    service = EventHandlerService(transfer_service)
    with pytest.raises(InvalidEvent) as excinfo:
        service.handle(event)

    assert str(excinfo.value) == "Invalid event: raw"
