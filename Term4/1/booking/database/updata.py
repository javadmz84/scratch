import sqlalchemy as db


engine = db.create_engine('mysql+pymysql://root:JaVaDmZ84!@localhost:3306/booking')

connection = engine.connect()
metadata = db.MetaData()


data = db.Table('person', metadata, autoload=True, autoload_with=engine)
query = db.update(data).values(fullname='taha momenzadeh').where(data.c.id==1)
ResultProxy = connection.execute(query)