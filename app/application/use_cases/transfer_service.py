from app.application.interfaces.transfer_service import TransferServiceInterface
from app.infrastructure.starkbank.starkbank_client import StarkbankClient


class TransferService(TransferServiceInterface):

    def transfer(self, receiver_cnpj: str, amount: float, fee: float):
        account = self.account_repository.get_by_cnpj(receiver_cnpj)
        StarkbankClient().transfer(account, amount - fee)
