from abc import ABC, abstractmethod

from app.domain.client.client import Client


class InvoiceGeneratorServiceInterface(ABC):

    @abstractmethod
    def generate(self, client: Client, data: dict):
        pass
