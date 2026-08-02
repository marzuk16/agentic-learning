from collections.abc import Iterator

from src.rag.llm.base import LLMService
from src.rag.prompts.rag import (
    RAG_SYSTEM_PROMPT,
    RAG_USER_PROMPT_TEMPLATE,
)
from src.rag.services.search_service import SearchService


class RAGService:

    def __init__(
        self,
        search_service: SearchService,
        llm_service: LLMService,
    ):
        self.search_service = search_service
        self.llm_service = llm_service


    def stream_answer(
        self,
        question: str,
    ) -> Iterator[str]:

        chunks = self.search_service.search(
            query=question,
        )

        context = "\n\n".join(
            chunk.content
            for chunk in chunks
        )

        user_prompt = RAG_USER_PROMPT_TEMPLATE.format(
            context=context,
            question=question,
        )

        messages = [
            {
                "role": "system",
                "content": RAG_SYSTEM_PROMPT,
            },
            {
                "role": "user",
                "content": user_prompt,
            },
        ]

        yield from self.llm_service.stream(
            messages
        )
