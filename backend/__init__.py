"""ThirdPlace backend package (Phase 0 foundation).

Layered boundary (master spec):
    API -> domain service -> repository -> PostgreSQL/Supabase

Phase 0 is non-contract: no canonical entities, DTOs, state machines, events,
migrations, or RLS policies are defined. Only /health and /meta are exposed.
"""

__version__ = "0.0.0"
