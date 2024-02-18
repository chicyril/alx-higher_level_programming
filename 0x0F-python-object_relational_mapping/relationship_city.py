#!/usr/bin/python3
"""Contains class definition of City model."""
from sqlalchemy import Column, String, Integer, ForeignKey
from relationship_state import Base
from sqlalchemy.orm import relationship


class City(Base):
    """Class definition of City mapped to a cities table."""
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer,
                      ForeignKey('states.id'),
                      nullable=False)
    state = relationship("State", back_populates='cities')
