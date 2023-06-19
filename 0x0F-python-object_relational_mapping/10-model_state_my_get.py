#!/usr/bin/python3
"""This script prints the State
object with the name passed as argument from the database """
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    """only print the onject name whose name matches the provided name."""
    db_url = 'mysql+msqldb://{}:{}@localhost:3306/{}'.format
    (argv[1], argv[2], argv[3])
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    instance = session.query(State).filter(State.name == argv[4]).first()

    if instance is None:
        print('Not found')
    else:
        print('{0}'.format(instance.id))

    session.close()
