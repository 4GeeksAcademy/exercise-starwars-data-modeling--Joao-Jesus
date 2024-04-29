import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er


Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)


class Character(Base):
    __tablename__ = 'character'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False )
    gender = Column(String(250), nullable=False)
    heigth = Column(String(250), nullable=False)
    eyecolor = Column(String(250), nullable=False)
    user_id= Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

class Planet(Base):
    __tablename__ = 'planet'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    terrain = Column(String(250))
    population = Column(Integer)
    diameter = Column(Integer)
    rotation = Column(Integer)
    gravity = Column(Integer)
    user_id= Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

class Vehicle(Base):
    __tablename__ = 'vehicle'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    crew = Column(Integer)
    speed = Column(Integer)
    vehicle_class = Column(String(250))
    user_id= Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    def to_dict(self):
        return {
            
        }

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
