from app.domain.account.account import Account, AccountNotFound
from app.infrastructure.repositories.interfaces.account_repositoy import AccountRepositoryInterface


class AccountLocalRepository(AccountRepositoryInterface):
    accounts = [
        Account(
            id=1,
            bank_code='20018183',
            branch='0001',
            number='6341320293482496',
            name='Stark Bank S.A.',
            cnpj='20.018.183/0001-80',
            account_type='payment',
        )
    ]

    def get_all(self) -> list[Account]:
        return self.accounts

    def get_by_id(self, account_id: int) -> Account:
        account = next((account for account in self.accounts if account.id == account_id), None)
        if account is None:
            raise AccountNotFound('Account not found')

        return account

    def get_by_cnpj(self, cnpj) -> Account:
        account = next((account for account in self.accounts if account.cnpj == cnpj), None)
        if account is None:
            raise AccountNotFound('Account not found')

        return account
