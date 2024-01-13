#!/usr/bin/python3
"""
A script that lists all State objects that contain the letter 'a'
from a database
"""
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

from sys import argv

if __name__ == "__main__":
    engine = create_engine(f"mysql://{argv[1]}:{argv[2]}@\
localhost:3306/{argv[3]}")
    Session = sessionmaker(bind=engine)
    session = Session()
    res = session.query(State).filter(State.name.like("%a%")).all()
    for row in res:
        print(f"{row.id}: {row.name}")
    session.close()
