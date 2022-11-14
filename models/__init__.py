#!/usr/bin/python3
"""__Init__ file for HappyPup project.
This module creates a unique storage instance for the project"""
from os import getenv
from models.basemodel import BaseModel
from models.owner import Owner
from models.state import State
from models.city import City
from models.dog import Dog
from models.medical_centres import Medical_Centres

classes = {"BaseModel": BaseModel, "State": State, "City": City,
           "Owner": Owner, "Dog": Dog,
           "Medical_Centres": Medical_Centres}

# check environ var to determine storage method
if getenv('TYPE_STORAGE') == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
    storage.reload()

else:  # file storage selected
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
    storage.reload()
