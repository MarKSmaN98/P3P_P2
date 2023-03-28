from db.models import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import time

engine = create_engine('sqlite:///thriddb.db')
Session = sessionmaker(bind=engine)
session = Session()

print("try this...")

time.sleep(5)
