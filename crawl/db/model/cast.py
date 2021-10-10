from crawl.regex import change_whitespace, get_last_index_of_digit


class Cast:
    def __init__(self, musical_id, date, time , full_text):
        self.musical_id = musical_id
        self.date = date
        self.time = time
        self.__cal_this_cast(full_text)

    def __cal_this_cast(self, full_text):
        last_digit_index = get_last_index_of_digit(full_text) + 1
        cast_text = full_text[last_digit_index:]
        self.cast = change_whitespace(cast_text.strip(), ',')
