#!/usr/bin/python3
"""This script  changes the name of a State object from the database"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    """the State object is changed to New Mexico"""
    db_url = 'mysql+msqldb://{}:{}@localhost:3306/{}'.format
    (argv[1], argv[2], argv[3])
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    new_mexico = session.query(State).filter(State.id == '2').first()
    new_mexico.name = 'New Mexico'
    session.commit()

    session.close()
