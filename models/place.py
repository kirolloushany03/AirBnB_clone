#!/usr/bin/python3
"""Place module defining the Place class.

This module contains the definition of the Place class, which
inherits attributes and methods from the BaseModel class.

Classes:
    Place: A class representing a place in the HBNB project.

Usage:
    To use the Place class, import it from this module:
        from models.place import Place

    Create instances of the Place class and use its methods and
    attributes as needed.

Example:
    # Create a new Place instance
    place1 = Place(name="Cozy Apartment", city_id="456", user_id="789")

    # Access attributes of the Place instance
    print(place1.id)              # Output: <place_id>
    print(place1.city_id)         # Output: 456
    print(place1.user_id)         # Output: 789
    print(place1.name)            # Output: Cozy Apartment
    print(place1.description)     # Output: ''
    print(place1.number_rooms)    # Output: 0
    print(place1.number_bathrooms)# Output: 0
    print(place1.max_guest)       # Output: 0
    print(place1.price_by_night)  # Output: 0
    print(place1.latitude)        # Output: 0.0
    print(place1.longitude)       # Output: 0.0
    print(place1.amenity_ids)     # Output: []

Attributes:
    city_id (str): The ID of the city associated with the place.
    user_id (str): The ID of the user who owns the place.
    name (str): The name of the place.
    description (str): The description of the place.
    number_rooms (int): The number of rooms in the place.
    number_bathrooms (int): The number of bathrooms in the place.
    max_guest (int): The maximum number of guests the place can accommodate.
    price_by_night (int): The price per night for the place.
    latitude (float): The latitude coordinate of the place.
    longitude (float): The longitude coordinate of the place.
    amenity_ids (list): A list of IDs of amenities associated with the place.

Methods:
    __init__: Initializes a Place instance.

"""


from models.base_model import BaseModel


class Place(BaseModel):
    """The class Place that inherits from BaseModel"""

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
    # def __init__(self, *args, **kwargs):
    #     """Initialize Place instance"""
    #     super().__init__(*args, **kwargs)
    #     self.city_id = kwargs.get("city_id", "")
    #     self.user_id = kwargs.get("user_id", "")
    #     self.name = kwargs.get("name", "")
    #     self.description = kwargs.get("description", "")
    #     self.number_rooms = kwargs.get("number_rooms", 0)
    #     self.number_bathrooms = kwargs.get("number_bathrooms", 0)
    #     self.max_guest = kwargs.get("max_guest", 0)
    #     self.price_by_night = kwargs.get("price_by_night", 0)
    #     self.latitude = kwargs.get("latitude", 0.0)
    #     self.longitude = kwargs.get("longitude", 0.0)
    #     self.amenity_ids = kwargs.get("amenity_ids", [])
