#!/usr/bin/python3
"""module: model_state
Used to create table states using SQLAlchemy"""
from sqlalchemy import Integer, String, Column
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """State class to represent the states table"""
    __tablename__ = 'states'  # declaring the table name
    id = Column(Integer, unique=True, nullable=False, primary_key=True,
                autoincrement=True)
    name = Column(String(128), nullable=False)
