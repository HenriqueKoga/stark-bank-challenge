from abc import ABC, abstractmethod

from app.domain.client.client import Client


class ClientRepositoryInterface(ABC):

    @abstractmethod
    def get_all(self) -> list[Client]:
        pass

    @abstractmethod
    def get_by_id(self, client_id: int) -> Client:
        pass

    @abstractmethod
    def get_by_cpf(self, cpf: str) -> Client:
        pass
