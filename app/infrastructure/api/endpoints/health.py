import os

from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
async def health_check():
    return {
        "status": "ok",
        "version": os.getenv("VERSION", "v0")
    }
