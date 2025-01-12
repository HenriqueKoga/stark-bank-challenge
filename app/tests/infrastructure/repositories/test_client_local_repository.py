import pytest

from app.domain.client.client import Client, ClientNotFound
from app.infrastructure.repositories.client_local_repository import ClientLocalRepository


def test_get_all():
    repository = ClientLocalRepository()
    clients = repository.get_all()

    assert all(isinstance(client, Client) for client in clients)


def test_get_by_id():
    repository = ClientLocalRepository()
    client = repository.get_by_id(1)

    assert isinstance(client, Client)
    assert client.id == 1


def test_get_by_id_not_found():
    repository = ClientLocalRepository()

    with pytest.raises(ClientNotFound):
        repository.get_by_id(-1)


def test_get_by_cpf():
    repository = ClientLocalRepository()
    client = repository.get_by_cpf("048.225.160-32")

    assert isinstance(client, Client)
    assert client.cpf == "048.225.160-32"
