from abc import ABC, abstractmethod

from app.infrastructure.repositories.interfaces.account_repositoy import AccountRepositoryInterface


class TransferServiceInterface(ABC):

    def __init__(self, account_repository: AccountRepositoryInterface):
        self.account_repository = account_repository

    @abstractmethod
    def transfer(self, receiver_cnpj: str, amount: float, fee: float):
        pass
