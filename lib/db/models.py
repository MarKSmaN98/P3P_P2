from sqlalchemy import ForeignKey, Column, String, Integer
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Town(Base):
    __tablename__ = 'towns'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    state = Column(String())
    restaurants = relationship("Restaurant", backref=backref('restaurant'))

    def __repr__(self):
        return f"Name: {self.name}, State: {self.state}"

class Restaurant(Base):
    __tablename__ = 'restaurants'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    address = Column(String())
    phone = Column(Integer())
    town_id = Column(Integer(), ForeignKey('towns.id'))
    reviews = relationship("Review", backref=backref('review'))

    def __repr__(self):
        return f"Restaurant Name: {self.name}, Address: {self.address}, Phone: {self.phone}"
    
class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer(), primary_key=True)
    review_text = Column(String())
    review_rating = Column(Integer())
    restaurant_id = Column(Integer(), ForeignKey('restaurants.id'))
