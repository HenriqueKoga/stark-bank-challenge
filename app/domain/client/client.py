from pydantic import BaseModel

from app.domain.address.address import Address


class ClientNotFound(Exception):
    pass


class Client(BaseModel):
    id: int
    name: str
    cpf: str
    address: Address
