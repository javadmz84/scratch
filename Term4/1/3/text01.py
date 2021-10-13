import sqlalchemy as db


engine = db.create_engine('mysql+pymysql://root:JaVaDmZ84!@localhost:3306/orm_db1')

connection = engine.connect()
metadata = db.MetaData()

emp = db.Table(
    'person',
    metadata,
    db.Column('id', db.Integer, autoincrement=True, primary_key=True),
    db.Column('name', db.String(255), nullable=False),
    db.Column('last_name', db.String(255), nullable=False)
)
metadata.create_all(engine)