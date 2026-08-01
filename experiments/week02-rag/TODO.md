# TODO — Alembic migrations

## Why
`embedding_dim` sets the width of `chunks.embedding` (`Vector(N)`) **at `CREATE TABLE` time**.
Today the schema is created by `scripts/create_tables.py` (create-only, not versioned), so
there is no safe, non-destructive path to change the embedding model/dimension, add columns,
or evolve the schema. Alembic gives us versioned, reversible migrations.

## Tasks
- [ ] Add `alembic` to the `database` dependency group in `pyproject.toml`; `uv sync`.
- [ ] `alembic init alembic` (sync engine — we use `psycopg`, not async).
- [ ] Wire `alembic/env.py`:
  - [ ] `sqlalchemy.url` from `src.config.settings.database_url` (don't hardcode in `alembic.ini`).
  - [ ] `import src.db.models` so `Document` + `Chunk` register on `Base.metadata`; set `target_metadata = Base.metadata`.
  - [ ] Add a `render_item` hook (or import in `script.py.mako`) so autogenerate emits
        `pgvector.sqlalchemy.Vector(...)` instead of a broken/`NULL` type.
- [ ] Baseline migration (replaces `create_tables.py`):
  - [ ] `op.execute("CREATE EXTENSION IF NOT EXISTS vector")` **before** table creation.
  - [ ] Create `content_type` enum, `documents`, `chunks` (incl. `Vector(embedding_dim)`, `metadata` JSONB, FK cascade).
  - [ ] Verify `alembic upgrade head` on a clean DB produces the same schema as the current models.
- [ ] Retire / demote `scripts/create_tables.py` (keep as a dev shortcut or delete); document
      `alembic upgrade head` as the canonical setup step in the README.
- [ ] **Change-embedding-model migration** (the motivating case):
  - [ ] `op.alter_column("chunks", "embedding", type_=Vector(<new_dim>))` — note existing vectors
        of a different dim **cannot** be reinterpreted; treat as a re-embed, not an in-place cast.
  - [ ] Backfill strategy: truncate `chunks` + re-ingest, **or** a data migration that re-embeds
        `content` with the new model and rewrites vectors. Decide and document which.
  - [ ] Keep the `LocalEmbeddingService` dim guard in sync with the target `EMBEDDING_DIM`.
- [ ] Add convenience commands (Makefile or README): `revision --autogenerate -m`, `upgrade head`, `downgrade -1`.

## Gotchas
- **pgvector + autogenerate**: the `Vector` type must be importable/renderable in `versions/*`
  or autogenerate produces invalid migrations.
- **Extension ordering**: `CREATE EXTENSION vector` must run before any `Vector` column is created.
- **Native enum**: `content_type` is a Postgres enum — autogenerate/downgrade must create/drop the type.
- **Dimension changes are destructive** to stored vectors — always pair a dim change with a re-embed.
