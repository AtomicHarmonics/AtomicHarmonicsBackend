import sys

# for creating the mapper code
from sqlalchemy import Column, ForeignKey, Integer, String, Float, Boolean

# for configuration and class code
from sqlalchemy.ext.declarative import declarative_base

# for creating foreign key relationship between the tables
from sqlalchemy.orm import relationship

# for configuration
from sqlalchemy import create_engine

# create declarative_base instance
Base = declarative_base()

# we create the class Book and extend it from the Base Class.
class EffectsProfile(Base):
    __tablename__ = 'effectsProfile'

    #id = Column(Integer, primary_key=True)
    title = Column(String(250), primary_key=True, nullable=False)
    author = Column(String(250), nullable=False)
    effect1Name = Column(String(250), nullable=False)
    effect1Param1Name = Column(String(250), nullable=False)
    isSelected = Column(Boolean, nullable=False)


# creates a create_engine instance at the bottom of the file
engine = create_engine('sqlite:///profile-collection.db')

Base.metadata.create_all(engine)
