from pydantic import BaseModel


class AccountNotFound(Exception):
    pass


class Account(BaseModel):
    id: int
    bank_code: str
    branch: str
    number: str
    name: str
    cnpj: str
    account_type: str
