from src.rag.chunking.models import TextChunk
from src.db.models.chunk import Chunk


def to_chunk_entity(
    text_chunk: TextChunk,
    document_id,
):

    return Chunk(
        document_id=document_id,
        chunk_index=text_chunk.index,
        content=text_chunk.content,
        metadata_=text_chunk.metadata,
    )