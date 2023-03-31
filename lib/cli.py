#!/usr/bin/env python3
from db.models import Town, Restaurant, Review
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import time, random, os



class CLI:
    def __init__(self, user_input = "undefined"):
        self.towns = [town for town in session.query(Town)]
        self.restaurants = [restaurant for restaurant in session.query(Restaurant)]
        self.reviews = [review for review in session.query(Review)]
        self.name = user_input
        self.init()

    def init(self):
        print("Starting CLI Interface...\n")
        time.sleep(.5)
        print(' . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .')
        time.sleep(.5)
        print('.                                                                    .')
        time.sleep(.5)
        print('.                        RAYMOND AN                                  .')
        time.sleep(.5)
        print('.                        MARK COATS                                  .')
        time.sleep(.5)
        print(".                        KYLE O'NEILL                                .")
        time.sleep(.5)
        print('.                                                                    .')
        time.sleep(.5)
        print(' . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .')
        for _ in range(4):
            print('.                                                                    .')
            time.sleep(.5)
        print('\n')
        self.start()

    def menu(self):
        print("1) Retrieve Data of Towns, Restaurants, Review")
        print("2) View Relationships")
        print("3) Add Data")
        print("4) Quit")

    def start(self):
        print(f'Welcome to PlatePal {self.name}\n\n')
        exit = False
        while exit == False:
            self.menu()
            sel = input("What would you like to do?: ")

            if sel == '1':
                get_data(self)
            elif sel == '2':
                start_rel_viewer(self)

            elif sel == '3':
                add_data(self)


            elif sel == '4':
                exit = True
            
            else:
                print("Invalid Input! Restarting Main Menu...")
                time.sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')
        printer(self.name)
def add_data(self):
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        print("What do you want to add?")
        #sub menu
        print("     1) Town")
        print('     2) Restaurant')
        print('     3) Review')
        print('     4) Exit')

        sel = input("Select an option: ")
        print('  ')
        if sel == '1':
            name = input("Type Town Name: ")
            print(' ')
            state = input("Type State: ")
            town = Town(name=name, state=state)
            session.add(town)
            session.commit()
            self.towns.append(town)

        elif sel == '2':
            print_towns(self.towns)
            print(' ')
            user_input = input("Is your town in the list above? (Type Y/N): ")
            print(' ')

            while user_input != "Y" and user_input != "y":
                add_data(self)
                print(' ')
                print_towns(self.towns)
                print(' ')
                user_input = input("Is your town in the list above? (Type Y/N): ")
                print(' ')

            make_restaurant(self)

        elif sel == '3':
            print_restaurants(self.restaurants)
            print(' ')
            user_input = input("Is your restaurant in the list above? (Type Y/N): ")
            print(' ')

            while user_input != "Y" and user_input != "y":
                add_data(self)
                print(' ')
                print_towns(self.restaurants)
                print(' ')
                user_input = input("Is your restaurant in the list above? (Type Y/N): ")
                print(' ')

            make_review(self)
        elif sel == '4':
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        else:
            print("invalid input!")
            time.sleep(1)

def make_restaurant(self):
    user_town = input("Type the number of the town from the list above: ")
    name = input("Name of Restaurant: ")
    address = input("Address of Restaurant: ")
    phone = input("Phone number of Restaurant: ")
    restaurant = Restaurant(
        name = name,
        address = address,
        phone = phone,
        town_id = self.towns[int(user_town)-1].id
    )
    session.add(restaurant)
    session.commit()
    self.restaurants.append(restaurant)
    print(' ')
    print('Congrats! You added the restaurant to your PlatePal!')
    print_restaurant(restaurant)

def make_review(self):
    user_restaurant = input("Type the number of the restaurant from the list above: ")
    review = input("Leave your Review!!!: ")
    rating = input("How many stars? (Out of 5): ")
    review = Review(
        review_text = review,
        review_rating = rating,
        restaurant_id = self.restaurants[int(user_restaurant)-1].id
    )
    session.add(review)
    session.commit()
    self.reviews.append(review)
    print(' ')
    print('Congrats! You added the review to your PlatePal!')
    print_review(review)


