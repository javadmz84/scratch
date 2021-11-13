import sqlalchemy as db



def update():
    query = db.update(data).values(
        fullname=search_fullname.get(),
        phone=search_phone.get(),
        ).where(data.c.idnum==res[0])
    connection.execute(query)