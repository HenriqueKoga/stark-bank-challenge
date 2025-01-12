from fastapi import FastAPI

from app.infrastructure.api.middleware import IPFilterMiddleware
from app.infrastructure.api.routers import router

app = FastAPI()
app.include_router(router)
app.add_middleware(IPFilterMiddleware)
