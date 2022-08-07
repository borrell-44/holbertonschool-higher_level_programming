#!/usr/bin/python3

"""Write a Python file similar to model_state.py named 
model_city.py that contains the class definition of a 
City."""

from sqlalchemy import Column, Integer, String
from model_state import Base


class City(Base):
    "Links to the MySQL table states"

    __tablename__ = "cities"
    id = Column(Integer, unique=True, autoincrement=True,
                nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, nullable=False, foreign_keys="states.id")
