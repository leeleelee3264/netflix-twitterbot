# 파싱을 할 때 버튼을 누르거나 하는 동작들의 모임
import time

from selenium.common.exceptions import ElementNotInteractableException

from crawl.dynamic.policy.Const import _Musical, _Server
import crawl.dynamic.driver_util as util

MConst = _Musical()
SConst = _Server()

def close_popup(_driver):

    try:
        time.sleep(SConst.WAIT_TIME)
        _driver.find_element_by_class_name('popupCloseBtn').click()
    except Exception as e:
        pass

def move_tab(_driver, tab_name):
    return util.move_tab(_driver, MConst.TAB_CLASS, SConst.WAIT_TIME, tab_name)

def back_to_prev_page(_driver):
    _driver.back()
