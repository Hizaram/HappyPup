#!/usr/bin/python3
""" Medical centres module for HappyPup project """
from models.basemodel import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv
import models


class Medical_Centres(BaseModel, Base):
    """ A class for the medical centres """
    __tablename__ = "medical_centres"
    if getenv('TYPE_STORAGE') == 'db':
        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        address = Column(String(1024), nullable=False)

        city = relationship("City", backref="medical_centres",
                            cascade="all, delete")
        state = relationship("State", backref="medical_centres",
                             cascade="all, delete")

    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        address = ""
