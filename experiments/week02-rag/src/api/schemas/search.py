from pydantic import BaseModel, Field


class SearchRequest(BaseModel):
    query: str = Field(
        min_length=1,
    )

    limit: int | None = Field(
        default=None,
        ge=1,
        le=20,
    )


class SearchResult(BaseModel):
    id: str
    content: str
    metadata: dict | None = None


class SearchResponse(BaseModel):
    results: list[SearchResult]