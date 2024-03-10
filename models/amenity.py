#!/usr/bin/python3

"""Amenity module defining the Amenity class.

This module contains the definition of the Amenity class, which
represents an amenity associated with a place in the HBNB project.
The Amenity class inherits attributes and methods from the BaseModel
class.

Classes:
    Amenity: A class representing an amenity in the HBNB project.

Usage:
    To use the Amenity class, import it from this module:
        from models.amenity import Amenity

    Create instances of the Amenity class and use its methods and
    attributes as needed.

Example:
    # Create a new Amenity instance
    amenity1 = Amenity(name="Wifi")

    # Access attributes of the Amenity instance
    print(amenity1.id)      # Output: <amenity_id>
    print(amenity1.name)    # Output: Wifi

Attributes:
    name (str): The name of the amenity.

Methods:
    __init__: Initializes an Amenity instance.

"""


from models.base_model import BaseModel


class Amenity(BaseModel):
    """The class Amenity that inherits from BaseModel"""

    name = ""
