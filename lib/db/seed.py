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

    # ocala = Town(name="Ocala", state="Florida")
    # session.add(ocala)
    # session.commit()
    # tacobell = Restaurant(name="Taco Bell", address="123asdf", phone=0, town_id=ocala.id)
    # session.add(tacobell)
    # session.commit()
    # wendys = Restaurant(name="Wendy's", address="123asdf", phone=0, town_id=ocala.id)
    # session.add(wendys)
    # session.commit()
    # review1 = Review(review_text='Tacos', review_rating=4.5, restaurant_id=tacobell.id)
    # session.add(review1)
    # session.commit()
    # review2 = Review(review_text='Borgors', review_rating=4.3, restaurant_id=wendys.id)
    # session.add(review2)
    # session.commit()

    faker = Faker()

    restaurant_names = ["Taco Bell", "Chipotle", "Burger King", "Wendys", "Kabob House", "Cook Out"]
    state_names = [ 'AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA',
           'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME',
           'MI', 'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM',
           'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX',
           'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY']

    towns = []

    for _ in range(50):
        town = Town(
            name=f"{faker.first_name()} Town",
            state=random.choice(state_names),
        
        )
        session.add(town)
        session.commit()
        towns.append(town)

    restaurants = []

    for town in towns:
        for _ in range(random.randint(1,5)):
            restaurant = Restaurant(
                 name=random.choice(restaurant_names),
                 address=faker.street_address(),
                 phone=random.randint(1000000000, 9999999999),
                 town_id=town.id

            )
            session.add(restaurant)
            session.commit()
            restaurants.append(restaurant)

    reviews = []
    for restaurant in restaurants:
        for _ in range(random.randint(1,3)):
            review = Review(
                review_text=faker.paragraph(nb_sentences=1),
                review_rating=random.randint(1,5),
                restaurant_id=restaurant.id

            )
            session.add(review)
            session.commit()
            reviews.append(review)
