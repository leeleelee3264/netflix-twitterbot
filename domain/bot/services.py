from abc import ABC, abstractmethod
from typing import List

from domain.bot.entity import Content, Meta


class BotService(ABC):

    @abstractmethod
    def get_meta(self) -> Meta:
        pass

    @abstractmethod
    def get_resources(self) -> List[Content]:
        pass

    @abstractmethod
    def run(self, contents: List[Content]) -> None:
        pass
