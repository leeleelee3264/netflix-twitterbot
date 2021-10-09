from crawl.db.model.insert_factory import InsertQuery
from crawl.regex import change_whitespace


class Musical(InsertQuery):

    def get_insert_query(self):

        query = """
        insert into %s (interpark_id, interpark_path, name, place, cast, start_date, end_date, poster_path)
        values('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')
        """ % ("mt_musical", self.interpark_id, self.interpark_path, self.name, self.place, self.cast, self.start_date, self.end_date, self.poster_path)

        return query

    def __init__(self, name, poster_path, full_period, current_url):
        self.name = name
        self.poster_path = poster_path
        self.__cal_period(full_period)
        self.__fetch_interpark_data(current_url)

    def __fetch_interpark_data(self, current_url):
        self.interpark_path = current_url
        self.__cal_product_id(current_url)

    def __cal_product_id(self, current_url):
        _split_char = '/'
        last_slash = current_url.rfind(_split_char)

        t_product_id = current_url[last_slash+1:]
        self.interpark_id = t_product_id

    def fetch_in_info_tab(self, cast_text, place):
        self.__fetch_cast(cast_text)
        self.__fetch_place(place)

    def __fetch_cast(self, cast_text):
        self.cast = cast_text

    def __fetch_place(self, place):
        self.place = place

    def __cal_period(self, full_period):
        _period = change_whitespace(full_period, '')
        _split_char = '~'

        middle_tilde = _period.find(_split_char)

        startStr = _period[:middle_tilde]
        endStr = _period[middle_tilde + 1:]

        self.start_date = startStr
        self.end_date = endStr

    def __str__(self):
        return """
        Title: %s 
        공연장: %s 
        기간: %s ~ %s 
        캐스팅: %s
        """ % (self.name, self.place, self.start_date, self.end_date, self.cast)
