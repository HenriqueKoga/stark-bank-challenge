from app.application.interfaces.event_handler_service import EventHandlerServiceInterface
from app.domain.event.event import Event, InvalidEvent, InvoiceEvent


class EventHandlerService(EventHandlerServiceInterface):

    def handle(self, event: Event):
        if isinstance(event, InvoiceEvent) and event.type == "paid":
            cnpj = event.data['receiverTaxId']
            amount = event.data['amount']
            fee = event.data['fee']

            self.transfer_service.transfer(cnpj, amount, fee)
            return

        raise InvalidEvent(f'Invalid event: {event.raw}')
