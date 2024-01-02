#!/usr/bin/python3
"""
place module defines the Place class
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    dscribs attributes/methods, dscription a place 
    should have orchoose from
    """

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
