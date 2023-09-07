import sys
import os

current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model.models import Base

DATABASE_URI = 'sqlite:///finntasker.db'

engine = create_engine(DATABASE_URI)

Session = sessionmaker(bind=engine)
session = Session()

create_db = Base.metadata.create_all(engine)