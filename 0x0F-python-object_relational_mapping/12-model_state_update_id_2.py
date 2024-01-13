#!/usr/bin/python3
'''A script that changes the name of a State object from a database'''
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

from sys import argv

if __name__ == "__main__":
    engine = create_engine(f"mysql://{argv[1]}:{argv[2]}@\
localhost:3306/{argv[3]}")
    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(State).filter(State.id == 2).first()
    query.name = "New Mexico"
    session.commit()
    session.close()
