#!/usr/bin/python3
""" Dog Module for HappyPup project """
from models.basemodel import BaseModel, Base
from sqlalchemy import Table, Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv
import models


class Dog(BaseModel, Base):
    """ A class that defines the pets, dogs"""
    __tablename__ = "dogs"
    if getenv('TYPE_STORAGE') == 'db':
        owner_id = Column(String(60), ForeignKey("owners.id"), nullable=False)
        name = Column(String(128), nullable=False)
        sex = Column(String(20), nullable=True)
        age = Column(Integer, default=0, nullable=False)
        breed = Column(String(128), nullable=False)

    else:
        owner_id = ""
        name = ""
        sex = ""
        age = 0
        breed = ""
