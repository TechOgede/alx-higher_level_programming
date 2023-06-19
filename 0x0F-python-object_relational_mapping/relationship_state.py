#!/usr/bin/python3
''' This module contains the class definition
of 'State' and an instance of 'declarative_base()' '''


from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class State(Base):
    ''' This class is a mapping of the states table '''
    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    name = Column(String(length=128), nullable=False)
    cities = relationship("City", backref="state")
