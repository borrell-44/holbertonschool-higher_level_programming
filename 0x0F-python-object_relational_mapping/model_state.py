#!/usr/bin/python3

"""Write a python file that contains the class definition of
a State and an instance Base = declarative_base()"""

import MySQLdb
from sqlalchemy import Column, Integer, String, Identity
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    "Links to the MySQL table states"

    __tablename__ = "states"
    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    db = MySQLdb.connect(db="hbtn_0e_4_usa", user="root", passwd="root",
                         port=3306)
