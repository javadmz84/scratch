import pymysql

con = pymysql.connect(host='localhost', user='root', password='JaVaDmZ84!', database='my_db_n')

sql = ' SELECT * FROM user'



try:
    with con.cursor() as cur:
        cur.execute(sql)
        print(cur.fetchall())
except:
    print ('Access Dinied')