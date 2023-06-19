#!/usr/bin/python3
''' This module contains the class definition
of 'City' and an instance of 'declarative_base()' '''


from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base


class City(Base):
    ''' This class is a mapping of the states table '''
    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    name = Column(String(length=128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
