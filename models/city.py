#!/usr/bin/python3

"""City module defining the City class.

This module contains the definition of the City class, which
inherits attributes and methods from the BaseModel class.

Classes:
    City: A class representing a city in the HBNB project.

Usage:
    To use the City class, import it from this module:
        from models.city import City

    Create instances of the City class and use its methods and
    attributes as needed.

Example:
    # Create a new City instance
    city1 = City(name="New York", state_id="123")

    # Access attributes of the City instance
    print(city1.id)         # Output: <city_id>
    print(city1.state_id)   # Output: 123
    print(city1.name)       # Output: New York

Attributes:
    state_id (str): The ID of the state associated with the city.
    name (str): The name of the city.

Methods:
    __init__: Initializes a City instance.

"""


from models.base_model import BaseModel


class City(BaseModel):
    """The class City that inherits from BaseModel"""

    state_id = ""
    name = ""
