# 진짜 파싱을 하는 코드


from selenium.webdriver.common.by import By

import actor as actor
from crawl.db.exe_query import *
from crawl.db.model.musical import Musical
from crawl.dynamic import driver
from crawl.dynamic.driver_util import get_text, wait_elemet
from crawl.dynamic.policy.Const import _Musical, _Server

MConst = _Musical()
SConst = _Server()



def go_to_detail_page(_driver):
    actor.close_popup(_driver)

    src = parse_detail(_driver)
    actor.back_to_prev_page(_driver)

    return src


def parse_detail(_driver):

    src = parse_basic_top(_driver)
    full_src = parse_info_tab(_driver, src)

    return full_src


def parse_basic_top(_driver):
    poster_container = _driver.find_element(By.XPATH, MConst.POSTER_XPATH)
    p_poster_path = poster_container.get_attribute('src')

    name_container = _driver.find_element(By.CLASS_NAME, MConst.NAME_CLASS)
    p_name = get_text(name_container)

    date_container = _driver.find_element(By.XPATH, MConst.DATE_XPATH)
    p_date = get_text(date_container)

    p_current_url = _driver.current_url

    tMusical = Musical(p_name, p_poster_path, p_date, p_current_url)

    return tMusical



# target처럼 class나 type을 미리 표시해두는 걸 typing이라고 한다.
# hint는 sql에서 나오는 용어였음
def parse_info_tab(_driver, src:Musical):
    # go to casting tab
    actor.move_tab(_driver, MConst.CAST_INFO_TAB_NAME)

    cast_container = wait_elemet(_driver, MConst.CAST_INFO_TEXT_CLASS, SConst.WAIT_TIME, By.CLASS_NAME)
    p_cast = get_text(cast_container)

    place_container = wait_elemet(_driver, MConst.PLACE_XPATH, SConst.WAIT_TIME, By.XPATH)
    p_place = get_text(place_container)

    src.fetch_in_info_tab(p_cast, p_place)
    return src


def insert_main_info(src:Musical):
    if src is not None:
        query_for_musical = src.get_insert_query()
        insert_common(query_for_musical)


def crawl():

    _driver = driver.get_driver(headless=True)
    _driver.get(MConst.MUSICAL_URL)

    find_length = len(_driver.find_elements_by_class_name('prdImg'))
    list_count = 0

    while (list_count < find_length):
        find = _driver.find_elements_by_class_name('prdImg')
        find[list_count].click()

        cast = go_to_detail_page(_driver)
        insert_main_info(cast)

        list_count = list_count + 1

    _driver.quit()


if __name__ == "__main__":
    crawl()
