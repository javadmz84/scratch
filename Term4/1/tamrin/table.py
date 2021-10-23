import pymysql

con = pymysql.connect(host='localhost', user='root', password='JaVaDmZ84!', database='Identity')


sql = 'CREATE TABLE person(id int auto_increment, full_name varchar(120) not null, phone varchar(11) not null, primary key(id))'


try:
    with con.cursor() as cur:
        cur.execute(sql)
except:
        print('Access denied!')
    