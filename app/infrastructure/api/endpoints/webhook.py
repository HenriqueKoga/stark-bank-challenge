from fastapi import APIRouter, Depends, HTTPException, Request

from app.application.use_cases.event_handler_service import EventHandlerService
from app.domain.event.event import EventFactory
from app.infrastructure.api.dependencies import get_event_handler_service

router = APIRouter()


@router.post("/webhook")
async def handle_invoice_event(request: Request, event_handler_service: EventHandlerService = Depends(get_event_handler_service)):
    try:
        payload = await request.json()
        event = EventFactory.from_dict(payload)
        event_handler_service.handle(event)
        return {"status": "success"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e)) from e
