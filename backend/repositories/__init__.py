"""Repository layer — the only layer that talks to PostgreSQL/Supabase.

Defines a generic persistence boundary. No concrete repositories or canonical
tables exist in Phase 0.
"""

from __future__ import annotations

from typing import Generic, Optional, Protocol, TypeVar

# Covariant return, contravariant id — correct variance for a read protocol.
T_co = TypeVar("T_co", covariant=True)
IdT_contra = TypeVar("IdT_contra", contravariant=True)


class Repository(Protocol, Generic[T_co, IdT_contra]):
    """Generic read boundary. Concrete repos arrive with approved V2.2 entities."""

    def get(self, id: IdT_contra) -> Optional[T_co]:  # pragma: no cover - interface
        ...
