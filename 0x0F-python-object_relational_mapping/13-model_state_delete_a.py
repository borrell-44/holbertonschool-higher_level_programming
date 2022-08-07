#!/usr/bin/python3

"""Write a script that lists all State objects
from the database hbtn_0e_6_usa"""

from sys import argv
from model_state import Base, State
import sqlalchemy as db

if __name__ == "__main__":
    engine = db.create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                              argv[1], argv[2], argv[3]), pool_pre_ping=True)
    meta = db.MetaData(bind=engine)
    db.MetaData.reflect(meta)
    states = meta.tables["states"]

    delete = db.delete(states).where(states.columns.name.contains('a'))
    engine.execute(delete)
