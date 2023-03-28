from faker import Faker
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import (Base, Town, Restaurant)

if __name__ == '__main__':
    engine = create_engine('sqlite:///thirddb.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    session.query(Town).delete()
    session.query(Restaurant).delete()

    ocala = Town(name="Ocala", state="Florida")
    session.add(ocala)
    session.commit()
    tacobell = Restaurant(name="Taco Bell", address="123asdf", phone=0, town_id=ocala.id)
    session.add(tacobell)
    session.commit()
    wendys = Restaurant(name="Wendy's", address="123asdf", phone=0, town_id=ocala.id)
    session.add(wendys)
    session.commit()