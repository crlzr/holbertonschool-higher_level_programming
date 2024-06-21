#!/usr/bin/python3
"""
First class definition of City.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_city import State

Base = declarative_base()


class City(Base):
    """
    Class City that inherits from Base
    """
    __tablename__ = 'city'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(State.id), nullable=False) #nullable must be at the end
    