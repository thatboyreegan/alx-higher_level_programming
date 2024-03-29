#!/usr/bin/python3
"""This script lists all State objects,
and corresponding City objects, contained in the database """
from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    """Not executed when imported"""
    db_url = 'mysql+msqldb://{}:{}@localhost:3306/{}'.format
    (argv[1], argv[2], argv[3])
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).outerjoin(City).order_by
    (State.id, city.id).all()

    for state in states:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("\t{}: {}".format(city.id, city.name))

    session.close()
