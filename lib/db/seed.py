from faker import Faker
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import (Base, Town, Restaurant, Review)

if __name__ == '__main__':
    engine = create_engine('sqlite:///thirddb.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    session.query(Town).delete()
    session.query(Restaurant).delete()
    session.query(Review).delete()

    ocala = Town(name="Ocala", state="Florida")
    session.add(ocala)
    session.commit()
    tacobell = Restaurant(name="Taco Bell", address="123asdf", phone=0, town_id=ocala.id)
    session.add(tacobell)
    session.commit()
    wendys = Restaurant(name="Wendy's", address="123asdf", phone=0, town_id=ocala.id)
    session.add(wendys)
    session.commit()
    review1 = Review(review_text='Tacos', review_rating=4.5, restaurant_id=tacobell.id)
    session.add(review1)
    session.commit()
    review2 = Review(review_text='Borgors', review_rating=4.3, restaurant_id=wendys.id)
    session.add(review2)
    session.commit()

