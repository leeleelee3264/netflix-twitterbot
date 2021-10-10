# 이제 여기서 일정과 케스팅일 파싱한다
from selenium.webdriver.common.by import By

from crawl.db.exe_query import get_musical, insert_schedules, insert_castings
from crawl.db.model.schedule import Schedule
from crawl.dynamic import driver
from crawl.dynamic.musical import actor
from crawl.dynamic.policy.Const import _Musical, _Server
import crawl.dynamic.driver_util as util
from crawl.regex import get_last_index_of_digit

MConst = _Musical()
SConst = _Server()


class MusicalMetaInfo:
    def __init__(self, id, path):
        self.__id = id
        self.__path = path

    @property
    def id(self):
        return self.__id

    @property
    def path(self):
        return self.__path


def go_to_detail_page(_driver, meta_info:MusicalMetaInfo):
    actor.close_popup(_driver)
    actor.move_tab(_driver, MConst.SCHEDULE_INFO_TAB_NAME)
    rst = parse_schedule(_driver, meta_info)
    return rst


def parse_schedule(_driver, meta_info:MusicalMetaInfo):
    rst = []
    table_container = util.wait_elemet(_driver, MConst.SCHEDULE_TABLE_XPATH, SConst.WAIT_TIME, By.XPATH, True)

    try:
        for i in range(1, len(table_container)):
            t_table = util.get_text(table_container[i])
            schedule = Schedule(meta_info.id, t_table)
            rst.append(schedule)

    except Exception as e:
        print(e)

    return rst


#   def parse_cast()

def crawl():
    targets = get_target_musical()

    _driver = driver.get_driver(headless=True)

    for target in targets:
        _driver.get(target.path)
        rst = go_to_detail_page(_driver, target)

        insert_parsed_infos(rst)
    _driver.quit()


def insert_parsed_infos(scedules):
    s_param = []
    c_param = []

    for scedule in scedules:
        s_param.append((
            scedule.musical_id,
            scedule.date,
            scedule.time
        ))

        c_param.append((
            scedule.musical_id,
            scedule.date,
            scedule.time,
            scedule.cast.cast
        ))

    insert_schedules(s_param)
    insert_castings(c_param)


def get_target_musical():

    targets = get_musical()
    rst = []

    for target in targets:
        try:
            t_id = target['id']
            t_path = target['interpark_path']

            tMusical_path = MusicalMetaInfo(t_id, t_path)
            rst.append(tMusical_path)
        except Exception as e:
            print(e)

    return rst


if __name__ == "__main__":
    crawl()