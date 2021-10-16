import sqlalchemy as db


engine = db.create_engine('mysql+pymysql://root:JaVaDmZ84!@localhost:3306/orm_db1')

connection = engine.connect()
metadata = db.MetaData()

data = db.Table('person', metadata, autoload=True, autoload_with=engine)

query = db.insert(data).values(name='Setayesh', last_name='Setayesh')
ResultProxy = connection.execute(query)