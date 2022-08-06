#!/usr/bin/python3

"""Write a python file that contains the class definition of
a State and an instance Base = declarative_base()"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects import mysql

Base = declarative_base()


class State(Base):
   """State class inherits from Base
    Links to MySQL table 'states'
    Attributes:
        id: column of auto-generated unique integer, can't be NULL, primary key
        name: column of string with max 128 characters, can't be NULL
    """

    __tablename__ = "states"
    id = Column(Integer, unique=True, autoincrement=True,
                nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
