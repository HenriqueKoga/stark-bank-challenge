from fastapi import Depends

from app.application.interfaces.transfer_service import TransferServiceInterface
from app.application.use_cases.event_handler_service import EventHandlerService
from app.application.use_cases.transfer_service import TransferService
from app.infrastructure.repositories.account_local_repository import AccountLocalRepository
from app.infrastructure.repositories.interfaces.account_repositoy import AccountRepositoryInterface


def get_account_repository():
    return AccountLocalRepository()


def get_transfer_service(account_repository: AccountRepositoryInterface = Depends(get_account_repository)):
    return TransferService(account_repository)


def get_event_handler_service(transfer_service: TransferServiceInterface = Depends(get_transfer_service)):
    return EventHandlerService(transfer_service)
