from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)

    bills = relationship("Bill", back_populates="user")
    investments = relationship("Investment", back_populates="user")

class Bill(Base):
    __tablename__ = 'bills'
    id = Column(Integer, primary_key=True)
    description = Column(String, nullable=False)
    amount = Column(Integer, nullable=False)
    due_date = Column(DateTime, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates='bills')
                     

class Investment(Base):
    __tablename__ = 'investments'
    id = Column(Integer, primary_key=True)
    description = Column(String, nullable=False)
    amount = Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship('User', back_populates= 'investments')