from crawl.regex import change_whitespace


class Musical:
    def __init__(self, name, poster_path, full_period):
        self.name = name
        self.poster_path = poster_path
        self.__cal_period(full_period)

    def fetch_in_info_tab(self, cast_text, place):
        self.__fetch_cast(cast_text)
        self.__fetch_place(place)

    def __fetch_cast(self, cast_text):
        self.cast = cast_text

    def __fetch_place(self, place):
        self.place = place

    def __cal_period(self, full_period):
        _period = change_whitespace(full_period, '')
        middle_tilde = _period.find('~')

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
