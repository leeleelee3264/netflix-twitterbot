import datetime
import re

from crawl.db.model.cast import Cast
from crawl.regex import get_last_index_of_digit


class Schedule:
    def __init__(self, musical_id, full_text):
        self.musical_id = musical_id
        self.__cal__date(full_text)
        self.cast = Cast(musical_id, self.date, self.time, full_text)

    def __cal__date(self, full_text):
        last_digit_index = get_last_index_of_digit(full_text) + 1
        date_text = full_text[:last_digit_index]

        my_datetime = self.__get_this_datetime(date_text)
        self.date = my_datetime.strftime('%Y-%m-%d')
        self.time = my_datetime.strftime('%H:%M:%S')

    def __remove_korean_date(self, date_text):
        return re.sub(r'\([^)]*\)', '', date_text)

    def __get_this_datetime(self, date_text):
        without_korean_date = self.__remove_korean_date(date_text)
        without_year = datetime.datetime.strptime(without_korean_date, '%m/%d %H:%M')

        today = datetime.datetime.now()
        this_year = today.year
        with_year = without_year.replace(year=this_year)

        if with_year < today:
            with_year = without_year.replace(year=this_year +1)

        return with_year
