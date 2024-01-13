#!/usr/bin/python3
'''A script that lists all State objects from the database hbtn_0e_6_usa'''
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

from sys import argv

if __name__ == "__main__":
    engine = create_engine(f"mysql://{argv[1]}:{argv[2]}@\
localhost:3306/{argv[3]}")
    Session = sessionmaker(bind=engine)
    session = Session()
    res = session.query(State).all()
    for row in res:
        print(f"{row.id}: {row.name}")
    session.close()
