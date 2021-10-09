from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from crawl.dynamic.policy.Const import _Server

CONST = _Server()

def wait_elemet(_driver, selector, limit_time, elemt_type, all_elements=False):
    try:
        if all_elements is True:
            return WebDriverWait(_driver, limit_time).until(
                EC.presence_of_all_elements_located((elemt_type, selector))
            )

        return WebDriverWait(_driver, limit_time).until(
            EC.presence_of_element_located((elemt_type, selector))
        )

    except Exception as e:
        print(e)
        return None


def move_tab(_driver, selector, limit_time, tab_name):

    try:
        tabs = wait_elemet(_driver, selector, limit_time, By.CLASS_NAME, True)

        castTab = get_target_tab_name(tabs, tab_name)
        tabs[castTab].click()
    except Exception as e:
        print(e)
        pass


def get_target_tab_name(elements, tab_name):
    if elements is None:
        return CONST.EMPTY_INT

    for i in range(len(elements)):
        if elements[i].text == tab_name:
            return i

    return CONST.EMPTY_INT


def get_text(elemet):

    try:
        if elemet.text == '해당없음':
            return CONST.NO_DATA_STR

        return elemet.text
    except Exception as e:
        print(e)
        return CONST.NO_DATA_STR
