#!/usr/bin/python3

"""Write a python file that contains the class definition of
a State and an instance Base = declarative_base()"""

from sqlalchemy import Column, Integer, String, Identity
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects import mysql

Base = declarative_base()


class State(Base):
    "Links to the MySQL table states"

    __tablename__ = "states"
    id = Column(mysql.Integer(11), unique=True, autoincrement=True,
                nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
