#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship, backref
import os
from sqlalchemy import MetaData, Table

metadata = Base.metadata

place_amenity = Table('place_amenity', metadata,
                      Column('place_id', String(60),
                             ForeignKey("places.id"),
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey("amenities.id"),
                             primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """This class define a table with various atributtes"""
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship("Review", backref="place",
                               cascade="all, delete")
        amenities = relationship("Amenity", backref="place",
                                 cascade="all, delete", viewonly=False,
                                 secondary="place_amenity")

    else:
        @property
        def place(self):
            """getter method place"""
            _places = []
            for _id, obj in models.storage.all(Place).items():
                if self.id == obj.place_id:
                    _places.append(obj)
            return _places

        @property
        def amenities(self):
            """getter method amenities"""
            _amenities = []
            for _id, obj in models.storage.all(Amenity).items():
                if self.id == obj.place_id:
                    _amenities.append(obj)
            return _amenities

        @amenities.setter
        def amenities(self, value):
            """setter method"""
            if type(value) is 'Amenity':
                self.amenity_ids.append(value.id)
