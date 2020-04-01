#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer
from models.city import City
import models
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """This is the class for State
    """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all,delete", backref="state")

    @property
    def cities(self):
        """Return all cities"""
        from models import storage
        allcities = storage.all(City)
        city_list = [v for v in models.storage.all(City).values()
        if v.state_id == self.id]
        return city_list
