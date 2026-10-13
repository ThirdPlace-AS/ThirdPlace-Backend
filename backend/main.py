"""FastAPI application factory.

Phase 0 exposes ONLY operational endpoints (/health, /meta). No domain or
public product routes exist — the public API contract is BLOCKED_CONTRACT_GAP
until the authoritative V2.2 specification is imported and founder-approved.
"""

from __future__ import annotations

from fastapi import FastAPI

from backend import __version__
from backend.api.health import router as health_router


def create_app() -> FastAPI:
    app = FastAPI(
        title="ThirdPlace Backend",
        version=__version__,
        docs_url="/docs",
        openapi_url="/openapi.json",
    )
    app.include_router(health_router)
    return app


app = create_app()
