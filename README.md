# ThirdPlace Backend

Scoring / ranking service for ThirdPlace.

Fresh start — 2026-10-12.

---

## Phase 0 foundation

Python / FastAPI service. This repo currently contains the **Phase 0 engineering
foundation only**. It exposes operational endpoints (`/health`, `/meta`) and no
product/public routes. The public API contract and database schema are
`BLOCKED_CONTRACT_GAP` / `BLOCKED_NOT_V22_CERTIFIED` until the authoritative V2.2
specification is imported and founder-approved.

### Stack

- Python 3.9+ · FastAPI · Uvicorn · Pydantic v2
- Celery + Redis (broker/result)
- Supabase (Postgres/PostGIS/Auth/Storage/Realtime) — client boundary only
- Ruff · Black · mypy (strict) · pytest

### Boundary

```
API  ->  domain service  ->  repository  ->  PostgreSQL/Supabase
```

### Layout

```
backend/
  api/            FastAPI routers (ops only: /health, /meta)
  domain/         business logic (empty until approved contracts)
  repositories/   persistence boundary (generic protocol only)
  adapters/       Supabase + Celery/Redis boundaries
  outbox/         transactional outbox placeholder
migrations/       EMPTY — Gate 5 schema blocked
tests/            pytest
docs/             baseline, ledger, blocker report
```

### Develop

```bash
python -m venv .venv && . .venv/Scripts/activate   # Windows
pip install -e ".[dev]"
uvicorn backend.main:app --reload                   # http://localhost:8000
ruff check . && black --check . && mypy && pytest
```

Copy `.env.example` → `.env`. The Supabase **service-role key is server-side
only** and must never reach a client.

See `docs/IMPLEMENTATION_BASELINE.md` and `docs/PHASE0_BLOCKER_REPORT.json`.
