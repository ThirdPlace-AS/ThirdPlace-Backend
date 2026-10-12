# ThirdPlace Backend — Implementation Baseline (Phase 0)

**Source package:** TP-SOT-v1.1.0-2026-10-12
**Disposition:** `BLOCKED_NOT_V22_CERTIFIED`
**Repo:** `ThirdPlace-AS/ThirdPlace-Backend` (two-repo topology, founder-locked TP-D-006)

## Authority & boundary

Canonical layered boundary (master spec):

```
API  ->  domain service  ->  repository  ->  PostgreSQL/Supabase
```

- `backend/api/` — FastAPI routers; Phase 0 exposes only `/health`, `/meta`.
- `backend/domain/` — business logic; no entities/services yet.
- `backend/repositories/` — the only layer touching Supabase; generic protocol only.
- `backend/adapters/` — vendor boundaries (Supabase client, Celery/Redis); nothing contacted.
- `backend/outbox/` — transactional outbox boundary placeholder.
- `migrations/` — intentionally empty (Gate 5 blocked).

## What Phase 0 established

| Deliverable | State |
|---|---|
| Repository structure baseline | DONE — `backend/`, `migrations/`, `tests/`, `docs/` |
| Stack baseline | DONE — Python 3.12+, FastAPI, Celery, Redis, Supabase client boundary |
| FastAPI app | DONE — `/health`, `/meta` only (no domain routes) |
| Celery/Redis wiring | DONE — app + one no-op `ops.health` task |
| Supabase boundary | DONE — lazy client from server-side env; no schema/RLS |
| Env/secrets checklist | DONE — `.env.example` (TP_* vars; service-role server-side only) |
| Test infrastructure baseline | DONE — pytest + `/health` + `/meta` tests |
| Lint / format / types | DONE — Ruff, Black, mypy (strict) |
| Progressive CI (partial Gate 7) | DONE — ruff/black/mypy/pytest on PR; contract/migration/scenario CI is a placeholder |
| Migrations | EMPTY — no schema invented |

## Canonical registry checks (status at Phase 0)

- Entity / API / state-machine / event registries: BLOCKED (no approved V2.2 contract).
- RLS/authorization matrix: baseline empty, awaiting approved schema (Gate 5).

## Required rule honored

No migration/backfill/dual-write/dual-read/cutover/legacy-schema preservation
(master spec:11840). Greenfield only.

## Next safe slice

First contract-bearing slice (any real route, DTO, entity, or migration) is gated
on importing the authoritative V2.2 spec, the 435-scenario registry, and the
verbatim Gates 1-4 text. See `docs/implementation-ledger/`.
