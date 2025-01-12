from abc import ABC, abstractmethod

from app.application.interfaces.transfer_service import TransferServiceInterface
from app.domain.event.event import Event


class EventHandlerServiceInterface(ABC):

    def __init__(self, transfer_service: TransferServiceInterface):
        self.transfer_service = transfer_service

    @abstractmethod
    def handle(self, event: Event):
        pass
