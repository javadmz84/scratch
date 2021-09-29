import pymysql

con = pymysql.connect(host='localhost', user='root', password='JaVaDmZ84!', database='product')


sql = 'CREATE TABLE TV(id int auto_increment, name varchar(255), primary key(id))'


try:
    with con.cursor() as cur:
        cur.execute(sql)
except:
        print('Access denied!')
    