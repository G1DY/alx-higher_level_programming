#!/usr/bin/python3
"""a script that creates the State “California”
   with the City “San Francisco” from the database
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    for instance in session.query(State).order_by(State.id):
        if instance.cities:
            print(instance.id, instance.name, sep=": ")
            city_info = {}
            for city in instance.cities:
                city_info[city.id] = city.name
            for city_id, city_name in city_info.items():
                print("    {}: {}".format(city_id, city_name))
