from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from crawl.dynamic.policy.Const import _Server

CONST = _Server()

def wait_class_elements(_driver, selector, limit_time, all_elements=False):
    try:
        if all_elements is True:
            return WebDriverWait(_driver, limit_time).until(
                EC.presence_of_all_elements_located((By
                                                     .CLASS_NAME, selector))
            )

        return WebDriverWait(_driver, limit_time).until(
            EC.presence_of_element_located((By.CLASS_NAME, selector))
        )

    except Exception as e:
        print(e)
        return


def move_tab(_driver, selector, limit_time, tab_name):
    tabs = wait_class_elements(_driver, selector, limit_time, True)

    if tabs is None:
        return False

    castTab = get_target_tab_name(tabs, tab_name)
    tabs[castTab].click()

    return True


def get_target_tab_name(elements, tab_name):
    for i in range(len(elements)):
        if elements[i].text == tab_name:
            return i

    return CONST.EMPTY_INT