from pydantic import BaseModel


class Address(BaseModel):
    street: str
    number: int
    complement: str
    district: str
    city: str
    state: str
    country: str
    zip_code: str

    @property
    def full_address(self):
        return f"{self.street}, {self.number}"
