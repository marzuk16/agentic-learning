from sqlalchemy import text

from src.db.base import Base
from src.db.database import engine

# Import models so they are registered with Base.metadata
from src.db.models import Document, Chunk


def create_tables() -> None:
    # pgvector's Vector column type requires the extension to exist first.
    with engine.begin() as conn:
        conn.execute(text("CREATE EXTENSION IF NOT EXISTS vector"))

    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    create_tables()
    print("Tables created successfully.")