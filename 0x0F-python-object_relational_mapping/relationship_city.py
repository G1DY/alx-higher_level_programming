#!/usr/bin/python3
"""Defines a City class to work with
   MySQLAlchemy ORM
"""
from relationship_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """Class city

    Attributes:
        __tablename__(str): the table name of the class
        id(int): id of the class
        name(str): name of the city
        state_id(int): id of the state the city belongs
    """
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('state.id'), nullable=False)
