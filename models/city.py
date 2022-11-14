#!/usr/bin/python3
""" City Module for HappyPup project """
import models
from models.basemodel import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    # initialize class for file or DB storage

    __tablename__ = 'cities'
    if getenv('TYPE_STORAGE') == "db":
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        medical_centres = relationship('Medical_Centres',
                                       cascade='all, delete',
                                       backref='cities')

    else:
        name = ""
        state_id = ""
