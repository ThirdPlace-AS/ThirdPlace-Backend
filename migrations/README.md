# Migrations

**Intentionally empty of schema.**

Gate 5 (database) is backend-owned, migration-first, greenfield Supabase schema
consolidated from the authoritative V2.2 spec, with strict RLS, PostGIS, and
transactional invariants. That schema does **not** exist yet
(`BLOCKED_NOT_V22_CERTIFIED`), so there are no migrations here.

Hard rules when migrations do land (master spec §4):

- UUID primary keys (prefer time-sortable UUIDv7 where supported).
- `timestamptz`, UTC storage.
- PostGIS for geography.
- RLS enforced per role + resource membership; least-privilege personas.
- No migration/backfill/dual-write/cutover from any legacy prototype.

Do **not** derive tables from historical entity counts (140/147/164/176/240/241)
or from the 249-row ledger. `creator_payables` is rejected. Only named,
founder-approved V2.2 entities become tables.
