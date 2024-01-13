#!/usr/bin/python3
"""
A script that prints the State object with the name passed as argument.
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
    state_name = argv[4]
    res = session.query(State).filter(State.name.like(state_name)).first()
    if res:
        print(f"{res.id}")
    else:
        print("Not found")
    session.close()
