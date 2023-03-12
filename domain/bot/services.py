from abc import ABC, abstractmethod
from typing import List

from domain.bot.dto.entity import Content, Meta


class BotService(ABC):

    @abstractmethod
    def get_meta(self, query_params: dict = None) -> Meta:
        pass

    @abstractmethod
    def get_resources(self, query_params: dict = None) -> List[Content]:
        pass

    @abstractmethod
    def run(self, contents: List[Content]) -> None:
        pass
