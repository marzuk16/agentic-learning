from sqlalchemy import select
from sqlalchemy.orm import Session

from src.db.models.chunk import Chunk


class ChunkRepository:

    def __init__(
        self,
        session: Session,
    ):
        self.session = session


    def create_many(
        self,
        chunks: list[Chunk],
    ):

        self.session.add_all(chunks)

        self.session.flush()

        return chunks
    
    def similarity_search(
        self,
        embedding: list[float],
        limit: int = 5,
    ) -> list[Chunk]:

        statement = (
            select(Chunk)
            .order_by(
                Chunk.embedding.cosine_distance(
                    embedding
                )
            )
            .limit(limit)
        )

        result = self.session.execute(
            statement
        )

        return result.scalars().all()