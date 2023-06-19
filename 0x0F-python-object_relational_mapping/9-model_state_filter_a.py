#!/usr/bin/python3
"""This script  lists all State
objects that contain the letter a from the database"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    """Lists all state objects that start with an a"""
    db_url = 'mysql+msqldb://{}:{}@localhost:3306/{}'.format
    (argv[1], argv[2], argv[3])
    engine = create_engine(db_url)

    Session = sessionmaker(bind=engine)
    session = Session()

    for instance in session.query(State).fitler(State.name.contains('a')):
        print('{0}: {1}'.format(instance.id, instance.name))

    session.close()
