#!/usr/bin/python3
'''
A script that lists all State objects, and corresponding City objects,
contained in a databas
'''
from sqlalchemy import create_engine
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm import sessionmaker

from sys import argv

if __name__ == "__main__":
    engine = create_engine(f"mysql://{argv[1]}:{argv[2]}@\
localhost:3306/{argv[3]}")
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(State).outerjoin(City)\
        .order_by(State.id, City.id).all()
    for states in query:
        print(f"{states.id}: {states.name}")
        for city in states.cities:
            print(f"    {city.id}: {city.name}")
    session.close()
