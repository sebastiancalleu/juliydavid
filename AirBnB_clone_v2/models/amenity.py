#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from os import getenv
from models.place import Place
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """ Class for HBNB project Amenity """
    __tablename__ = 'amenities'
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        place_amenities = relationship('Place', secondary='place_amenity')
    else:
        name = ''
