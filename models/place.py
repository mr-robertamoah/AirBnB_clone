#!/usr/bin/python3

"""
this is a module containg the Place class
"""

from models.base_model import BaseModel


class Place(BaseModel):
    """
    Place class which inherits the BaseModel
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guests = 0
    price_by_height = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
