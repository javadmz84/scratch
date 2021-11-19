import sqlalchemy as db
from sqlalchemy.engine import result


def insert_person(fName, number):
    query = db.insert(person).values(fullname=fName.lower(), id_number=number)
    connection.execute(query)

def set_fligh(fcity, tcity, d, a, ag, s, p):
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

def passengers_list():
    query = db.select(person)
    result = connection.execute(query)
    for row in result:
        print(row)
        
engine = db.create_engine('mysql+pymysql://root:JaVaDmZ84!@localhost:3306/booking')

connection = engine.connect()
metadata = db.MetaData()


person = db.Table('person', metadata, autoload=True, autoload_with=engine)
flight = db.Table('flight', metadata, autoload=True, autoload_with=engine)
ticket = db.Table('ticket', metadata, autoload=True, autoload_with=engine)
