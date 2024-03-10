#!/usr/bin/python3

"""BaseModel module defining the BaseModel class.

This module contains the definition of the BaseModel class, which
serves as the base class for other classes in the HBNB project. The
BaseModel class provides common attributes and methods such as ID
generation, timestamp management, serialization, and string
representation.

Classes:
    BaseModel: A class serving as the base model for other classes
    in the HBNB project.

Usage:
    To use the BaseModel class, import it from this module:
        from models.base_model import BaseModel

    Create instances of the BaseModel class and use its methods and
    attributes as needed.

Example:
    # Create a new BaseModel instance
    base_model1 = BaseModel()

    # Access attributes of the BaseModel instance
    print(base_model1.id)          # Output: <base_model_id>
    print(base_model1.created_at)  # Output: <creation_timestamp>
    print(base_model1.updated_at)  # Output: <update_timestamp>

Methods:
    __init__: Initializes a BaseModel instance.
    __str__: Returns a string representation of the BaseModel
    instance.
    save: Updates the update timestamp and saves the instance to the
    storage.
    to_dict: Returns a dictionary representation of the BaseModel
    instance.

Attributes:
    id (str): The unique identifier of the BaseModel instance.
    created_at (datetime): The timestamp indicating the creation
    time of the BaseModel instance.
    updated_at (datetime): The timestamp indicating the last update
    time of the BaseModel instance.

For more information about the HBNB project, visit:
https://github.com/your_repository/hbnb

"""


import uuid
from datetime import datetime
import models


class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)
        else:
            # from models import storage  # 1

            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)  # 3

    def __str__(self):
        return f"{[self.__class__.__name__]} ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        dic_data = self.__dict__.copy()
        dic_data["__class__"] = self.__class__.__name__
        dic_data["created_at"] = self.created_at.isoformat()
        dic_data["updated_at"] = self.created_at.isoformat()
        return dic_data
