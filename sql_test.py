#!/usr/bin/env python
"""
Simple script to play around with SQLAlchemy
"""
from sqlalchemy import create_engine
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.ext.declarative import declarative_base

# Create the DB connection
engine = create_engine('mysql+mysqlconnector://root@localhost/star_trek')

# Create the declarative base class
Base = declarative_base()

# Define the captain table
class Captain(Base):
    __tablename__ = 'captain'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(50))
    last_name = Column(String(50))

    def __repr__(self):
        return "<Captain(name='{} {}')>".format(first_name, last_name)
