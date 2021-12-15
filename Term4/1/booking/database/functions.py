import sqlalchemy as db
from sqlalchemy.engine import result

def find_passenger(value):
    query = db.select(person).where(person.c.id == int(value))
    return connection.execute(query)

def find_flight(value):
    query = db.select(flight).where(flight.c.id ==int(value))
    return connection.execute(query)


def insert_person(fName, number):
    query = db.insert(person).values(fullname=fName.lower(), id_number=number)
    connection.execute(query)

def delete_person(person_id):
    query = db.delete(person).where(person.c.id == person_id)
    connection.execute(query)

def set_flight(fcity, tcity, d, a, ag, s, p):
    query = db.insert(flight).values(
        from_city=fcity,
        to_city=tcity,
        depretur=d,
        arrival=a,
        agency=ag,
        seats=s,
        price=p
    )
    connection.execute(query)

def bood_ticket(p_id, f_id):
    query = db.insert(ticket).values(person_id=p_id, flight_id=f_id)
    connection.execute(query)


def flight_list():
    query = db.select(flight)
    return connection.execute(query)

def flight_filter(value):
    query = db.select(flight).where(flight.c.id == int(value))

def update_person(fName, number, person_id):
    query = db.update(person).values(
        fullname=fName,
        id_number=number,
    ).where(person.c.id == person_id )
    connection.execute(query)

def update_flight(fcity, tcity, d, a, ag, s, p, flighy_id):
    query = db.update(flight).values(
        from_city=fcity,
        to_city=tcity,
        depretur=d,
        arrival=a,
        agency=ag,
        seats=s,
        price=p
    ).where(flight.c.id == id)
    connection.execute(query)
    
def update_ticket(p_id, f_id, ticket_id):
    query = db.update(person).values(
    person_id = p_id,
    flighy_id = f_id,
    ).where(ticket.c.id == ticket_id)
    connection.execute(query)

def passenger_list():
    query = db.select(person)
    return connection.execute(query)


def passenger_filter(value):
    txt = value+'%'
    query = db.select(person).where(person.c.id_number.like(txt))
    return connection.execute(query)

def delete_person(person_id):
    query = db.delete(person).where(person.c.id == person_id)
    connection.execute(query)

engine = db.create_engine('mysql+pymysql://root:JaVaDmZ84!@localhost:3306/booking')

connection = engine.connect()
metadata = db.MetaData()


person = db.Table('person', metadata, autoload=True, autoload_with=engine)
flight = db.Table('flight', metadata, autoload=True, autoload_with=engine)
ticket = db.Table('ticket', metadata, autoload=True, autoload_with=engine)
