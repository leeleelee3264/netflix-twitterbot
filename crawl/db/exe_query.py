import datetime

import pymysql

from crawl import util
from crawl.db.connector import local_cnf
from crawl.dynamic.policy.Table import _MTable

db = local_cnf
cursor = local_cnf.cursor(pymysql.cursors.DictCursor)

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


# def close_db():
#     cursor.close()
#     db.close()
