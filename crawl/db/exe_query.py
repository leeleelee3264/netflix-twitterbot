import datetime

import pymysql

from crawl import util
from crawl.db.connector import get_connector
from crawl.dynamic.policy.Table import _MTable

db = get_connector()
cursor = db.cursor(pymysql.cursors.DictCursor)

TABLE = _MTable()

# 하나씩
def insert_common(query):
    try:
        cursor.execute(query)
        db.commit()
    except Exception as e:
        print(e)
    # finally:
    #     close_db()


def insert_schedules(schedules):
    sql = "insert into schedule(musical_id, date, time)" + \
        "values(%s, %s, %s)"

    try:
        cursor.executemany(sql, schedules)
        db.commit()
    except Exception as e:
        print(e)
    # finally:
    #     close_db()

def insert_castings(castings):
    sql = "insert into casting(musical_id, date, time, cast)" + \
            "values(%s, %s, %s, %s)"

    try:
        cursor.executemany(sql, castings)
        db.commit()
    except Exception as e:
        print(e)
    # finally:
    #     close_db()


def get_musical():

    today = util._get_date(datetime.datetime.now())

    query = "SELECT id, interpark_path" + \
            " FROM " + TABLE.MUSICAL + \
            " WHERE end_date >= " + today

    rst = []

    try:
        cursor.execute(query)
        rst = cursor.fetchall()

    except Exception as e:
        print(e)
    # finally:
    #     close_db()

    return rst


def get_schedule_for_twitter():
    today_cast = util._get_date(datetime.datetime.now())

    query = " SELECT c.time, c.cast, m.name, m.place, m.poster_path " + \
            " FROM " + TABLE.CASTING + " c" + \
            " INNER JOIN " + TABLE.MUSICAL + " m ON m.id = c.musical_id" + \
            " WHERE c.date = " + today_cast
    try:
        cursor.execute(query)
        rst = cursor.fetchall()

        return rst
    except Exception as e:
        print(e)
        return {}

