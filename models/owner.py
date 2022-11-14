#!/usr/bin/python3
"""This module defines a class Owner"""
from models.basemodel import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class Owner(BaseModel, Base):
    """This class defines a dog owner by various attributes"""
    __tablename__ = "owners"
    if getenv('TYPE_STORAGE') == 'db':
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        phone_number = Column(String(20), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)

        dog = relationship("Dog", backref="owner", cascade="all, delete")

    else:
        email = ""
        password = ""
        phone_number = ""
        first_name = ""
        last_name = ""
