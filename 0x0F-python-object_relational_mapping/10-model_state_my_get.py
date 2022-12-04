#!/usr/bin/python3
"""prints state id if state name is passed
"""
import sys
from model_state import Base, State

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1],
                                  sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    args = sys.argv[4]
    for state in session.query(State).order_by(State.id):
        if args == state.name:
            print("{}".format(state.id))
            exit()
    print("Not found")
    session.close()
