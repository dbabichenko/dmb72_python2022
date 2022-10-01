import pymysql.cursors
import pandas as pd
import datetime
import uuid
import numpy as np
from itertools import combinations


#db_connection = sql.connect(host='localhost', database='benedict', user='root', password='artema2')
# Connect to the database
con = pymysql.connect(host='67.205.163.33',
                             user='bankUser',
                             password='bankUser123',
                             db='bank',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)


try:
    with con.cursor() as cur:
        cur.execute('SELECT * FROM books')
        rows = cur.fetchall()
        for row in rows:
            print(row['book_id'], row['first_name'], row['last_name'])
finally:
    con.close()
