#!/usr/bin/python3
'''A script that prints all City objects from a database'''
from sqlalchemy import create_engine
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker

from sys import argv

if __name__ == "__main__":
    engine = create_engine(f"mysql://{argv[1]}:{argv[2]}@\
localhost:3306/{argv[3]}")
    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(City, State)\
        .join(State, State.id == City.state_id).all()
    for cities, states in query:
        print(f"{states.name}: ({cities.id}) {cities.name}")
    session.close()
