#!/usr/bin/python3
"""Script to list all state object that contain the letter 'a'
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3]),
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    contain_a = session.query(State).filter(State.name.like('%a%')).all()
    for rows in contain_a:
        print("{0}: {1}".format(rows.id, rows.name))
