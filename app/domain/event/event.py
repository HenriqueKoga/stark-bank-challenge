from abc import ABC

from pydantic import BaseModel


class InvalidEvent(Exception):
    pass


class Event(BaseModel, ABC):
    raw: dict


class InvoiceEvent(Event):
    type: str
    data: dict


class EventFactory:
    @classmethod
    def from_dict(cls, data: dict) -> Event:
        try:
            raw_event = data['event']
            if raw_event['subscription'] == 'boleto':
                return InvoiceEvent(
                    raw=raw_event,
                    type=raw_event['log']['type'],
                    data=raw_event['log']['boleto']
                )
            raise InvalidEvent(f'Invalid event: {data}')
        except KeyError as e:
            raise InvalidEvent(f'Invalid event: {data}') from e
