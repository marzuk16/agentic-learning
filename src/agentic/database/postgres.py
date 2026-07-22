"""Postgres connectivity wired to configuration.

The engine is built from `settings.postgres_dsn`, so host/port/credentials
all come from `.env` — no connection details are hardcoded here.
"""

from collections.abc import Iterator
from contextlib import contextmanager

from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import Session, sessionmaker

from agentic.config.settings import Settings, get_settings


def build_engine(settings: Settings | None = None) -> Engine:
    """Create a SQLAlchemy engine from settings."""
    settings = settings or get_settings()
    return create_engine(settings.postgres_dsn, pool_pre_ping=True)


# Module-level engine + session factory (created once, reused everywhere).
engine: Engine = build_engine()
SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)


@contextmanager
def get_session() -> Iterator[Session]:
    """Yield a session, committing on success and rolling back on error."""
    session = SessionLocal()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()
