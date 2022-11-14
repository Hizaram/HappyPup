#!/usr/bin/python3
"""This module defines a file storage class for HappyPup project"""
import json


class FileStorage:
    """This class manages storage of HappyPup models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        obj_list = FileStorage.__objects
        if cls:
            obj_list = {}
            for key, value in FileStorage.__objects.items():
                if type(value) == cls:
                    obj_list[key] = value
        return obj_list

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.basemodel import BaseModel
        from models.owner import Owner
        from models.dog import Dog
        from models.state import State
        from models.city import City
        from models.medical_centres import Medical_Centres

        classes = {
                    'BaseModel': BaseModel, 'Owner': Owner, 'Dog': Dog,
                    'State': State, 'City': City,
                    'Medical_Centres': Medical_Centres,
                  }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """deletes an object"""
        if obj:
            key = obj.__class__.__name__ + '.' + obj.id
            del FileStorage.__objects[key]
            self.save()

    def close(self):
        """Closes a session and deserializes our JSON file"""
        self.reload()
