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
        fname = Column(String(128), nullable=False)
        lname = Column(String(128), nullable=False)
        phone = Column(String(20), nullable=False)
        email = Column(String(128), nullable=True)
        password = Column(String(128), nullable=True)

        dog = relationship("Dog", backref="owner", cascade="all, delete")

    else:
        fname = ""
        lname = ""
        phone = ""
        email = ""
        password = ""
