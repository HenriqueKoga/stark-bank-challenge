from app.domain.address.address import Address
from app.domain.client.client import Client, ClientNotFound
from app.infrastructure.repositories.interfaces.client_repository import ClientRepositoryInterface


class ClientLocalRepository(ClientRepositoryInterface):
    clients = [
        Client(id=1, name="Alice", cpf="048.225.160-32", address=Address(
            street="Rua A",
            number=1,
            complement="apto 123",
            district="Bairro A",
            city="Cidade A",
            state="SP",
            country="BR",
            zip_code="12345-678"
        )),
        Client(id=2, name="Bob", cpf="206.905.390-37", address=Address(
            street="Rua B",
            number=2,
            complement="apto 234",
            district="Bairro B",
            city="Cidade B",
            state="BA",
            country="BR",
            zip_code="23456-789"
        )),
        Client(id=3, name="Charlie", cpf="803.002.970-50", address=Address(
            street="Rua C",
            number=3,
            complement="apto 345",
            district="Bairro C",
            city="Cidade C",
            state="RJ",
            country="BR",
            zip_code="34567-890"
        )),
        Client(id=4, name="David", cpf="755.979.660-57", address=Address(
            street="Rua D",
            number=4,
            complement="apto 456",
            district="Bairro D",
            city="Cidade D",
            state="CE",
            country="BR",
            zip_code="45678-901"
        )),
        Client(id=5, name="Eve", cpf="211.662.200-01", address=Address(
            street="Rua E",
            number=5,
            complement="apto 567",
            district="Bairro E",
            city="Cidade E",
            state="AM",
            country="BR",
            zip_code="56789-012"
        )),
        Client(id=6, name="Frank", cpf="248.954.990-14", address=Address(
            street="Rua F",
            number=6,
            complement="apto 678",
            district="Bairro F",
            city="Cidade F",
            state="PA",
            country="BR",
            zip_code="67890-123"
        )),
        Client(id=7, name="Grace", cpf="450.649.480-69", address=Address(
            street="Rua G",
            number=7,
            complement="apto 789",
            district="Bairro G",
            city="Cidade G",
            state="TO",
            country="BR",
            zip_code="78901-234"
        )),
        Client(id=8, name="Heidi", cpf="666.632.660-12", address=Address(
            street="Rua H",
            number=8,
            complement="apto 890",
            district="Bairro H",
            city="Cidade H",
            state="GO",
            country="BR",
            zip_code="89012-345"
        )),
        Client(id=9, name="Ivan", cpf="978.388.330-51", address=Address(
            street="Rua I",
            number=9,
            complement="apto 901",
            district="Bairro I",
            city="Cidade I",
            state="MA",
            country="BR",
            zip_code="90123-456"
        )),
        Client(id=10, name="Judy", cpf="640.712.640-12", address=Address(
            street="Rua J",
            number=10,
            complement="apto 012",
            district="Bairro J",
            city="Cidade J",
            state="PI",
            country="BR",
            zip_code="01234-567"
        )),
        Client(id=11, name="Kevin", cpf="305.523.400-65", address=Address(
            street="Rua K",
            number=11,
            complement="apto 123",
            district="Bairro K",
            city="Cidade K",
            state="SC",
            country="BR",
            zip_code="12345-678"
        )),
        Client(id=12, name="Linda", cpf="158.699.780-76", address=Address(
            street="Rua L",
            number=12,
            complement="apto 234",
            district="Bairro L",
            city="Cidade L",
            state="RS",
            country="BR",
            zip_code="23456-789"
        )),
        Client(id=13, name="Michael", cpf="657.195.110-08", address=Address(
            street="Rua M",
            number=13,
            complement="apto 345",
            district="Bairro M",
            city="Cidade M",
            state="PR",
            country="BR",
            zip_code="34567-890"
        )),
    ]

    def get_all(self) -> list[Client]:
        return self.clients

    def get_by_id(self, client_id: int) -> Client:
        client = next((client for client in self.clients if client.id == client_id), None)
        if client is None:
            raise ClientNotFound(f"Client with id {client_id} not found")

        return client

    def get_by_cpf(self, cpf: str) -> Client:
        client = next((client for client in self.clients if client.cpf == cpf), None)
        if client is None:
            raise ClientNotFound(f"Client with cpf {cpf} not found")

        return client
