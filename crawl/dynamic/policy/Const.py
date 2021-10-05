
# 파이썬에는 상수라는 개념이 없어서 const 개념을 직접 만들어준다
def constant(func):
    def func_set(self, val):
        raise TypeError

    def func_get(self):
        return func(self)
    return property(func_get, func_set)


class _Musical(object):

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