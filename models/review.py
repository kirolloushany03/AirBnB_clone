#!/usr/bin/python3

"""Review module defining the Review class.

This module contains the definition of the Review class, which
inherits attributes and methods from the BaseModel class.

Classes:
    Review: A class representing a review in the HBNB project.

Usage:
    To use the Review class, import it from this module:
        from models.review import Review

    Create instances of the Review class and use its methods and
    attributes as needed.

Example:
    # Create a new Review instance
    review1 = Review(place_id="123", user_id="456", text="Great place!")

    # Access attributes of the Review instance
    print(review1.id)       # Output: <review_id>
    print(review1.place_id) # Output: 123
    print(review1.user_id)  # Output: 456
    print(review1.text)     # Output: Great place!

Attributes:
    place_id (str): The ID of the place associated with the review.
    user_id (str): The ID of the user who created the review.
    text (str): The content of the review.

Methods:
    __init__: Initializes a Review instance.

"""


from models.base_model import BaseModel


class Review(BaseModel):
    """The class Review that inherits from BaseModel"""

    place_id = ""
    user_id = ""
    text = ""
