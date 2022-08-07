#!/usr/bin/python3

"""Prints all City objects from the given database"""

from sys import argv
from model_state import Base, State
import sqlalchemy as db

if __name__ == "__main__":
    engine = db.create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                              argv[1], argv[2], argv[3]), pool_pre_ping=True)
    meta = db.MetaData(bind=engine)
    db.MetaData.reflect(meta)
    state = meta.tables["states"]
    city = meta.tables["cities"]

    query = db.select([state.columns.name, city.columns.id,
                      city.columns.name]).where(city.columns.state_id == 
                      state.columns.id).order_by(city.columns.id.asc())
    rows = engine.execute(query).fetchall()

    for row in rows:
        print(row)
