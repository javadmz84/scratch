import sqlalchemy as db

engine = db.create_engine('mysql+pymysql://root:JaVaDmZ84!@localhost:3306/booking')

connection = engine.connect()
metadata = db.MetaData()

person = db.Table(
    "person",
    metadata,
    db.Column("id", db.Integer, autoincrement=True, primary_key=True),
    db.Column("fullname", db.String(120), nullable=False),
    db.Column("id_number", db.String(10), nullable=False, unique=True)
)

flight = db.Table(
    'flight',
    metadata,
    db.Column("id", db.Integer, autoincrement=True, primary_key=True),
    db.Column('from_city', db.String(120), nullable=False),
    db.Column('to_city', db.String(120), nullable=False),
    db.Column('depretur', db.DateTime(), nullable=False),
    db.Column('arrival', db.DateTime(), nullable=False),
    db.Column('agency', db.String(120), nullable=False),
    db.Column('seats', db.Integer(), nullable=False),
    db.Column('price', db.Integer(), nullable=False),
)

ticket = db.Table(
    'ticket',
    metadata,
    db.Column('id', db.Integer, autoincrement=True, primary_key=True),
    db.Column('person_id', db.Integer(), db.ForeignKey(person.c.id), nullable=False, ),
    db.Column('flight_id', db.Integer(), db.ForeignKey(flight.c.id), nullable=False, )
)
metadata.create_all(engine)