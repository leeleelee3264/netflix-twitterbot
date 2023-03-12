from typing import List

import requests.exceptions

from domain.bot.entity import Meta, Content
from domain.bot.exceptions import MetaNotFoundError, ResourcesNotFoundError
from domain.bot.services import BotService
from services.netflix_bot.mapper import NetflixResponseMapper


class NetflixBotService(BotService):

    def __init__(self):
        self._endpoint = 'https://about.netflix.com/api/data/releases'
        self._mapper = NetflixResponseMapper()

    def get_meta(self, query_params: dict = None) -> Meta:

        try:
            payload = self._get(url=self._endpoint, query_params=query_params)
            return self._mapper.build_meta(payload)
        except requests.exceptions.HTTPError as e:
            raise MetaNotFoundError(
                'Netflix meta data not found. '
                f'{e.response.content}'
            )

    def get_resources(self, query_params: dict = None) -> List[Content]:

        try:
            payload = self._get(url=self._endpoint, query_params=query_params)
            return self._mapper.build_resources(payload)
        except requests.exceptions.HTTPError as e:
            raise ResourcesNotFoundError(
                'Netflix resources not found. '
                f'{e.response.content}'
                f'{query_params}'
            )

    def run(self, contents: List[Content]) -> None:
        pass

    def _get(self, url, query_params: dict = None) -> dict:

        try:
            headers = {'Content-Type': 'application/json'}

            res = requests.get(
                url=url,
                headers=headers,
                params=query_params,
            )

            res.raise_for_status()
            payload = res.json()

            return payload
        except requests.exceptions.RequestException as e:
            print('Error: ', e)
