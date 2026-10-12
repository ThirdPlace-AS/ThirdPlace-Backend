"""Operational endpoints. These are NOT product/public contract routes."""

from __future__ import annotations

from fastapi import APIRouter
from pydantic import BaseModel

from backend import __version__
from backend.config import get_settings

router = APIRouter(tags=["ops"])


class HealthResponse(BaseModel):
    status: str


class MetaResponse(BaseModel):
    name: str
    version: str
    environment: str
    disposition: str


@router.get("/health", response_model=HealthResponse)
def health() -> HealthResponse:
    return HealthResponse(status="ok")


@router.get("/meta", response_model=MetaResponse)
def meta() -> MetaResponse:
    settings = get_settings()
    return MetaResponse(
        name=settings.app_name,
        version=__version__,
        environment=settings.environment,
        # Honest governance signal surfaced by the service itself.
        disposition="BLOCKED_NOT_V22_CERTIFIED",
    )
