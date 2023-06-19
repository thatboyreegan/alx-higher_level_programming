#!/usr/bin/python3
"""Module that contains the class definition of a City"""
from model_state import Base, State
from sqlalchemy import Column, String, Integer, ForeignKey


class City(Base):
    """The class cities"""
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id') nullable=False)
