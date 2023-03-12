from typing import List

from domain.bot.entity import Content
from domain.bot.service import BotService


class BotUseCase:

    def __init__(self, service: BotService):
        self._bot_service = service

    def run(self):
        total_resources = self._fetch_resources()
        self._bot_service.upload(total_resources)

    def _fetch_resources(self) -> List[Content]:
        pages = self._bot_service.get_meta().total_page
        resources = []

        for i in range(1, pages + 1):
            resource = self._bot_service.get_resources(page=i)
            resources += resource

        return resources