def get_data(self):
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        print("Data Catalogue")
        #sub menu
        print("     1) Towns")
        print('     2) Restaurants')
        print('     3) Reviews')
        print('     4) Exit')
        sel = input("Select a Catalogue: ")
        print('  ')
        if sel == '1':
            print_towns(self.towns)
        elif sel == '2':
            print_restaurants(self.restaurants)
        elif sel == '3':
            print_reviews(self.reviews)
        elif sel == '4':
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        else:
            print("invalid input!")
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')





def print_towns(towns):
    count = 0
    print('  ')
    print('**Towns**')
    print('  ')
    for index, town in enumerate(towns):
        print(f'{index+1}. {town.name}')
        count += 1
        if count % 20 == 0:
            sel = input("Press Enter To Continue Or Q to Quit ")
            if sel == 'q' or sel == 'Q':
                break
    print('  ')

def print_restaurants(restaurants):
    count = 0
    print('  ')
    print('**Restaurants**')
    print('  ')
    for index, restaurant in enumerate(restaurants):
        print(f'{index+1}.')
        print_restaurant(restaurant)
        count += 1
        if count % 50 == 0:
            sel = input("Press Enter To Continue Or Q to Quit ")
            if sel == 'q' or sel == 'Q':
                break

    print('  ')

def print_restaurant(restaurant):
    print(f'Restaurant: {restaurant.name}')
    print(f'     Address: {restaurant.address}')
    print(f'     Phone:   {restaurant.phone}')

def print_reviews(reviews):
    count = 0

    print('  ')
    print('**Reviews**')
    print('  ')
    for index, review in enumerate(reviews):
        print(f'{index+1}.')
        print_review(review)
        count += 1
        if count % 100 == 0:
            sel = input("Press Enter To Continue Or Q to Quit ")
            if sel == 'q' or sel == 'Q':
                break

    print('  ')

def print_review(review):
    print('')
    print(f'Review: {review.review_text}')
    print(f'Rating: {review.review_rating} Stars')

#__________________________RELATIONSHIP VIEWER_____________________________________
#Mark Coats

def start_rel_viewer(self):
    os.system('cls' if os.name == 'nt' else 'clear')
    sub_exit = False
    while sub_exit == False:
        print("....Relationship Viewer....\n\n")
        print("Town to Restauraunt")
        print("Restaurant to Review")
        print("Exit")

        sel = input("Select an Option: ")

        if sel == '1':
            view_T_R(self)
        elif sel == '2':
            view_R_r(self)
        elif sel == '3':
            sub_exit = True
            print("Returning To Main Menu...")
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            print("invalid input!")
            time.sleep(1)
            start_rel_viewer(self)

def view_T_R(self):
    count = 0
    for town in self.towns:
        print(f'{town.name}____________________________')
        for rest in self.restaurants:
            if rest.town_id == town.id:
                print("         ___")
                print(f'        {rest.name}')
                print("         ___")
        count += 1
        if count % 50 == 0:
            sel = input("Press Enter To Continue Or Q to Quit ")
            if sel == 'q' or sel == 'Q':
                break

def view_R_r(self):
    count = 0
    for rest in self.restaurants:
        print(f'{rest.name}____________________________')
        for rev in self.reviews:
            if rev.restaurant_id == rest.id:
                print("         ___")
                print(f'        {rev.review_text}')
                print(f'        {rev.review_rating} Stars')
                print("         ___")
        count += 1
        if count % 50 == 0:
            sel = input("Press Enter To Continue Or Q to Quit ")
            if sel == 'q' or sel == 'Q':
                break


#________________________________END RELATIONSHIP VIEWER_____________________________



def printer(user_input):
    print(f'Goodbye {user_input}')
if __name__ == '__main__':
    engine = create_engine('sqlite:///db/thirddb.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    user_input = input("Enter Username: ")
    CLI(user_input)
    time.sleep(5)