#!/usr/bin/python3
"""Script for listing all states
that contain 'a'
from given database via SQLAlchemy"""

from sqlalchemy.orm.session import Session


if __name__ == "__main__":

    import sys
    from sqlalchemy import (create_engine)
    from model_state import Base, State
    from sqlalchemy.orm import sessionmaker

    argv = sys.argv
    u_name = argv[1]
    passwd = argv[2]
    db_name = argv[3]

    engine = create_engine("""mysql+mysqldb://{}:{}@localhost/{}"""
                           .format(u_name, passwd, db_name))
    # creating connection to database engine
    Base.metadata.create_all(engine)  # create metadata
    Session = sessionmaker(bind=engine)  # instance for engine
    session = Session()  # initializing
    querying = session.query(State).filter(State.name == argv[4])\
        .first()  # creating query
    if querying is None:
        print("Not found")
    if querying:
        print("{}".format(querying.id))
