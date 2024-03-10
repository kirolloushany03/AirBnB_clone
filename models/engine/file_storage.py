#!/usr/bin/python3

"""FileStorage module providing file-based storage for instances of classes.

This module defines the FileStorage class, which serves as a link between
JSON files and the program. It provides methods to save, reload, create,
and retrieve instances of various classes such as User, State, City, Amenity,
Place, Review, and BaseModel.

Classes:
    FileStorage: A class providing file-based storage functionality.

Usage:
    To use the FileStorage class, import it from this module:
        from models.engine.file_storage import FileStorage

    Create an instance of the FileStorage class and use its methods to
    manage instances of classes.

Example:
    # Create a new FileStorage instance
    storage = FileStorage()

    # Save objects to the file
    storage.save()

    # Reload objects from the file
    storage.reload()

Methods:
    all: Returns a dictionary containing all stored objects.
    new: Adds a new object to the storage dictionary.
    save: Saves the objects to a JSON file.
    reload: Reloads the objects from a JSON file.
    get_class: Retrieves the class associated with the class name.

Attributes:
    __file_path (str): The file path for storing JSON data.
    __objects (dict): A dictionary containing stored objects.

"""


import json

from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.base_model import BaseModel


class FileStorage:  # link between json and our program

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns a dictionary containing all stored objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Adds a new object to the storage dictionary."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.all()[key] = obj

    def save(self):
        """Saves the objects to a JSON file."""
        data = {}
        for key, value in FileStorage.__objects.items():
            data[key] = value.to_dict()
        with open(self.__file_path, "w") as file:
            json.dump(data, file)

    def reload(self):
        """Reloads the objects from a JSON file."""
        try:
            with open(self.__file_path, "r") as file:
                data = json.load(file)  # convert json to python dictionary
        except FileNotFoundError:
            return
        for key, value in data.items():
            # class_name, obj_id = key.split(".")
            # cls = eval(self.class_name)
            # cls = globals().get(class_name)
            cls = self.get_class(value["__class__"])
            if cls:
                self.__objects[key] = cls(**value)

    @staticmethod
    def get_class(class_name):
        """Retrieves the class associated with the class name."""
        mapping_class = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review,
        }
        return mapping_class.get(class_name)
