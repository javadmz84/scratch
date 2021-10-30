import sqlalchemy as db

engine = db.create_engine('mysql+pymysql://root:JaVaDmZ84!@localhost:3306/orm_db')

connection = engine.connect()
metadata = db.MetaData()

emp = db.Table(
    "person",
    metadata,
    db.Column("id", db.Integer, autoincrement=True, primary_key=True),
    db.Column("fullname", db.String(120), nullable=False),
    db.Column("id_number", db.String(10), nullable=False, unique=True)
)
#flight = db.Table(
#    "flight"
#    metadata,
#    db.Column("id", db.Integer, autoincrement=True, primary_key=True),

#)

#metadata.create_all(engine)