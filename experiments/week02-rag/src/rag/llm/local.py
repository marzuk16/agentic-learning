from collections.abc import Iterator

from openai import OpenAI

from src.config import settings
from src.rag.llm.base import LLMService


class LocalLLMService(LLMService):

    def __init__(
        self,
        model: str | None = None,
        temperature: float = 0.2,
    ):
        self.model = model or settings.llm_model
        self.temperature = temperature

        self.client = OpenAI(
            base_url=settings.llm_base_url,
            api_key=settings.llm_api_key,
        )


    def generate(
        self,
        messages: list[dict],
    ) -> str:

        response = (
            self.client.chat.completions.create(
                model=self.model,
                temperature=self.temperature,
                messages=messages,
            )
        )

        return response.choices[0].message.content


    def stream(
        self,
        messages: list[dict],
    ) -> Iterator[str]:

        response = (
            self.client.chat.completions.create(
                model=self.model,
                temperature=self.temperature,

                stream=True,

                messages=messages,
            )
        )


        for chunk in response:

            token = (
                chunk
                .choices[0]
                .delta
                .content
            )

            if token:
                yield token
