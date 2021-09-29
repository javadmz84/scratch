import pymysql

con = pymysql.connect(host='localhost', user='root', password='JaVaDmZ84!', database='my_db_n')

sql = 'INSERT INTO user(name) VALUES (%s)'
data = 'Setayesh'


try:
    with con.cursor() as cur:
        cur.execute(sql, data)
        con.commit()
except:
    print('Access Denied')
