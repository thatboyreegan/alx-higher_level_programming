#!/usr/bin/python3
"""This script creates the state
california with the city san francisco form the database"""
from sys import argv
from model_state import Base, State
from model_state import City
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

    state = State(name='California')
    s_city = City(name='San Francisco')

    state.cities.append(s_city)

    session.add(state)

    session.commit()
    session.close()
