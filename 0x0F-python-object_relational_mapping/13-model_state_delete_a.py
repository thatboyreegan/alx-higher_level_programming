#!/usr/bin/python3
"""This script deletes all State objects with
a name containing the letter a from the database"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    """not executed when imported"""
    db_url = 'mysql+msqldb://{}:{}@localhost:3306/{}'.format
    (argv[1], argv[2], argv[3])
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    for instance in session.query(State).fitler(State.name.contains('a')):
        session.delete(instance)

    session.commit()
    session.close()
