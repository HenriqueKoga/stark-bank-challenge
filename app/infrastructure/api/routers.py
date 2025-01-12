from fastapi import APIRouter

from app.infrastructure.api.endpoints import health, webhook

router = APIRouter()
router.include_router(webhook.router, tags=["webhook"])
router.include_router(health.router, tags=["health"])
