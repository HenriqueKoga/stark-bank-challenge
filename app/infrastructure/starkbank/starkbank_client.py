import os

import starkbank

from app.domain.account.account import Account
from app.domain.invoice.invoice import Invoice
from app.utils.file_utils import get_file_content


class StarkbankClient:
    def __init__(self):
        self.user = starkbank.Project(
            environment="sandbox",
            id="6239578461569024",
            private_key=get_file_content(os.environ["STARK_BANK_PRIVATE_KEY"])
        )
        starkbank.user = self.user

    def issue_invoices(self, invoices: list[Invoice]):
        for invoice in invoices:
            starkbank.boleto.create([
                starkbank.Boleto(
                    amount=invoice.amount,
                    due=invoice.due_date.isoformat(),
                    name=invoice.client.name,
                    tax_id=invoice.client.cpf,
                    street_line_1=invoice.client.address.full_address,
                    street_line_2=invoice.client.address.complement,
                    district=invoice.client.address.district,
                    city=invoice.client.address.city,
                    state_code=invoice.client.address.state,
                    zip_code=invoice.client.address.zip_code,
                )
            ])

    def transfer(self, account: Account, amount: int):
        starkbank.transfer.create([
            starkbank.Transfer(
                amount=amount,
                tax_id=account.cnpj,
                name=account.name,
                bank_code=account.bank_code,
                branch_code=account.branch,
                account_number=account.number,
                account_type=account.account_type,
            )
        ])
