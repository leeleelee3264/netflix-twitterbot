# 파싱을 할 때 버튼을 누르거나 하는 동작들의 모임
from selenium.common.exceptions import ElementNotInteractableException

from crawl.dynamic.policy.Const import _Musical, _Server
import crawl.dynamic.driver_util as util

MConst = _Musical()
SConst = _Server()

def close_popup(_driver):

    try:
        _driver.find_element_by_class_name('popupCloseBtn').click()
    except ElementNotInteractableException as e:
        pass

def move_tab(_driver):
    return util.move_tab(_driver, MConst.CAST_INFO_TAB_CLASS, SConst.WAIT_TIME, MConst.CAST_INFO_TAB_NAME)

def back_to_prev_page(_driver):
    _driver.back()
