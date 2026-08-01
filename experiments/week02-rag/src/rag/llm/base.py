from abc import ABC, abstractmethod


class LLMService(ABC):

    @abstractmethod
    def generate(
        self,
        messages: list[dict],
    ) -> str:
        pass


    @abstractmethod
    def stream(
        self,
        messages: list[dict],
    ):
        pass