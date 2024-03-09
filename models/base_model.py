#!/usr/bin/python3
"""The module contains the class BaseModel"""
from uuid import uuid4
from datetime import datetime
from models import storage


class BaseModel():
    """The class BaseModel that defines all common \
    attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """Insilization"""

        if kwargs:
            kwargs["created_at"] = datetime.strptime(
                kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
            kwargs["updated_at"] = datetime.strptime(
                kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Retrun: [<class name>] (<self.id>) <self.__dict__>"""

        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def __repr__(self):
        """Retrun: [<class name>] (<self.id>) <self.__dict__>"""

        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates the public instance attribute \
            updated_at with the current datetime"""

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dictionary containing all \
            keys/values of __dict__ of the instance"""

        object_dict = self.__dict__.copy()
        object_dict["created_at"] = object_dict["created_at"].isoformat()
        object_dict["updated_at"] = object_dict["updated_at"].isoformat()
        object_dict["__class__"] = self.__class__.__name__
        return object_dict
