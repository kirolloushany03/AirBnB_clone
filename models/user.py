#!/usr/bin/python3

"""User module defining the User class.

This module contains the definition of the User class, which
inherits attributes and methods from the BaseModel class.

Classes:
    User: A class representing a user in the HBNB project.

Usage:
    To use the User class, import it from this module:
        from models.user import User

    Create instances of the User class and use its methods and
    attributes as needed.

Example:
    # Create a new User instance
    user1 = User(email="user@example.com", password="password")

    # Access attributes of the User instance
    print(user1.id)          # Output: <user_id>
    print(user1.email)       # Output: user@example.com
    print(user1.password)    # Output: password
    print(user1.first_name)  # Output: ''
    print(user1.last_name)   # Output: ''

Attributes:
    email (str): The email address of the user.
    password (str): The password of the user.
    first_name (str): The first name of the user.
    last_name (str): The last name of the user.

Methods:
    __init__: Initializes a User instance.

"""


from models.base_model import BaseModel


class User(BaseModel):
    """The class User that inherits from BaseModel"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
