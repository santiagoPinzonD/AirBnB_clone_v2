#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column("name", String(128), nullable=True)
    if getenv('HBNB_TYPE_STORAGE') == "bd":
        cities = relationship("City", cascade='all, delete', backref='state')

    @property
    def cities(self):
        """getter"""
        inst = []
        dic = models.storage.all(City)
        for k, v in dic.items():
            if v.state_id == self.id:
                inst.append(v)
        return inst
