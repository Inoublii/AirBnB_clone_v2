#!/usr/bin/python3
"""This is the city class"""
from models.base_model import BaseModel


class City(BaseModel):
    """This is the class for City
    """
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)


