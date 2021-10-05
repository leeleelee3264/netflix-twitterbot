# 진짜 파싱을 하는 코드


from selenium.webdriver.common.by import By

import actor as actor
import crawl.dynamic.driver_util as util
from crawl.dynamic import driver
from crawl.dynamic.policy.Const import _Musical, _Server

MConst = _Musical()
SConst = _Server()

TARGET_URL_MUSICAL = MConst.MUSICAL_URL

CAST_INFO_TAB_NAME = MConst.CAST_INFO_TAB_NAME
CAST_INFO_TAB_CLASS = MConst.CAST_INFO_TAB_CLASS
CAST_INFO_TEXT_CLASS = MConst.CAST_INFO_TEXT_CLASS

GENERAL_WAIT_TIME = SConst.WAIT_TIME

EMPTY = '정보없음'

# TODO: 얘는 없어질 예정
def get_cast_text(_driver, selector, limit_time):
    text_container = util.wait_class_elements(_driver, selector, limit_time)

    if text_container is None:
        return EMPTY

    return get_text(text_container)



def get_text(elemet):

    try:
        if elemet.text == '해당없음':
            return EMPTY
        return elemet.text
    except Exception as e:
        return SConst.EMPTY_STRING



def detail_page(_driver):
    actor.close_popup(_driver)

    parse_basic_top(_driver)
    parse_basic_cast(_driver)

    actor.back_to_prev_page(_driver)

    return []


def parse_basic_top(_driver):
    name_container = _driver.find_element(By.CLASS_NAME, MConst.NAME_CLASS)
    p_name = get_text(name_container)

    plcae_container = _driver.find_element(By.XPATH, MConst.PLACE_XPATH)
    p_place = get_text(plcae_container)

    date_container = _driver.find_element(By.XPATH, MConst.DATE_XPATH)
    p_date = get_text(date_container)

    print(f'{p_name}  {p_place}  {p_date}')


def parse_basic_cast(_driver):
    # go to casting tab
    move_rst = actor.move_tab(_driver)

    if move_rst is False:
        return EMPTY

    # parse text
    text_rst = get_cast_text(_driver, CAST_INFO_TEXT_CLASS, GENERAL_WAIT_TIME)
    return text_rst

# def parse_basic_top()
# def parse_basic_cast()
# def parse_schedule()

# data_form = [
#     [musical, scheule, casting],
#     [musical, schedule, casting],
# ]



def crawl():
    cast_list = []

    _driver = driver.get_driver(False)
    _driver.get(TARGET_URL_MUSICAL)

    find_length = len(_driver.find_elements_by_class_name('prdImg'))
    list_count = 0

    while (list_count < find_length):
        find = _driver.find_elements_by_class_name('prdImg')
        find[list_count].click()

        cast = detail_page(_driver)
        print(cast)
        cast_list.append(cast)
        list_count = list_count + 1

    _driver.quit()


crawl()
