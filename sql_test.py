#!/usr/bin/env python
"""
Simple script to play around with SQLAlchemy
"""
from sqlalchemy import create_engine
from sqlalchemy import Column
from sqlalchemy import Float 
from sqlalchemy import ForeignKey 
from sqlalchemy import Integer
from sqlalchemy import JSON 
from sqlalchemy import String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create the DB connection
engine = create_engine('mysql+mysqlconnector://root:password@localhost/star_trek')
Session = sessionmaker(bind=engine)
session = Session()

# Create the declarative base class
Base = declarative_base()

# Define the captain table
class Captain(Base):
    __tablename__ = 'captain'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    meta = Column(JSON())

    def __repr__(self):
        return "<Captain(name='{} {}')>".format(self.first_name, self.last_name)

class Ship(Base):
    __tablename__ = 'ship'

    id = Column(Integer, primary_key=True)
    captain_fk = Column(Integer(), ForeignKey('captain.id'))
    name = Column(String(50))
    reg_number = Column(String(20))
    max_warp_speed = Column(Float(), default=1)

    def __repr__(self):
        return "<Ship(name='{}')>".format(self.name)
