import sqlalchemy as db


engine = db.create_engine('mysql+pymysql://root:JaVaDmZ84!@localhost:3306/orm_db1')

connection = engine.connect()
metadata = db.MetaData()


data = db.Table('person', metadata, autoload=True, autoload_with=engine)

# SELECT *
# query = db.select(data)

# SELECT with WHERE 
query = db.select(data).where(data.c.name=='Amir')

result = connection.execute(query)
for row in result:
    print(row)
