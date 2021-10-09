
# 파이썬에는 상수라는 개념이 없어서 const 개념을 직접 만들어준다
def constant(func):
    def func_set(self, val):
        raise TypeError

    def func_get(self):
        return func(self)
    return property(func_get, func_set)


class _Musical(object):

    @constant
    def DATE_FORMAT(self):
        return '%Y.%m.%d'

    @constant
    def MUSICAL_URL(self):
        return "http://ticket.interpark.com/contents/Ranking/RankList?pKind=01011&pCate=&pType=M&pDate="

    @constant
    def CAST_INFO_TAB_NAME(self):
        return "부가정보"

    @constant
    def CAST_INFO_TAB_CLASS(self):
        return "navLink"

    @constant
    def CAST_INFO_TEXT_CLASS(self):
        return "moreInfoCast"

    @constant
    def NAME_CLASS(self):
        return "prdTitle"

    @constant
    def PLACE_XPATH(self):
        return "//*[@id=\"productMainBody\"]/div/div[2]/table/tbody/tr[3]/td[2]"


    @constant
    def DATE_XPATH(self):
        return "//*[@id=\"container\"]/div[5]/div[1]/div[2]/div[1]/div/div[2]/ul/li[2]/div/p"

    @constant
    def POSTER_XPATH(self):
        return '//*[@id="container"]/div[5]/div[1]/div[2]/div[1]/div/div[2]/div/div[1]/img'


class _Server(object):

    @constant
    def EMPTY_STRING(self):
        return ""

    @constant
    def EMPTY_INT(self):
        return -1

    @constant
    def WAIT_TIME(self):
        return 5