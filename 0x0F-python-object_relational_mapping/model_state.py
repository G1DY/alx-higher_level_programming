#!/usr/bin/python3
"""Defines a State and a Base class to work with
   MySQLAlchemy ORM
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Class state

    Attributes:
        __tablename__(str): the table name of the class
        id(int): id of the class
        name(str): state name of the class
    """
    __tablename__ = "states"

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
