import pymysql

con = pymysql.connect(host='localhost', user='root', password='JaVaDmZ84!', database='my_db_n')

sql = "DELETE FROM user WHERE id=1"

try:
    with con.cursor() as cur:
        cur.execute(sql)
        con.commit()
except:
    print('Access Denied')