# 셀레니움을 이용해서 다이나믹으로 웹을 조작해서 크롤링을 한다
import time
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

import driver

TARGET_URL_MUSICAL = "http://ticket.interpark.com/contents/Ranking/RankList?pKind=01011&pCate=&pType=M&pDate="

CAST_INFO_TAB_NAME = '부가정보'
CAST_INFO_TAB_CLASS = 'navLink'
CAST_INFO_TEXT_CLASS = 'moreInfoCast'

GENERAL_WAIT_TIME = 5

EMPTY = '정보없음'


def get_cast_tab_number(elements):
    for i in range(len(elements)):
        if elements[i].text == CAST_INFO_TAB_NAME:
            return i

    return -1


def move_to_cast_tab(_driver, selector, limit_time):
    tabs = wait_class_elements(_driver, selector, limit_time, True)

    if tabs is None:
        return False

    castTab = get_cast_tab_number(tabs)
    tabs[castTab].click()

    return True


def get_cast_text(_driver, selector, limit_time):
    text_container = wait_class_elements(_driver, selector, limit_time)

    if text_container is None:
        return EMPTY

    text_rst = text_container.text

    return set_default_cast_text(text_rst)


def set_default_cast_text(text):

    if text == '해당없음':
        return EMPTY
    return text


def wait_class_elements(_driver, selector, limit_time, all_elements=False):
    try:
        if all_elements is True:
            return WebDriverWait(_driver, limit_time).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, selector))
            )

        return WebDriverWait(_driver, limit_time).until(
            EC.presence_of_element_located((By.CLASS_NAME, selector))
        )

    except Exception as e:
        print(e)
        return None


def parse_casting(_driver):
    # 예매 알림 팝업 닫기
    try:
        _driver.find_element_by_class_name('popupCloseBtn').click()
    except ElementNotInteractableException as e:
        pass

    # go to casting tab
    move_rst = move_to_cast_tab(_driver, CAST_INFO_TAB_CLASS, GENERAL_WAIT_TIME)

    if move_rst is False:
        return EMPTY

    # parse text
    text_rst = get_cast_text(_driver, CAST_INFO_TEXT_CLASS, GENERAL_WAIT_TIME)

    _driver.back()
    return text_rst


def crawl():
    cast_list = []

    _driver = driver.get_driver()
    _driver.get(TARGET_URL_MUSICAL)

    find_length = len(_driver.find_elements_by_class_name('prdImg'))
    list_count = 0

    while (list_count < find_length):
        find = _driver.find_elements_by_class_name('prdImg')
        find[list_count].click()

        cast = parse_casting(_driver)
        print(cast)
        cast_list.append(cast)
        list_count = list_count + 1

    _driver.quit()

crawl()
