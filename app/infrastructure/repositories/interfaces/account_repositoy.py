from abc import ABC, abstractmethod

from app.domain.account.account import Account


class AccountRepositoryInterface(ABC):

    @abstractmethod
    def get_all(self) -> list[Account]:
        pass

    @abstractmethod
    def get_by_id(self, account_id: int) -> Account:
        pass

    @abstractmethod
    def get_by_cnpj(self, cnpj: str) -> Account:
        pass
