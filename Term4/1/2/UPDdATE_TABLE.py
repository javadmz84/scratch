import pymysql

con = pymysql.connect(host='localhost', user='root', password='JaVaDmZ84!', database='my_db_n')

sql = "UPDATE user set name='Amir' where id= 1"

try:
    with con.