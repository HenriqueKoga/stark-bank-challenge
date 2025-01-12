from app.domain.account.account import Account
from app.infrastructure.repositories.account_local_repository import AccountLocalRepository


def test_get_all():
    repository = AccountLocalRepository()
    accounts = repository.get_all()

    assert all(isinstance(account, Account) for account in accounts)


def test_get_by_id():
    repository = AccountLocalRepository()
    account = repository.get_by_id(1)

    assert isinstance(account, Account)
    assert account.id == 1


def test_get_by_cnpj():
    repository = AccountLocalRepository()
    account = repository.get_by_cnpj('20.018.183/0001-80')

    assert isinstance(account, Account)
    assert account.cnpj == '20.018.183/0001-80'
