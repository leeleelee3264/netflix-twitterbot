from abc import ABC, abstractmethod
from typing import List

from domain.bot.entity import Meta, Content


class BotService(ABC):

    @abstractmethod
    def get_meta(self) -> Meta:
        pass

    @abstractmethod
    def get_resources(self, page: int) -> List[Content]:
        pass

    @abstractmethod
    def upload(self, contents: List[Content]) -> None:
        pass
