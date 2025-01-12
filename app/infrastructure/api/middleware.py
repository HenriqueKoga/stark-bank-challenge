import os

from fastapi import HTTPException, Request
from starlette.middleware.base import BaseHTTPMiddleware

ALLOWED_IPS = {
    "127.0.0.1",
    "localhost",
    "::1",
    os.getenv("STARK_BANK_IP_ADDRESS_1"),
    os.getenv("STARK_BANK_IP_ADDRESS_2"),
}


class IPFilterMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        client_ip = request.client.host
        if client_ip not in ALLOWED_IPS:
            raise HTTPException(status_code=403, detail="Access denied")
        return await call_next(request)
