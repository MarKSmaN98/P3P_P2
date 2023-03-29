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
        self.start()

    def init(self):
        print("Starting CLI Interface...\n")
        time.sleep(.5)
        print(' . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .')
        time.sleep(.5)
        print('.                                                                    .')
        time.sleep(.5)
        print('.                        MARK COATS                                  .')
        time.sleep(.5)
        print('.                        RAYMOND AN                                  .')
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
        print("finish start")
        self.start()

    def menu(self):
        print("1) Retrieve Data of Towns, Restaurants, Review")
        print("2) ...")
        print("3) ...")
        print("4) ...")
        print("5) Quit")

    def start(self):
        print('Welcome to PlatePal {self.name}')
        exit = False
        while exit == False:
            self.menu()
            sel = input("What would you like to do?: ")

            if sel == '1':
                get_data(self)
            elif sel == '2':
                pass

            elif sel == '3':
                pass

            elif sel == '4':
                pass

            elif sel == '5':
                exit = True
            
            else:
                print("Invalid Input!")
                print ("Restarting")
                for _ in range(4):
                    print('.', end=' ')
                    time.sleep(.5)
                print('\n')
                os.system('cls' if os.name == 'nt' else 'clear')
                self.init()
            # z = input("Would You Like To Continue?\n")
            # if z == 'q' or z == 'Q':
            #     exit = True

def get_data(self):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Data Catalogue")
    for _ in range(5):
        print('  ')
    #sub menu
    print("1) Towns")
    print('2) Restaurants')
    print('3) Reviews')
    sel = input("Select a Catalogue: ")
    print('  ')
    if sel == '1':
        print_towns(self.towns)
    elif sel == '2':
        print_restaurants(self.restaurants)
    elif sel == '3':
        print_reviews(self.reviews)

# def view_T_R(self):
#     count = 0
#     for town in self.towns:
#         print(f'{town.name}____________________________')
#         for rest in self.restaurants:
#             if rest.town_id == town.id:
#                 print("         ___")
#                 print(f'        {rest.name}')
#                 print("         ___")
#         count += 1
#         if count % 50 == 0:
#             sel = input("Press Enter To Continue Or Q to Quit ")
#             if sel == 'q' or sel == 'Q':
#                 break

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
        print_restaurant(restaurant)
        count += 1
        if count % 50 == 0:
            sel = input("Press Enter To Continue Or Q to Quit ")
            if sel == 'q' or sel == 'Q':
                break

    print('  ')

def print_restaurant(restaurant):
    print('')
    print(f'Restaurant: {restaurant.name}')
    print(f'     Address: {restaurant.address}')
    print(f'     Phone:   {restaurant.phone}')

def print_reviews(reviews):
    count = 0

    print('  ')
    print('**Reviews**')
    print('  ')
    for index, review in enumerate(reviews):
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

if __name__ == '__main__':
    engine = create_engine('sqlite:///db/thirddb.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    user_input = input("Enter Username: ")
    CLI(user_input)
    time.sleep(5)