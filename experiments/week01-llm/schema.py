from pydantic import BaseModel

class ReviewResponse(BaseModel):
    summary: str
    bugs: list[str]
    improvements: list[str]