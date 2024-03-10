#!/usr/bin/python3

"""State module defining the State class.

This module contains the definition of the State class,
which inherits attributes and methods from the BaseModel
class.

Classes:
    State: A class representing a state in the HBNB project.

Usage:
    To use the State class, import it from this module:
        from models.state import State

    Create instances of the State class and use its methods
    and attributes as needed.

Example:
    # Create a new State instance
    state1 = State(name="California")

    # Access attributes of the State instance
    print(state1.id)       # Output: <state_id>
    print(state1.name)     # Output: California

Attributes:
    name (str): The name of the state.

Methods:
    __init__: Initializes a State instance.

"""


from models.base_model import BaseModel


class State(BaseModel):
    """The class State that inherits from BaseModel"""

    name = ""
