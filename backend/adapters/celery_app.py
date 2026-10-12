"""Celery application wired to a Redis broker.

Phase 0 registers a single no-op health task to prove the worker boundary is
correctly configured. No domain/background jobs exist yet.
"""

from __future__ import annotations

from celery import Celery

from backend.config import get_settings

settings = get_settings()

celery_app = Celery(
    "thirdplace",
    broker=settings.redis_url,
    backend=settings.redis_url,
)
celery_app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="UTC",
    enable_utc=True,
)


@celery_app.task(name="ops.health")  # type: ignore[untyped-decorator]
def health_task() -> str:
    """No-op task used to verify worker/broker wiring."""
    return "ok"
