#!/usr/bin/python3
"""A database storage engine"""
import models
from models.basemodel import BaseModel, Base
from models.owner import Owner
from models import classes
from models.medical_centres import Medical_Centres
from models.city import City
from models.state import State
from models.dog import Dog
from sqlalchemy import create_engine
from os import getenv
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm.session import sessionmaker, Session
from models import classes


class DBStorage:
    """DBStorage of the HappyPup project"""
    __engine = None
    __session = None

    def __init__(self):
        """Initialises the SQLAlchemy engine"""
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}:3306/{}"
                                      .format(getenv('MYSQL_USER'),
                                              getenv('MYSQL_PWD'),
                                              getenv('MYSQL_HOST'),
                                              getenv('MYSQL_DB')),
                                      pool_pre_ping=True)
        # drop tables if the environment is test
        if getenv('H_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Method that queries and returns all objects by class"""
        """Query and return all objects by class/generally
        Return: dictionary (<class-name>.<object-id>: <obj>)
        """
        obj_dict = {}
        objs = None

        if cls:
            if cls in classes:
                cls = classes[cls]
            objs = self.__session.query(cls)
        else:
            objs = self.__session.query(
                    Owner, State, City, Dog, Medical_Centres)
        for row in objs:
            # populate dict with objects from storage
            key = '{}.{}'.format(type(row).__name__, row.id)

            obj_dict[key] = row
        return obj_dict

    def new(self, obj):
        """Adds object to current database session"""
        self.__session.add(obj)

    def save(self):
        """Commits the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes an object from the current session if obj not None"""
        if obj:
            # if an object is provided, determine class from obj
            cls_name = classes[type(obj).__name]

            # query class table and delete
            self.__session.query(cls_name) \
                .filter(cls_name.id == obj.id).delete()

    def reload(self):
        """Creates the database session"""
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=self.__engine, expire_on_commit=False)

        # allows session to be reused
        self.__session = scoped_session(session)

    def close(self):
        """Closes scoped session"""
        self.__session.remove()
