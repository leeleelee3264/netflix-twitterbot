import datetime
from typing import List

from domain.bot.entity import Meta, Content


class NetflixResponseMapper:

    def __init__(self):
        self._key_total_items = 'totalItems'
        self._key_total_pages = 'totalPages'
        self._key_per_page = 'perPage'

        self._key_data = 'data'

        self._key_title = 'title1'
        self._key_start_time ='startTime'
        self._key_image = 'image'

    def build_meta(self, payload: dict) -> Meta:

        return Meta(
            total_items=payload.get(self._key_total_items),
            total_page=payload.get(self._key_total_pages),
            per_page=payload.get(self._key_per_page),
        )

    def build_resources(self, payload: dict) -> List[Content]:
        data = payload.get(self._key_data)

        return [self._build_resource(s_data) for s_data in data]

    def _build_resource(self, payload: dict) -> Content:

        epoch_time = payload.get(self._key_start_time)
        start_time = datetime.datetime.fromtimestamp(epoch_time).date()

        start_time_str = start_time.strftime('%Y-%m-%d')

        return Content(
            title=payload.get(self._key_title),
            start_time=start_time_str,
            image=payload.get(self._key_image),
        )
