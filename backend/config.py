"""Application settings, loaded from environment.

No secrets are hard-coded. Supabase service-role credentials, if provided, stay
server-side only and are never exposed to clients. All fields are optional at
Phase 0 because no external system is actually contacted yet.
"""

from __future__ import annotations

from functools import lru_cache
from typing import Optional

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="TP_",
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    environment: str = "development"
    app_name: str = "thirdplace-backend"

    # Boundaries — not contacted in Phase 0; presence is validated lazily.
    supabase_url: Optional[str] = None
    supabase_service_role_key: Optional[str] = None
    redis_url: str = "redis://localhost:6379/0"


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    return Settings()
