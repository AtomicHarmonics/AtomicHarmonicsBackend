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

BaseBypass = declarative_base()

# we create the class Book and extend it from the Base Class.
class EffectsProfile(Base):
    __tablename__ = 'effectsProfile'

    #id = Column(Integer, primary_key=True)
    title = Column(String(250), primary_key=True, nullable=False)
    author = Column(String(250), nullable=False)
    
    tremoloFreq = Column(Float, nullable=False)
    tremoloDepth = Column(Integer, nullable=False)
    tremoloEnabled = Column(Boolean, nullable=False)
    tremoloOrderNumber = Column(Integer, nullable=False)
    
    overDriveThresh = Column(Float, nullable=False)
    overDriveEnabled = Column(Boolean, nullable=False)
    overDriveOrderNumber = Column(Integer, nullable=False)
    
    distortThresh = Column(Float, nullable=False)
    distortEnabled = Column(Boolean, nullable=False)
    distortOrderNumber = Column(Integer, nullable=False)
    
    reverbWetLevel = Column(Float, nullable=False)
    reverbRoomSize = Column(Float, nullable=False)
    reverbDryLevel = Column(Float, nullable=False)
    reverbDampLevel = Column(Float, nullable=False) 
    reverbWidth = Column(Float, nullable=False)
    reverbMode = Column(Float, nullable=False)
    reverbEnabled = Column(Boolean, nullable=False)
    reverbOrderNumber = Column(Integer, nullable=False)
    
    preAmpEnabled = Column(Boolean, nullable=False)
    preAmpGain = Column(Float, nullable=False)

    bitcrusherDownSample = Column(Integer, nullable=False)
    bitcrusherEnabled = Column(Boolean, nullable=False)
    bitcrusherOrderNumber = Column(Integer, nullable=False)

    isSelected = Column(Boolean, nullable=False)


class BypassProfile(BaseBypass):
    __tablename__ = 'bypassProfile'

    #id = Column(Integer, primary_key=True)
    bypassEnabled = Column(Boolean, primary_key=True, nullable=False)


# creates a create_engine instance at the bottom of the file
engine = create_engine('sqlite:///profile-collection.db')

Base.metadata.create_all(engine)

# creates a create_engine instance at the bottom of the file
engine_bypass = create_engine('sqlite:///bypass-collection.db')

BaseBypass.metadata.create_all(engine_bypass)
