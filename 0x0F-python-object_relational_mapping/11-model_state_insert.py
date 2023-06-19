#!/usr/bin/python3
"""This script adds the State object “Louisiana” to the database"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    """Access the db and adds the state object louisiana"""
    db_url = 'mysql+msqldb://{}:{}@localhost:3306/{}'.format
    (argv[1], argv[2], argv[3])
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    louisiana_s = State(name='louisiana')
    session.add(louisiana_s)
    session.commit()

    print('{0}'.format(louisiana_s.id))
    session.close()
