# 셀레니움을 이용해서 다이나믹으로 웹을 조작해서 크롤링을 한다
import time
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

import driver

TARGET_URL_MUSICAL = "http://ticket.interpark.com/contents/Ranking/RankList?pKind=01011&pCate=&pType=M&pDate="
CAST_INFO_NAME = '부가정보'
CAST_INFO_TAB_CLASS = 'navLink'
CAST_INFO_TEXT_CLASS = 'moreInfoCast'
GENERAL_WAIT_TIME = 5


def get_cast_tab_number(elements):

    for i in range(len(elements)):
        if elements[i].text == CAST_INFO_NAME:
            return i

    return -1


def parse_casting(_driver):
    # 예매 알림 팝업 닫기
    try:
        _driver.find_element_by_class_name('popupCloseBtn').click()
    except ElementNotInteractableException as e:
        pass


    # cast parse
    try:
        tabs = WebDriverWait(_driver, GENERAL_WAIT_TIME).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, CAST_INFO_TAB_CLASS))
        )

        castTab = get_cast_tab_number(tabs)

        tabs[castTab].click()
    except Exception as e:
        print(e)
        return ''

    try:
        text_container = WebDriverWait(_driver, GENERAL_WAIT_TIME).until(
            EC.presence_of_element_located((By.CLASS_NAME, CAST_INFO_TEXT_CLASS))
        )

        return text_container.text
    except Exception as e:
        print(e)
        return ''
    finally:
        _driver.back()


# 셀레니움으로 페이지 이동 했다가 다시 오고 그러면 이미 새로 랜더링이 되어서
# 예전의 엘리먼트가 없다고 에러가 났는데 이렇게 해결을 할 수 있었다.
# 그냥 페이지는 새로 고쳐버리고 몇번째까지 읽었나를 기억하면 그만이었네..
# https://stackoverflow.com/questions/58717379/how-to-do-loop-with-click-in-selenium
def crawl():
    cast_list = []

    _driver = driver.get_driver()
    _driver.get(TARGET_URL_MUSICAL)

    find_length = len(_driver.find_elements_by_class_name('prdImg'))
    list_count = 0

    while(list_count < find_length):

        find = _driver.find_elements_by_class_name('prdImg')
        find[list_count].click()

        cast = parse_casting(_driver)
        print(cast)
        cast_list.append(cast)
        list_count = list_count + 1


crawl()
