import pymysql

con = pymysql.connect(host='localhost', user='root' , password='JaVaDmZ84!')


try:
    with con.cursor() as cur:
        cur.execute('CREATE DATABASE contacts')
except:
    print('Access denied')

