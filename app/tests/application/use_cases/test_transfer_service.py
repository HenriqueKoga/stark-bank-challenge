from unittest.mock import MagicMock

import pytest

from app.application.use_cases.transfer_service import TransferService
from app.infrastructure.repositories.interfaces.account_repositoy import AccountRepositoryInterface


@pytest.fixture
def starkbanck_client_mock(mocker):
    return mocker.patch('app.application.use_cases.transfer_service.StarkbankClient')


def test_transfer(starkbanck_client_mock: MagicMock):
    account_repository = MagicMock(spec=AccountRepositoryInterface)

    service = TransferService(account_repository)
    service.transfer('123456789', 1000, 10)

    account_repository.get_by_cnpj.assert_called_once_with('123456789')
    starkbanck_client_mock().transfer.assert_called_once_with(account_repository.get_by_cnpj.return_value, 990)
