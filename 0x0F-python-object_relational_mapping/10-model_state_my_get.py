#!/usr/bin/python3

"""Write a script that lists all State objects
from the database hbtn_0e_6_usa"""

from sys import argv
from model_state import Base, State
import sqlalchemy as db

if __name__ == "__main__":
    engine = db.create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                              argv[1], argv[2], argv[3]), pool_pre_ping=True)
    st = State()
    bol = False
    meta = db.MetaData()
    con = engine.connect()

    census = db.Table('states', meta, autoload=True, autoload_with=engine)
    query = db.select([census])
    result = con.execute(query)
    sets = result.fetchall()
    for set in sets:
        if set[1] == argv[4]:
            print(set[0])
            bol = True
    if not bol:
        print("Not Found")
