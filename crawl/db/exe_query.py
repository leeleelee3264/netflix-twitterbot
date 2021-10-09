import pymysql

from crawl.db.connector import local_cnf

db = local_cnf
cursor = local_cnf.cursor(pymysql.cursors.DictCursor)

# 하나씩
def exe_insert(query):
    cursor.execute(query)
    db.commit()

# 여러개
def exe_insert_many(query, data_list):
    cursor.executemany(query, data_list)
    db.commit()