#!/usr/bin/python3
'''A script that lists all City objects from a database'''
from sqlalchemy import create_engine
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text

from sys import argv

if __name__ == "__main__":
    engine = create_engine(f"mysql://{argv[1]}:{argv[2]}@\
localhost:3306/{argv[3]}")
    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(City, State).join(State).all()
    for cities, states in query:
        print(f"{cities.id}: {cities.name} -> {states.name}")
    session.close()
