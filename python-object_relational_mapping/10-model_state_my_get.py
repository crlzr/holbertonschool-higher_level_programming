#!/usr/bin/python3
"""
Write a script that prints the State object with the name
passed as argument from the database hbtn_0e_6_usa"""

import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    for av in sys.argv:
        if av.count(";") > 0:
            exit()

        engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3]),
            pool_pre_ping=True
        )
        Session = sessionmaker(bind=engine)
        session = Session()

        state_name = sys.argv[4]

        query = session.query(State).filter(State.name == state_name).limit(1).first()

        if query:
            print(query.id)
        else:
            print("Not found")
