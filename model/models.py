from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)

class Bill(Base):
    __tablename__ = 'bills'
    id = Column(Integer, primary_key=True)
    description = Column(String, nullable=False)
    amount = Column(Integer, nullable=False)
    due_date = Column(DateTime, nullable=False)

class Investment(Base):
    __tablename__ = 'investments'
    id = Column(Integer, primary_key=True)
    description = Column(String, nullable=False)
    amount = Column(Integer, nullable=False)