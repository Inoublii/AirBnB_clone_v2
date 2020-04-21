#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer
import models
from sqlalchemy.orm import relationship
import os

storage_type = os.getenv('HBNB_TYPE_STORAGE')


class State(BaseModel, Base):
    """This is the class for State
    """
    __tablename__ = 'states'

    if (storage_type == 'db'):
        name = Column(String(128), nullable=False)
        cities = relationship("City", cascade="all,delete", backref="state")
    else:
        name = ''
    @property
    def cities(self):
        """Return all cities"""
        from models import storage
        allcities = storage.all(City)
        city_list = [v for v in models.storage.all(City).values()
                     if v.state_id == self.id]
        return city_list
