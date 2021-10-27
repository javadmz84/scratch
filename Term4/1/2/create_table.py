import pymysql

con = pymysql.connect(host='localhost', user='root', password='JaVaDmZ84!', database='register')


sql = 'CREATE TABLE person(idnum int auto_increment, fullname varchar(120) not null, phone varchar(11) not null, primary key(idnum))'


try:
    with con.cursor() as cur:
        cur.execute(sql)
except:
        print('Access denied!')
    