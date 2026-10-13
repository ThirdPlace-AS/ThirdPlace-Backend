"""Supabase client boundary.

Builds a client lazily from server-side settings. NO schema, queries, tables,
or RLS policies are defined here — those are Gate 5 (migration-first, backend
owned) and remain BLOCKED until the approved V2.2 schema exists. Mobile clients
never receive the service-role key.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Optional

from backend.config import get_settings

if TYPE_CHECKING:  # pragma: no cover
    from supabase import Client


def get_client() -> Optional[Client]:
    """Return a Supabase client, or None if not configured (Phase 0 default)."""
    settings = get_settings()
    if not settings.supabase_url or not settings.supabase_service_role_key:
        return None
    from supabase import create_client

    return create_client(settings.supabase_url, settings.supabase_service_role_key)
