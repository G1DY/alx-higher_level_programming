#!/usr/bin/python3
"""Start link class to table in database and
   lists all state objects from the database
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


if __name__ == "__main__":
    db_uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(db_uri)
    Session = sessionmaker(bind=engine)

    session = Session()
    instance = session.query(State).filter(State.name == sys.argv[4]).first()

    if instance is None:
        print("Not found")
    else:
        print("{0}".format(instance.id))
