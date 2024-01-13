#!/usr/bin/python3
"""
Module that contains the class definition of a City
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base

from sys import argv


class City(Base):
    """
    Represents a city in the database.

    Attributes:
        __tablename__ (str): The name of the database table.
        id (int): The primary key of the city record (auto-incremented).
        name (str): The name of the city (maximum 128 characters).
        state_id (int): The foreign key referencing the associated state's ID.
        state (State): The relationship to the associated state using
            the "State" class.
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
    state = relationship("State", foreign_keys="City.state_id")
