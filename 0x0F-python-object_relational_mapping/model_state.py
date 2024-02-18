#!/usr/bin/python3
"""Contains a class definition of State and a declarative base model Base.
"""
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base
Base = declarative_base()


class State(Base):
    """Defines a State class mapped to a state table."""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
